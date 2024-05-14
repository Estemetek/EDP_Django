from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm, addStudent
from .models import Add
from django.db.models import Q
from django.db.models import Value, CharField
from django.db.models.functions import Concat

def home(request):
    if request.method == "POST":
        form = addStudent(request.POST)
        if(form.is_valid()):

            student = Add(
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                course = form.cleaned_data["course"],
                gender = form.cleaned_data["gender"],
                age = form.cleaned_data["age"]
            )

            student.save()
            return redirect("/")
        
    #GET
    context = {}
    context["form"] = addStudent()
    return render(request, "add.html", context)

def filter_table(request):
    students = Add.objects.all() 
    filter_form = StudentForm() 
    context = {}

    if request.method == "POST":
        filter_form = StudentForm(request.POST) 
        if(filter_form.is_valid()):
            name = filter_form.cleaned_data.get('full_name')
            course = filter_form.cleaned_data.get('course')
            gender = filter_form.cleaned_data.get('gender')
            age1 = filter_form.cleaned_data.get('age1')
            age2 = filter_form.cleaned_data.get('age2')

            filters = Q()
            if name:
                filters &= Q(first_name__icontains=name) |  Q(last_name__icontains=name)  | Q(full_name__icontains=name)
            if course:
                filters &= Q(course=course)
            if gender:
                filters &= Q(gender=gender)
            if age1 and age2:
                filters &= Q(age__range=(age1, age2))
            
            students  = students.annotate(full_name=Concat('first_name',Value(' ') ,'last_name',output_field=CharField())).filter(filters)
            # return render(request, 'student_list.html', {'students': students})
    context = {'students': students, 'filter_form': filter_form}  
    return render(request, 'base.html', context)

def delete(request, id):
    stud = Add.objects.get(id=id)
    stud.delete()
    return redirect("/")

def update(request, id):
    context = {}
    stud = Add.objects.get(id=id)

    if request.method == "POST":
        form = addStudent(request.POST)
        if form.is_valid():
            stud.first_name = form.cleaned_data["first_name"]
            stud.last_name = form.cleaned_data["last_name"]
            stud.course = form.cleaned_data["course"]
            stud.gender = form.cleaned_data["gender"]
            stud.age = form.cleaned_data["age"]
            stud.save()
            return redirect("/")
    else:
        form = addStudent(initial={
            'first_name': stud.first_name,
            'last_name': stud.last_name,
            'course': stud.course,
            'gender': stud.gender,
            'age': stud.age
        })
    context["form"] = form
    return render(request, 'add.html', context)
