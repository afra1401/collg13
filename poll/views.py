from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
# from django.http import
from .forms import Register
from .models import Student_register
# Create your views here.

def Home(request):
    if request.method == "POST":
        fm = Register(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['fname']
            lname = fm.cleaned_data['lname']
            em = fm.cleaned_data['email']
            pw1 = fm.cleaned_data['password1']
            pw2 = fm.cleaned_data['password2']

            gen = fm.cleaned_data['gender']
            col = fm.cleaned_data['colors']
            data = Student_register(fname=fname, lname=lname, email=em, password1=pw1,password2=pw2,gender=gen, colors=col)


            
            # fname = request.POST['fname']
            # lname = request.POST['lname']
            # em = request.POST['email']
            # pw1 = request.POST['password1']
            # gen = request.POST['gender']
            # col = request.POST['colors']

        
            # print("First Name is :\t", fname)
            # print("Last Name is :\t", lname)
            # print("Email is :\t", em)
            # print("Password is :\t", pw1)
            # print("Gender is :\t", gen)
            # print("Color is :\t", col)
            
            # return redirect("/")
            # return HttpResponseRedirect("/")
            # fm = Register()
            # return HttpResponse("Form submitted successfully !!!!!!".center(100," "))
            return HttpResponseRedirect('/thank/')
    else:
        fm = Register()  
    return render (request, 'home.html', {'form':fm})


def thank(request):
    return render(request, 'thanks.html')