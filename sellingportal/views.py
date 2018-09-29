
from django.http import HttpResponse
from django.shortcuts import render
from sellingportal import models
from sellingportal import form


# Create your views here.
def index(request):
    names = ['ahmed', 'ali', 'audy']
    return render(request, 'index.html', {'names': names})



def student(request):
    students = models.Student.objects.all()
    context = {'students': students}

    return render(request, 'students.html', context)


def studentDegree(request, student_id):
    degrees = models.Degree.objects.filter(student_id=student_id)
    stuents = models.Student.objects.get(id=student_id)
    form_data = form.DegreeRegistrar(request.POST or None)
    msg = ''
    if form_data.is_valid():
        degree = models.Degree()
        degree.student_degree = form_data.cleaned_data['student_drgee']
        degree.student_id = stuents
        degree.save()
        msg = 'data is saved'
    context = {
        'degrees': degrees,
        'formregister': form_data,
        'msg': msg

    }
    return render(request, 'degree.html', context)

def Register(request):
    form_data = form.UserRegistrar(request.POST or None)
    msg = ''

    if form_data.is_valid():
        student = models.Student()
        student.first_name = form_data.cleaned_data['first_name']
        student.last_name = form_data.cleaned_data['last_name']
        student.age = form_data.cleaned_data['age']
        student.data_bith = form_data.cleaned_data['data_bith']
        student.save()
        msg = 'data is saved'
    context = {
        'formregister': form_data,
        'msg': msg
      }
    return render(request, 'regiester.html', context)





