from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Appointment, Patient, Doctor
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
import datetime
from datetime import date, datetime
from django.contrib.admin.widgets import AdminDateWidget


class AppointmentForm(forms.ModelForm):
    specialization = forms.ChoiceField(
        choices=Doctor.objects.values_list('specialization', 'specialization').distinct()
    )
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(choices=[])

    class Meta:
        model = Appointment
        fields = ('specialization', 'doctor', 'is_commercial', 'date', 'time')
        widgets = {
            'is_commercial': forms.Select(attrs={'class': 'form-control'}, choices=[('T', 'True'), ('F', 'False')]),
            'specialization': forms.Select(attrs={'class': 'form-control', 'id': 'id_specialization'}),
            'doctor': forms.Select(attrs={'class': 'form-control', 'id': 'id_doctor'}),
            'time': forms.Select(attrs={'class': 'form-control', 'id': 'id_time'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(f"self.instance: {self.instance}")
    #     print(f"self.instance.pk: {self.instance.pk if self.instance else None}")
    #     doctor_id = self.data.get('doctor')
    #     print(f"doctor_id: {doctor_id}")
    #     if doctor_id:
    #         doctor = Doctor.objects.get(pk=doctor_id)
    #         print(f"doctor: {doctor}")
    #         available_times = doctor.get_available_times(date.today())
    #         print(f"available_times: {available_times}")
    #         self.fields['time'].choices = [
    #             (time, time.strftime('%H:%M:%S')) for time in available_times
    #         ]
    #     else:
    #         available_times = Doctor.objects.first().get_available_times(date.today())
    #         print(f"available_times: {available_times}")
    #         self.fields['time'].choices = [
    #             (time, time.strftime('%H:%M:%S')) for time in available_times
    #         ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['time'].choices = [
                (time, time.strftime('%H:%M:%S')) for time in self.instance.doctor.get_available_times(self.instance.date)
            ]
        else:
            self.fields['time'].choices = [
                (time, time.strftime('%H:%M:%S')) for time in Doctor.objects.first().get_available_times(date.today())
            ]

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # if doctor and date:
        #     available_times = [
        #         (time, time.strftime('%H:%M:%S')) for time in doctor.get_available_times(date)
        #     ]
        #     self.fields['time'].choices = available_times
        #
        # return cleaned_data

        # if doctor and date and time:
        #     datetime_combined = datetime.combine(date, time)
        #     if datetime_combined < timezone.now():
        #         raise forms.ValidationError("Data i czas muszą być przyszłe")
        #
        #     # Check if the doctor is not None before accessing its properties
        #     if doctor:
        #         if Appointment.objects.filter(doctor=doctor, date=date, time=time).exists():
        #             raise forms.ValidationError("Ten termin jest już zajęty")



# TO DZIAŁA ALE ZAPISUJEMY SIĘ O PÓŁNOCY W JAKIKOLWIEK DZIEŃ CHCEMY
# class AppointmentForm(ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ('doctor', 'is_commercial', 'date', 'time')
#         widgets = {
#             'doctor': forms.Select(attrs={'class': 'form-control'}),
#             'is_commercial': forms.Select(attrs={'class': 'form-control'}, choices=[('T', 'True'), ('F', 'False')]),
#             'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'time': forms.Select(attrs={'class': 'form-control'}),
#         }

    # def clean_date(self):
    #     date = self.cleaned_data.get('date')
    #     if date and date < timezone.now():
    #         raise ValidationError("Data musi być przyszła")
    #     return date
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     doctor = cleaned_data.get('doctor')
    #     date = cleaned_data.get('date')
    #     if doctor and date:
    #         if Appointment.objects.filter(doctor=doctor, date=date).exists():
    #             raise ValidationError("Ten termin jest już zajęty")


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('email', 'first_name', 'last_name', 'pesel', 'birth_date', 'gender')
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'pesel': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=[('M', 'Male'), ('F', 'Female')]),
        }
