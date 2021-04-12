from django.shortcuts import render
from django.http import HttpResponse
import redis
from rq import Queue
from tasks import create_image_set

r = redis.Redis()
q = Queue(connection=r)

# Create your views here.
def index(request):
    image_dir = 'C:\\Users\\Admin\\Desktop'
    filename = '1545117208706.jpg'
    q.enqueue(create_image_set, image_dir, filename)

    print("Image resizing", "success")

    return HttpResponse('test')