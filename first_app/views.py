from django.shortcuts import render, redirect
from . import models
from first_app.form import StudentForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    else: 
        form = StudentForm()
    student= models.Student.objects.all()
    return render(request,'home.html',{'form':form,'data':student})

def delete_student(request,roll):
    student= models.Student.objects.get(pk=roll).delete()
    return redirect("home")