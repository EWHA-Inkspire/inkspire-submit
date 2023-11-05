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
    
    def __str(self):
        return self.email
    