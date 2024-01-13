from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from babel.dates import format_date
from babel import Locale
from django.utils.html import format_html
from .forms import AppointmentForm, PatientForm
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from .models import Doctor, Patient, Appointment, UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = request.user.first_name
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    locale = Locale('pl_PL')
    now = datetime.now()
    current_data = now.date()
    time = now.strftime('%H:%M')
    formatted_date = format_date(current_data, format='full', locale=locale)
    return render(request, "home.html", {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_data": formatted_date,
        "time": time,

    })


def contact(request):
    return render(request, 'contact.html')


def home2(request):
    return render(request, 'home2.html')


def patient(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})


def doctor(request):
    doctors = Doctor.objects.all()
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    return render(request, 'doctors.html', {'doctors': doctors, 'specializations': specializations})



def appointment(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient)
    now = datetime.now()
    current_data = now.date()
    return render(request, 'appointments.html', {'appointments': appointments,
                                                 "current_data": current_data, })


@login_required
def get_doctors(request):
    specialization_id = request.GET.get('specialization_id')
    doctors = Doctor.objects.filter(specialization=specialization_id).values_list('id', 'first_name', 'last_name')
    doctors_list = list(doctors)
    return JsonResponse({'doctors': doctors_list})


class GetAvailableTimesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        doctor_id = request.GET.get('doctor_id')
        date = request.GET.get('date')
        date = datetime.strptime(date, '%Y-%m-%d').date()
        doctor = Doctor.objects.get(id=doctor_id)
        available_times = doctor.get_available_times(date)
        return JsonResponse({'available_times': available_times})


def add_appointment(request):
    submitted = False
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.doctor = doctor
            appointment.save()
            submitted = True
    else:
        form = AppointmentForm()

    return render(request, 'add_appointment.html', {'form': form, 'submitted': submitted})


@login_required
def add_patient_or_doctor(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    submitted = profile.form_submitted
    patient = None
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            profile.form_submitted = True
            profile.save()
            submitted = True
    try:
        patient = Patient.objects.get(user=request.user)
        form = PatientForm(initial=model_to_dict(patient))
        submitted = True
    except Patient.DoesNotExist:
        form = PatientForm(initial={'email': request.user.email, 'first_name': request.user.first_name,
                                    'last_name': request.user.last_name})
    return render(request, 'add_patient_or_doctor.html', {'form': form, 'submitted': submitted, 'patient': patient})
