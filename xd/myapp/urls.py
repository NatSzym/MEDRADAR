from django.urls import path
from . import views

urlpatterns = [
    path("account/", views.home, name="home"),
    path("", views.home2, name="home2"),
    path("<int:year>/<str:month>/", views.home, name="home"),
    path("doctors/", views.doctor, name="doctors"),
    path("patients/", views.patient, name="patients"),
    path("appointments/", views.appointment, name="appointments"),
    path("add_appointment/", views.add_appointment, name = "add_appointment"),
    path("add_patient_or_doctor/", views.add_patient_or_doctor, name = "add_patient_or_doctor"),
    path("contact/", views.contact, name="contact"),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_available_times/', views.GetAvailableTimesView.as_view(), name='get_available_times'),
]
