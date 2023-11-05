from django.db import models
from account.models import User

# Create your models here.
class Character(models.Model):
    # character_id : 자동 생성 (PK)
    character_id = models.AutoField(primary_key=True)
    # 외래키 지정 (User - Character -> 1 : N 관계)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # 캐릭터 이름
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    # 캐릭터 스탯 : 공격력, 방어력, 체력, 민첩성, 지능
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name', 'user_id']
    
    def __str__(self):
        return self.name
    