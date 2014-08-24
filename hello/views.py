from django.shortcuts import render
from django.http import HttpResponse
import os
import json

from .models import Greeting
import faceDetection

CASCADE_FILE = 'hello/haarcascade_frontalface_default.xml'

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
        return render(request, 'face.html', {'num_faces': num_faces, 'image_link': image_link})
    elif request.method == 'POST':
        return HttpResponse('yeah..')
    return HttpResponse('test!')

def num_faces(request):
    if request.method == 'GET':
        image_link = request.GET['im']
        num_faces = faceDetection.detectFaces(image_link, CASCADE_FILE)
        return HttpResponse(json.dumps({'num_faces' : num_faces}))
    return HttpResponse('nope')

def are_similar(request):
    if request.method == 'GET':
        image_link1 = request.GET['im1']
        image_link2 = request.GET['im2']
        are_similar = faceDetection.facesAreSimilar(image_link1, image_link2)
        return HttpResponse(json.dumps({'are_similar' : are_similar}))
    return HttpResponse('nope')
