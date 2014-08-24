from django.shortcuts import render
from django.http import HttpResponse
import os

from .models import Greeting
import faceDetection

CASCADE_FILE = 'app/hello/haarcascade_frontalface_default.xml'

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def face(request):
    if request.method == 'GET':
        image_link = request.GET['im']
        num_faces = faceDetection.detectFaces(image_link, CASCADE_FILE)
        return render(request, 'face.html', {'num_faces': num_faces, 'image_link': image_link}
    elif request.method == 'POST':
        return HttpResponse('yeah..')
    return HttpResponse('test!')
