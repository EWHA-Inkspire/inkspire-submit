from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# AbstractBaseUser : id, password, last_login 필드
class UserManager(BaseUserManager):
    # 일반 user
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 user
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email,
            password=password,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
# 회원 정보
class User(AbstractBaseUser):
    # user_id : 자동 생성 (PK)
    user_id = models.AutoField(primary_key=True)
    email=models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname=models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()
    
    # 사용자의 username field 닉네임으로 설정
    USERNAME_FIELD = 'nickname'
    
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.nickname

# 캐릭터 정보
class Character(models.Model):
    # character_id : 자동 생성 (PK)
    character_id = models.AutoField(primary_key=True)
    
    # 외래키 지정 (User - Character -> 1 : N 관계)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    
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
