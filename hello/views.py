from django.shortcuts import render
from django.http import HttpResponse

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
        result = faceDetection.detectFaces(image_link , CASCADE_FILE)
        return HttpResponse("Found %d faces" % result)
    elif request.method == 'POST':
        return HttpResponse('yeah..')
    return HttpResponse('test!')
