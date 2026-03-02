from django.shortcuts import render
from.forms import student_form
from django.http import HttpResponse
from .models import student_model
# Create your views here.

def student(request):
    if request.method=='POST':
        form=student_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("data is saved")
        else:
            return HttpResponse("invalid")
    else:
        form=student_form()
        return render(request,'student.html',{'form':form})

def display(request):
    model=student_model.objects.all()
    obj={
        'model':model
    }
    return render(request,'display.html',obj)