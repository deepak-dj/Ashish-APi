import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerialzer
from .forms import StudentForm


# API
class Students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


#  django app

def home(request):
    return render(request, 'home.html', {'text': 'Welcome home'})


def create_student(request):
    if request.method == 'POST':
        data = StudentForm(request.POST).data

        print('data = ################ = ', data)
        api_url = request.build_absolute_uri('/')[:-1]
        response = requests.post(f'{api_url}/students/', data=data)
        print('response = **************** =', response)
        if response.status_code == 201:
            return redirect('get_all')
        else:
            return HttpResponse('bad request')
    else:
        form = StudentForm()
        return render(request, 'create.html', {'form': form})


def get_all_student(request):
    api_url = request.build_absolute_uri('/')[:-1]
    response = requests.get(f'{api_url}/students')
    if response.status_code == 200:
        context = {'data': json.loads(response.text)}
        return render(request, 'get_all.html', context)

    else:
        return HttpResponse('no data found')


def update_student(request, id):
    api_url = request.build_absolute_uri('/')[:-1]
    get_response = requests.get(f'{api_url}/students/{id}/')
    obj = Student.objects.get(id=id)
    print('response =========', get_response)
    # text_data = json.loads(get_response.text)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj).data
        print('form ===== ', form)
        response = requests.put(f'{api_url}/students/{id}/', form)
        print('response======= ', response)
        if response.status_code == 200:
            return redirect('get_all')
        else:
            HttpResponse('invalid id')
    else:
        form = StudentForm(instance=obj)
        return render(request, 'update.html', {'form': form})


def delete_student(request, id):
    api_url = request.build_absolute_uri('/')[:-1]
    response = requests.delete(f'{api_url}/students/{id}/')

    if response.status_code == 204:
        return HttpResponse('data deleted')
    else:
        return HttpResponse('data not available to delete')
