from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from computer.models import Computer
from computer_status.models import ComputerStatus
from api.serializers import ComputerSerializer, ComputerStatusSerializer, ComputerEventsSerializer


@csrf_exempt
@api_view(['GET'])
def computer_list(request):
    if request.method == 'GET':
        computers = Computer.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET'])
def computer_status_list(request):
    if request.method == 'GET':
        computers_status = ComputerStatus.objects.all()
        serializer = ComputerStatusSerializer(computers_status, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['POST'])
def save_randon_events(request):
    if request == 'GET':
        return JsonResponse(None, status=403)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComputerEventsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


