from django.shortcuts import render
from rest_framework import viewsets
from users.models import Mamamboga, Stakeholder
from .serializers import MamambogaSerializer, StakeholderSerializer


class MamambogaViewSet(viewsets.ModelViewSet):
    queryset = Mamamboga.objects.all()
    serializer_class=MamambogaSerializer

class StakeholderViewSet(viewsets.ModelViewSet):
    queryset = Stakeholder.objects.all()
    serializer_class=StakeholderSerializer



# Create your views here.



from rest_framework import api_view
from rest_framework import Response
from rest_framework import status
from users.models import Mamamboga, Stakeholder
from .serializers import MamambogaSerializer, StakeholderSerializer


# class MamambogaViewSet(viewsets.ModelViewSet):
#     queryset = Mamamboga.objects.all()
#     serializer_class=MamambogaSerializer

# class StakeholderViewSet(viewsets.ModelViewSet):
#     queryset = Stakeholder.objects.all()
#     serializer_class=StakeholderSerializer

@api_view(['GET'])
def get_mamambogas(requests):
    return Response(MamambogaSerializer.object.all())

@api_view(['POST'])
def create_mamambogas(requests):
    serializer = MamambogaSerializer(data=requests.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status)

@api_view(['GET'])
def get_mamambogas(requests):
    return Response(MamambogaSerializer.object.all())




# Create your views here.
