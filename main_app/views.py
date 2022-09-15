from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *


@api_view(['GET', 'PUT', 'DELETE'])
def client_view(request, pk):
    try:
        client = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if 'tag' in request.data:
            serializer = ClientSerializer(client, data={'id': client.id, 'number': client.number, 'code': client.code, 'tag': request.data['tag']})
        elif 'number' in request.data:
            serializer = ClientSerializer(client, data={'id': client.id, 'number': request.data['number'], 'code': client.code, 'tag': client.tag})
        elif 'code' in request.data:
            serializer = ClientSerializer(client, data={'id': client.id, 'number': client.number, 'code': request.data['code'], 'tag': client.tag})
        elif 'code' in request.data and 'number' in request.data:
            serializer = ClientSerializer(client, data={'id': client.id, 'number': request.data['number'], 'code': request.data['code'], 'tag': client.tag})
        elif 'code' in request.data and 'tag' in request.data:
            serializer = ClientSerializer(client, data={'id': client.id, 'number': client.number, 'code': request.data['code'], 'tag': request.data['tag']})
        elif 'number' in request.data and 'tag' in request.data:
            serializer = ClientSerializer(client, data={'id': client.id, 'number': request.data['number'], 'code': client.code, 'tag': request.data['tag']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        message_lst = MassageList.objects.all()
        serializer = MessageListSerializer(message_lst, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessageListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
