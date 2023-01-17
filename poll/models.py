from django.db import models

# Create your models here.
GENDER = {
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
}
COLORS = {
    (" ", "--SELECT--"),
    ("Red", "RED"),
    ("Green", "GREEN"),
    ("Pink", "PINK"),
    ("Black", "BLACK"),
}
class Student_register(models.Model):
    fname = models.CharField(max_length=20, blank= True,verbose_name="first name",help_text="first name")
    lname = models.CharField(max_length=20, verbose_name="last name", help_text="last name")
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 =models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER)
    colors = models.CharField(max_length=10,choices=COLORS)

