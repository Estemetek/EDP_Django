from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm, addStudent
from .models import Student
from .models import Add

# Create your views here.
# def create_add_object(form_data):
#     return Add(
#         first_name=form_data["first_name"],
#         last_name=form_data["last_name"],
#         age=form_data["age"],
#         course=form_data["course"],
#         gender=form_data["gender"]
#     )

def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if(form.is_valid()):
            #whole_name = form.cleaned_data["whole_name"]

            student = Student(
                whole_name = form.cleaned_data["whole_name"],
                age = form.cleaned_data["age"],
                course = form.cleaned_data["course"],
                gender = form.cleaned_data["gender"]
            )
            student.save()

            #return HttpResponse(f"Thank you, {whole_name}")
        elif "delete" in request.POST:
            pk = request.POST.get("delete")
            abc = Add.objects.get(id=pk)
            abc.delete()

        # elif "edit" in request.POST:
        #     pk = request.POST.get("edit")
        #     abc = Add.objects.get(id=pk)
        #     form = StudentForm(instance=abc) #has an error
        
    #GET
    context = {}
    context["form"] = StudentForm()
    data = Add.objects.all() #retrieves data
    context["data"] = data #retrieves data
    return render(request, "base.html", context)

def add(request):
    if request.method == "POST":
        form = addStudent(request.POST)
        if(form.is_valid()):
            first_name=form.cleaned_data["first_name"]

            add = Add(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                age=form.cleaned_data["age"],
                course=form.cleaned_data["course"],
                gender=form.cleaned_data["gender"]
            )
            add.save()

            # return HttpResponse(f"Thank you, {first_name}")

    #GET
    context={}
    context["form"] = addStudent()
    return render(request, "add.html", context)