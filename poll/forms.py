from django import forms
# from django.core import validators
from .models import Student_register

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
#3-validators:
# def color_starts_with(value):
#     if value[0]!='r':
#         raise forms.ValidationError("name sholud not start with r ")
 
# class Register(forms.Form):
#     fname = forms.CharField(label="First Name",validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(6)])
#     lname = forms.CharField(label="Last Name",validators=[validators.MinLengthValidator(6),validators.MaxLengthValidator(8)])
#     email = forms.EmailField(label="Email Adress")
#     password1 = forms.CharField(label="Password",validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(9)])
#     password2 = forms.CharField(label=" Confirm Password",validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(9)])
#     gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER))
#     colors = forms.CharField(widget=forms.SelectMultiple(choices=COLORS))


class Registeration(forms.ModelForm):
    class Meta:
        model = Student_register
        feilds = "__all__"
        # exclude =  ['lname']
        labels= {
            "fname":"user first name",
            "lname": "user last name",
            "email":"user email address",

        }

        error_messages={
            "fname":{"required": "user first name is required"},
            "lname":{"required": "user last name is required"},
            "email":{"required": "user email is required"},
            "password1":{"required": "user password is required"},
            "password2":{"required": "confirm password  is required"},
        }

        help_texts = {
            "fname":"user first name",
            "lname":"user last name",
            "email":"user email address",
        
        }
        widgets={
            "email":forms.EmailInput(),
            "password1":forms.PasswordInput(),
            "password2":forms.PasswordInput(),

        } 


#celaning specfic feild:  
    # def clean_fname(self):
    #     val = self.cleaned_data['fname']
    #     if len(val)<=5:
    #         raise forms.ValidationError("First Name Should Be Greater 5 Characters!!")
    #     return val
    
    # def clean_lname(self):
    #     val = self.cleaned_data['lname']
    #     if len(val)<=4:
    #         raise forms.ValidationError("Last Name Should Be Greater Than Equal TO 8 Characters!!")
    #     elif len(val)>8:
    #         raise forms.ValidationError("Last Name Should Be Less Than Equal 8 Characters!!")
    #     return val
    
    # def clean_email(self):
    #     val = self.cleaned_data['email']
    #     print(val)
    #     l = [".", "com", "@"]
    #     for i in l:
            
    #         if len(val)<=6:
    #             raise forms.ValidationError("First Name Should Be Greater 8 Characters!!")
    #         elif len(val)>8:
    #             raise forms.ValidationError("First Name Should Be Lessr 8 Characters!!")
    #         return val
    
    # def clean_password1(self):
    #     val = self.cleaned_data['password1']
    #     if len(val)<=4:
    #         raise forms.ValidationError("First Name Should Be Greater 8 Characters!!")
    #     elif len(val)>6:
    #         raise forms.ValidationError("First Name Should Be Lessr 8 Characters!!")
    #     return val
    
    # def clean_password2(self):
    #     val = self.cleaned_data['password2']
    #     if len(val)<=4:
    #         raise forms.ValidationError("First Name Should Be Greater 8 Characters!!")
    #     elif len(val)>6:
    #         raise forms.ValidationError("First Name Should Be Lessr 8 Characters!!")
    #     return val
    

#validation of all form at a once:
#     def clean(self):
#         valname = super().clean()
#         nm = self.cleaned_data['fname']
#         if len(nm)<4:
#             raise forms.ValidationError("name should be greater than 4 char")

#         lm =  self.changed_data['lname']
#         if len(lm)<6:
#             raise forms.ValidationError("last name should be greater than 6 char")

#match two password feilds:

#     def clean(self):
#         val = super().clean()
#         pwd1 = self.cleaned_data['password1'] 
#         pwd2 = self.cleaned_data['password2']  

#         if pwd1 !=pwd2:
#             raise forms.ValidationError("password does not match .. please try again!!")


#built-in validation:



