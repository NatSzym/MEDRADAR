from datetime import date, datetime, timedelta, time, timezone
from django.utils import timezone
from django.core.validators import RegexValidator, EmailValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from babel.dates import format_date


# Create your models here.
class Day(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self):
        return self.day


# DAYS_MAPPING = {
#     'Poniedziałek': 'Monday',
#     'Wtorek': 'Tuesday',
#     'Środa': 'Wednesday',
#     'Czwartek': 'Thursday',
#     'Piątek': 'Friday',
#     'Sobota': 'Saturday',
#     'Niedziela': 'Sunday',
# }
#
#
# def time_to_minutes(t):
#     return t.hour * 60 + t.minute


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    working_days = models.ManyToManyField(Day)
    working_hours_start = models.TimeField(default=time(8, 0))
    working_hours_end = models.TimeField(default=time(15, 0))
    visit_time = models.IntegerField(default=15)
    break_start = models.TimeField(default=time(12, 0))
    break_duration = models.IntegerField(default=15)

    def get_available_times(self, date):
        available_times = []
        day_of_week = format_date(date, 'EEEE', locale='pl_PL').capitalize()
        if day_of_week not in list(self.working_days.values_list('day', flat=True)):
            return available_times
        else:
            start_time = datetime.combine(date.min, self.working_hours_start)
            end_time = datetime.combine(date.min, self.working_hours_end)

            break_start = datetime.combine(date.min, self.break_start)
            break_end = break_start + timedelta(minutes=self.break_duration)

            current_time = start_time
            available_times = []
            while current_time + timedelta(minutes=self.visit_time) <= end_time:
                if not (break_start <= current_time < break_end):
                    if not Appointment.objects.filter(doctor=self, date=date, time=current_time.time()).exists():
                        available_times.append(current_time.time())
                current_time += timedelta(minutes=self.visit_time)
            return available_times

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    email = models.EmailField(
        'User Email',
        default='xyz@wp.pl',
        unique=True,
        validators=[EmailValidator(message='Enter a valid email address.')]
    )
    first_name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex='^[a-zA-Z]*$',
            message='First name should only contain letters.'
        )]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Last name should only contain letters.'
        )]
    )
    pesel = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(
            regex='^[0-9]*$',
            message='PESEL should only contain digits.'
        )]
    )
    birth_date = models.DateField()
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    form_submitted = models.BooleanField(default=False)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    is_commercial = models.BooleanField(default=False)
    date = models.DateField(default='2015-05-06')
    time = models.TimeField(default=time(12, 0,0))

    # def clean(self):
    #     if not self.time:
    #         raise ValidationError(_('Nie wybrano godziny.'))
    #
    #     if self.date < timezone.now().date():
    #         raise ValidationError(_('Nie można wprowadzić daty z przeszłości.'))
    #
    #     if self.date == timezone.now().date() and self.time < timezone.now().time():
    #         raise ValidationError(_('Chyba nie zdążysz już przyjść? Ta godzina minęła.'))
    #
    #     day_of_week = format_date(self.date, 'EEEE', locale='pl_PL').capitalize()
    #     # print('day_of_week:', day_of_week)
    #     # working_days = list(self.doctor.working_days.values_list('day', flat=True))
    #     # print('working_days:', working_days)
    #     if day_of_week not in list(self.doctor.working_days.values_list('day', flat=True)):
    #         raise ValidationError(_('Wybrany lekarz nie pracuje w wybranym dniu.'))
    #
    #     if not (self.doctor.working_hours_start <= self.time <= self.doctor.working_hours_end):
    #         raise ValidationError(_('Wybrana godzina jest poza godzinami pracy lekarza.'))
    #
    #     break_end = (datetime.combine(date.min, self.doctor.break_start) + timedelta(
    #         minutes=self.doctor.break_duration)).time()
    #     if self.doctor.break_start <= self.time <= break_end:
    #         raise ValidationError(_('Wybrana godzina koliduje z przerwą lekarza.'))

    def save(self, *args, **kwargs):
        if not self.pk:
            available_times = self.doctor.get_available_times(self.date)
            if available_times:
                self.time = available_times[0]

        self.clean()
        super().save(*args, **kwargs)
