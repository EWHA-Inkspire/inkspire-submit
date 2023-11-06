from django.db import models
from account.models import Character

# 스크립트 모델
class Script(models.Model):
    # script_id : 자동 생성 (PK)
    script_id = models.BigAutoField(primary_key=True)
    
    # 외래키 지정 (Character - Script -> 1 : 1 관계)
    character = models.OneToOneField(Character, related_name="script", on_delete=models.CASCADE, db_column="character_id")
    
    # 스크립트 배경
    background = models.CharField(default='', max_length=100, null=False, blank=False)
    # 스크립트 장르
    genre = models.CharField(default='', max_length=50, null=False, blank=False)
    # 마을 이름
    town = models.CharField(default='', max_length=50, null=True)
    # 마을 설명
    town_detail = models.TextField(default='', null=True)
    
    def __str__(self):
        return self.background + ", " + self.genre + ": " + self.town
