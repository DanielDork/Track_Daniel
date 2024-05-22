
from django.shortcuts import render 

# Create your views here.
from datetime import datetime
from django.http import HttpResponse  

def tracker(request, image, uid):
    client_ip = request.META.get('REMOTE_ADDR', None)

    print(f'''
    ######### Person Tracked #########
    TIME READ: {datetime.now()}
    IMAGE: {image}
    UID: {uid}
    IP ADDRESS: {client_ip}
    ''')

    return HttpResponse(content_type="image/png")
