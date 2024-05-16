from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView,Response
from rest_framework.generics import GenericAPIView
from .serializer import videoSerializer
from .models import video_model
from rest_framework import parsers, renderers
# Create your views here.
class index(GenericAPIView):
    # parser_classes = (MultiPartParser,)
 

    # @swagger_auto_schema(operation_description='Upload file...',)
    # @action(detail=False, methods=['post'])
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class=videoSerializer
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
