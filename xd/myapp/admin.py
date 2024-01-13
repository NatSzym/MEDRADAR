from django.contrib import admin
from .models import Doctor, Patient, Appointment, Day

# Register your models here.
#admin.site.register(Doctor)
#admin.site.register(Patient)
#admin.site.register(Appointment)
admin.site.register(Day)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization')
    ordering = ['specialization']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'pesel', 'birth_date', 'gender')
    ordering = ['last_name']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'is_commercial', 'date')
    ordering = ['date']
    filter = ('date',)

