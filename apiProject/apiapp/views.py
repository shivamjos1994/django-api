from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import ApiModels
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404



# Create your views here.
def index(request):
    if request.method=="POST":
        name= request.POST['name']
        age= request.POST['age']
        email= request.POST['email']
        fm= ApiModels(name=name, age=age, email=email)
        fm.save()
        return render(request, "form.html")
    else:
      return render(request, "form.html")
       
@csrf_exempt # To exempt from default requirement for CSRF tokens to use postman
def api(request):
    if request.method == "GET":
        titles = ApiModels.objects.all()
        # serialize the data into json
        data = serialize('json', titles, fields=('name', 'age', 'email'))
        # turn the json data into dict and send as json response
        return JsonResponse(json.loads(data), safe=False)
    
    if request.method == "POST":
        # turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # create the new item
        newrecord = ApiModels.objects.create(name=body['name'], age=body['age'], email=body['email'])
        # turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serialize('json', [newrecord]))
        # send json response with new object
        return JsonResponse(data, safe=False)


       
@csrf_exempt # To exempt from default requirement for CSRF tokens to use postman
def apiOne(request, id):
    if request.method == "PUT":
        # turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # update the item or raise 404
        item = get_object_or_404(ApiModels, pk=id)
        item.name=body['name'] 
        item.age=body['age']
        item.email=body['email']
        item.save()
        newrecord = ApiModels.objects.get(pk=id)
        data = json.loads(serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)
    
    if request.method == "DELETE":
        item = get_object_or_404(ApiModels, pk=id)
        item.delete()
        newrecord = ApiModels.objects.all()
        data = json.loads(serialize('json', [newrecord], many=True))
        return JsonResponse(data, safe=False)
    
    