from django import forms
from Student.models import Student
from django.forms import DateInput


class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ("Name", "Class", "Section",
                  "Address", "MobileNo", "Email", "Dob")

        widgets = {
            'Dob': DateInput(attrs={'type': 'date'}),
        }
