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
    full_name=forms.CharField(required=False)
    age1 = forms.IntegerField(required=False, min_value=1)
    age2 = forms.IntegerField(required=False, min_value=1)
    course = forms.ChoiceField(widget=forms.RadioSelect, choices = COURSES, required=False)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER, required=False)

class addStudent(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True, min_value=1)
    course = forms.ChoiceField(required=True, widget=forms.Select, choices = COURSES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER)
