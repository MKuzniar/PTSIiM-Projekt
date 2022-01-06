import django_filters
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .serializer import *
from .models import *


class AppointmentFilter(filters.FilterSet):
    date_of_appointment_l = django_filters.CharFilter(field_name='date_of_appointment', lookup_expr='lte')
    date_of_appointment_g = django_filters.CharFilter(field_name='date_of_appointment', lookup_expr='gte')

    class Meta:
        model = Appointment
        fields = ('id', 'patient_id', 'doctor_id')


class CommentFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = ('appointment_id',)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-date_of_appointment')
    serializer_class = AppointmentSerializer
    filterset_class = AppointmentFilter


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
