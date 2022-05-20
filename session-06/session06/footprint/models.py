from django.db import models


class Footprint(models.Model):
    footprint_id = models.AutoField(primary_key=True)       # AutoField로 설정해서 footprint_id는 자동으로 1씩 증가된 값이 부여됩니다
    receiver = models.TextField(null=False)                 # receiver는 텍스트입니다
    message = models.TextField(null=False)                  # message는 텍스트입니다
    sent_at = models.DateTimeField(auto_now_add=True, blank=True)   # 메시지 전송 시각은, 자동으로 데이터가 생성된 시간으로 값을 부여합니다
