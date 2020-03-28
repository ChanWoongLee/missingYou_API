#views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def animal_list(request):
    if request.method == 'GET':
        query_set = Animal.objects.all()
        serializer = AnimalSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def animal_insert(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


@csrf_exempt
def animal_get(request, pk):
    if request.method == 'GET':
        obj = Animal.objects.filter(animal_name__contains=pk)
        serializer = AnimalSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        obj = Animal.objects.get(pk=pk)
        obj.delete()
        return HttpResponse(status=204)