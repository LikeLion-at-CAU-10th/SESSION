from footprint.models import Footprint  # Footprint 테이블에 대한 ORM을 사용하기 위해 model import
from django.http import JsonResponse    # REST한 JSON 응답을 주기 위한 JsonResponse 함수 Import
import json     # Request-Body로 넘어오는 Json 데이터를 올바르게 디코딩, 파싱해서 사용하기 위한 json 모듈 import


def footprint_GET(request):
    footprints = Footprint.objects.filter(receiver="김영권").order_by('-sent_at')   # DB에서 receiver = '김영권'인 데이터를 조회, sent_at으로 내림차순
    messages = []
    for i in range(len(footprints)):
        messages.append(footprints[i].message)  # footprint[i]는 message 뿐만 아니라, id, sent_at, receiver 등의 값이 포함되어 있으므로 message만 뽑아냄

    return JsonResponse({
        'status': 200,
        'message': 'Footprint 조회 성공',
        'data': {
            'messages': messages
        }
    })


def footprint_POST(request):
    body_unicode = request.body.decode('utf-8')     # Request-Body를 utf-8 방식으로 디코딩 (한국어(receiverName) 디코딩을 위해)
    body = json.loads(body_unicode)     # Json 객체를 파이썬에 알맞은 dict 변수로 변환
    Footprint.objects.create(
        message=body['content'], receiver=body['receiverName']) # DB의 Footprint 테이블에 새로운 footprint 데이터 생성
    
    return JsonResponse({
        'status': 200,
        'message': '메시지 전송 성공'
    })
