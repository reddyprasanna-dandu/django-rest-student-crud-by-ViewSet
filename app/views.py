from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.
from app.serializers import *

class StudentCRUDVS(ViewSet):
    def list(self,request):
        QSO=Student.objects.all()
        JD=StudentSM(QSO,many=True)
        return Response(JD.data)
    
    def retrieve(self,request,pk):
        SO=Student.objects.get(pk=pk)
        jD=StudentSM(SO)
        return Response(jD.data)
    
    def create(self,request):
        
        PSO=StudentSM(data=request.data)
        if PSO.is_valid():
            PSO.save()
            return Response({'Success':'Updated Success'})
        else:
            return Response({'Invalid':'Not Updated'})

    
    def update(self,request,pk):
        SO=Student.objects.get(pk=pk)
        USO=StudentSM(SO,data=request.data)
        if USO.is_valid():
            USO.save()
            return Response({'message':'Student is Updated'})
        else:
            return Response({'Failed':'Student is not Updated'})


    def partial_update(self,request,pk):
        SO=Student.objects.get(pk=pk)
        USO=StudentSM(SO,data=request.data,partial=True)
        if USO.is_valid():
            USO.save()
            return Response({'message':'Student is Partially Updated'})
        else:
            return Response({'Failed':'Student is not Updated'})
    
    def destroy(self,request,pk):
        SO=Student.objects.get(pk=pk)
        SO.delete()
        return Response({'message':'studentt Deleted Successfully'})