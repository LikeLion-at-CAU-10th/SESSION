from footprint.models import Footprint
from django.http import JsonResponse
import json


def footprint_GET(request):
    footprints = Footprint.objects.filter(receiver="김영권").order_by('-sent_at')
    messages = []
    for i in range(len(footprints)):
        messages.append(footprints[i].message)

    return JsonResponse({
        'status': 200,
        'message': 'Footprint 조회 성공',
        'data': {
            'messages': messages
        }
    })


def footprint_POST(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Footprint.objects.create(
        message=body['content'], receiver=body['receiverName'])
    
    return JsonResponse({
        'status': 200,
        'message': '메시지 전송 성공'
    })
