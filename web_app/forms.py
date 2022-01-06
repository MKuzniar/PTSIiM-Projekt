from django import forms

from clinic_api.models import Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('date_of_appointment', 'doctor_id')
        widgets = {
            'date_of_appointment': DateInput
        }


class VisitForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('date_of_appointment', 'patient_id')
        widgets = {
            'date_of_appointment': DateInput
        }
