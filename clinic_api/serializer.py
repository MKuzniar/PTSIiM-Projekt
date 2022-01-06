from rest_framework import serializers

from .models import *


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'birthdate', 'gender')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'date_of_appointment', 'doctor_id', 'patient_id')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_text', 'appointment_id', 'doctor_id', 'patient_id')
