from rest_framework import serializers
from app.models import *
class StudentSM(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'