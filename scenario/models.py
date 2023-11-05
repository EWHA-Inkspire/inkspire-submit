from django.db import models
from account.models import User, Character

# 스크립트
class Script(models.Model):
    # script_id : 자동 생성 (PK)
    script_id = models.AutoField(primary_key=True)
    
    # 외래키 지정 (User - Script -> 1 : N 관계)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # 외래키 지정 (Character - Script -> 1 : N 관계)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    
    # 스크립트 배경
    background = models.CharField(default='', max_length=100, null=False, blank=False)
    # 스크립트 장르
    genre = models.CharField(default='', max_length=50, null=False, blank=False)
    # 마을 이름
    town = models.CharField(default='', max_length=50, null=True)
    # 마을 설명
    town_detail = models.TextField(default='', null=True)
    
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['user_id', 'character_id', 'background', 'genre']
    
    def __str__(self):
        return self.background + ", " + self.genre + ": " + self.town

# 목표
class Goal(models.Model):
    class TypeChoices(models.TextChoices):
        FINAL = 'final', '최종'
        DETAIL = 'detail', '세부'
    
    # goal_id : 자동 생성 (PK)
    goal_id = models.AutoField(primary_key=True)
    
    # 외래키 지정 (Script - Goal -> 1 : N 관계)
    script_id = models.ForeignKey(Script, on_delete=models.CASCADE)
    
    # 목표 타입
    type = models.CharField(choices=TypeChoices.choices, max_length=10, null=False, blank=False)
    # 목표 내용
    content = models.TextField(default='', null=False, blank=False)
    # 목표 달성 여부
    finished = models.BooleanField(default=False)
    
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['script_id', 'type', 'content']
    
    def __str__(self):
        return self.type + " Goal: " + self.content

# gpt response / request
class Gpt(models.Model):
    class RoleChoices(models.TextChoices):
        SYSTEM = 'system', 'system'
        ASSI = 'assistant', 'assi'
        USER = 'user', 'user'
        
    # gpt_id : 자동 생성 (PK)
    gpt_id = models.AutoField(primary_key=True)
    
    # 외래키 지정 (Script - Goal -> 1 : N 관계)
    script_id = models.ForeignKey(Script, on_delete=models.CASCADE)
    
    # 역할
    role = models.CharField(choices=RoleChoices.choices, max_length=10, null=False, blank=False)
    # 쿼리
    query = models.TextField(default='', null=True)
    
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['script_id', 'role']
