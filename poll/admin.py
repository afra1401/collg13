from django.contrib import admin
from .models import Student_register

# Register your models here.
@admin.register(Student_register)
class Student_registerAdmin(admin.ModelAdmin):
    list_display = ('id','fname','lname','email','password1','password2','gender','colors')
