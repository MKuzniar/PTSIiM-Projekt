from urllib import request

from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    birthdate = models.DateField(null=False)
    gender = models.BooleanField(null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    date_of_appointment = models.DateField(null=False)
    doctor_id = models.ForeignKey(Doctor, null=False, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"Date of appointment: {self.date_of_appointment}, Doctor: {self.doctor_id}, Patient: {self.patient_id}"


class Comment(models.Model):
    comment_text = models.CharField(max_length=200, null=True)
    appointment_id = models.ForeignKey(Appointment, null=False, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment_text}, Appointment ID: {self.appointment_id}, Doctor ID: {self.doctor_id}, Patient ID:{self.patient_id} "
