from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django import forms

from web_app.forms import AppointmentForm, VisitForm
from datetime import datetime

import requests

from clinic_api.models import Appointment, Patient, Comment, Doctor

today = datetime.today().strftime('%Y-%m-%d')


def home(request):
    query = request.user.groups.values_list('name', flat=True)
    groups = list(query)

    if 'Patients' in groups:
        return render(request, 'web_app/patient_home.html')
    else:
        return render(request, 'web_app/doctor_home.html')


def planned_visits(request):
    query = request.user.groups.values_list('name', flat=True)
    groups = list(query)

    if 'Patients' in groups:
        context = {
            'data': requests.get(
                f'http://127.0.0.1:8000/api/appointments/?patient_id=3&doctor_id=&date_of_appointment_l=&date_of_appointment_g={today}').json()
        }

        for entry in context['data']:
            doctor_data = requests.get(f"{entry['doctor_id']}").json()
            entry['doctor_id'] = doctor_data['first_name'] + " " + doctor_data['last_name']

        for data in context['data']:
            appointment = data['id']
            comment = requests.get(f'http://127.0.0.1:8000/api/comments/?appointment_id={appointment}').json()
            for j in range(len(comment)):
                if comment[j]['patient_id'] is None:
                    text = comment[j]['comment_text']
                    data['doctor_com'] = text
                else:
                    text = comment[j]['comment_text']
                    data['patient_com'] = text

        return render(request, 'web_app/patient_planned_visits.html', context)
    else:
        context = {
            'data': requests.get(
                f'http://127.0.0.1:8000/api/appointments/?patient_id=&doctor_id=4&date_of_appointment_l=&date_of_appointment_g={today}').json()
        }

        for entry in context['data']:
            patient_data = requests.get(f"{entry['patient_id']}").json()
            entry['patient_id'] = patient_data['first_name'] + " " + patient_data['last_name']

        for data in context['data']:
            appointment = data['id']
            comment = requests.get(f'http://127.0.0.1:8000/api/comments/?appointment_id={appointment}').json()
            for j in range(len(comment)):
                if comment[j]['patient_id'] is None:
                    text = comment[j]['comment_text']
                    data['doctor_com'] = text
                else:
                    text = comment[j]['comment_text']
                    data['patient_com'] = text

        return render(request, 'web_app/doctor_planned_visits.html', context)


def history_visits(request):
    query = request.user.groups.values_list('name', flat=True)
    groups = list(query)

    if 'Patients' in groups:
        context = {
            'data': requests.get(
                f'http://127.0.0.1:8000/api/appointments/?patient_id=3&doctor_id=&date_of_appointment_l={today}&date_of_appointment_g=').json()
        }

        for entry in context['data']:
            doctor_data = requests.get(f"{entry['doctor_id']}").json()
            entry['doctor_id'] = doctor_data['first_name'] + " " + doctor_data['last_name']

        for data in context['data']:
            appointment = data['id']
            comment = requests.get(f'http://127.0.0.1:8000/api/comments/?appointment_id={appointment}').json()
            for j in range(len(comment)):
                if comment[j]['patient_id'] is None:
                    text = comment[j]['comment_text']
                    data['doctor_com'] = text
                else:
                    text = comment[j]['comment_text']
                    data['patient_com'] = text

        return render(request, 'web_app/patient_history_visits.html', context)
    else:
        context = {
            'data': requests.get(
                f'http://127.0.0.1:8000/api/appointments/?patient_id=&doctor_id=4&date_of_appointment_l={today}&date_of_appointment_g=').json()
        }

        for entry in context['data']:
            patient_data = requests.get(f"{entry['patient_id']}").json()
            entry['patient_id'] = patient_data['first_name'] + " " + patient_data['last_name']

        for data in context['data']:
            appointment = data['id']
            comment = requests.get(f'http://127.0.0.1:8000/api/comments/?appointment_id={appointment}').json()
            for j in range(len(comment)):
                if comment[j]['patient_id'] is None:
                    text = comment[j]['comment_text']
                    data['doctor_com'] = text
                else:
                    text = comment[j]['comment_text']
                    data['patient_com'] = text

        return render(request, 'web_app/doctor_history_visits.html', context)


def get_patients(request):
    context = {
        'data': requests.get('http://127.0.0.1:8000/api/patients/').json()
    }

    for entry in context['data']:
        if entry['gender']:
            entry['gender'] = 'Male'
        else:
            entry['gender'] = 'Female'

    return render(request, 'web_app/doctor_patients_list.html', context)


class MakeReservation(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'web_app/patient_new_appointment.html'

    def form_valid(self, form):
        form.instance.patient_id = Patient(id='3', first_name='Jan', last_name='Kowalski', birthdate='1967-10-15',
                                           gender='True')
        return super().form_valid(form)

    def get_success_url(self):
        return 'http://127.0.0.1:8000/planned_visits/'


class AddComment(CreateView):
    model = Comment
    fields = ('comment_text', 'appointment_id')
    template_name = 'web_app/patient_add_comment.html'

    def form_valid(self, form):
        form.instance.patient_id = Patient(id='3', first_name='Jan', last_name='Kowalski', birthdate='1967-10-15',
                                           gender='True')
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(AddComment, self).get_form(*args, **kwargs)
        form.fields['appointment_id'].queryset = Appointment.objects.filter(patient_id=Patient(id='3', first_name='Jan', last_name='Kowalski', birthdate='1967-10-15',
                                           gender='True'))
        return form

    def get_success_url(self):
        return 'http://127.0.0.1:8000/planned_visits/'


class AddPatient(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'web_app/doctor_add_patient.html'

    def get_success_url(self):
        return 'http://127.0.0.1:8000/patients_list/'


class ScheduleVisit(CreateView):
    model = Appointment
    form_class = VisitForm
    template_name = 'web_app/doctor_new_appointment.html'

    def form_valid(self, form):
        form.instance.doctor_id = Doctor(id='4', first_name='Artur', last_name='Borkowski')
        return super().form_valid(form)

    def get_success_url(self):
        return 'http://127.0.0.1:8000/planned_visits/'


class AddCommentDoc(CreateView):
    model = Comment
    fields = ('comment_text', 'appointment_id')
    template_name = 'web_app/doctor_add_comment.html'

    def form_valid(self, form):
        form.instance.doctor_id = Doctor(id='4', first_name='Artur', last_name='Borkowski')
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(AddCommentDoc, self).get_form(*args, **kwargs)
        form.fields['appointment_id'].queryset = Appointment.objects.filter(doctor_id=Doctor(id='4', first_name='Artur', last_name='Borkowski'))
        return form

    def get_success_url(self):
        return 'http://127.0.0.1:8000/planned_visits/'