from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView,Response
from .serializer import videoSerializer
from .models import video_model
# Create your views here.
class index(APIView):
    def post(self,request):
        serializer=videoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'done'})
        return Response(serializer.errors)
    def get(self,request):
        data =video_model.objects.all()
        serializer=videoSerializer(data,many=True)
        return Response(serializer.data)