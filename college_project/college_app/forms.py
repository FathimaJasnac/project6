from django import forms
from django.forms import ModelForm
from .models import *


class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course',
                  'purpose', 'materials_provide']
