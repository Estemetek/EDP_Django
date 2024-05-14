from django import forms
COURSES = (
    ("BS-IT", "Information Technology"),
    ("BS-CS", "Computer Science"),
    ("BS-DS", "Data Science"),
    ("BS-IS", "Information Systems")
)
GENDER = (
    ("F", "Female"),
    ("M", "Male")
)

class StudentForm(forms.Form):
    whole_name=forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    course = forms.ChoiceField(widget=forms.RadioSelect, choices = COURSES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER)

class addStudent(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    course = forms.ChoiceField( choices = COURSES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER)