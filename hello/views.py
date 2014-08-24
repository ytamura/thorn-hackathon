from django.shortcuts import render
from django.http import HttpResponse
import os

from .models import Greeting
import faceDetection

CASCADE_FILE = 'haarcascade_frontalface_default.xml'

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
        this_path, this_file = os.path.split(__file__)
        result = faceDetection.detectFaces(image_link, this_path + '/' + CASCADE_FILE)
        return HttpResponse("Found %d faces in %s. Current dir: %s" % (result, image_link, this_path))
    elif request.method == 'POST':
        return HttpResponse('yeah..')
    return HttpResponse('test!')
