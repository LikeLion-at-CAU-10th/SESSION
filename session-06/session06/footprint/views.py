from footprint.models import Footprint
from django.http import JsonResponse


def footprint_GET(request):
    footprints = Footprint.objects.filter(receiver="김영권").order_by('-sent_at')
    messages = []
    for i in range(len(footprints)):
        messages.append(footprints[i].message)

    return JsonResponse({
        "status": 200,
        "message": "Footprint 조회 성공",
        "data": {
            "messages": messages
        }
    })


def footprint_POST(request):
    pass
