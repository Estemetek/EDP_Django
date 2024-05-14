from django.contrib import admin
from .models import Student
from .models import Add

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    pass