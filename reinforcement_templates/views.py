from django.http import HttpResponse
from django.shortcuts import render

def new_profile(request):
    list = ["email", "username", "pin", "website", "address", "alias"]
    context = {'field_items': list}
    return HttpResponse(render(request, 'profiles/new.html', context))
