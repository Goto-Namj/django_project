from django.db import models
from django.conf import settings


class Calc():
    def basic(self, a):
        result = ( (a[0]+a[1])/2 * (1+a[2]/100) * (1+a[3]*a[4]/10000) + a[5] )* a[6]
        # ((무기최소공격력+무기최대공격력)/2) * (1+위력/100) * (1+크확*크뎀/10000) + 고정뎀)
        # * 공격속도
        return round(result,3)


class Item(models.Model):
    # name image grade use nature data tag group state state_spc
    # 이미지 등급 사용방식 아이템성격 설명 태그 포함된세트효과 능력치 특수능력치
    # 사용방식 = 양손무기 한손 (주무기) 한손 (보조무기) 액세서리
    # 아이템성격 = 원거리무기 근접무기 액세서리
    # #카타나 #창 #날개 #충전형 #권총 NULL
    # 일반 아이템(하양)  고급 아이템(파랑)  희귀 아이템(노랑)  전설 아이템(분홍)
    # 설명 = "뭐시기"

    name = models.CharField(max_length=30) # 9.16일 기준, 최대 길이가 한글9개 공백 3개 21byte
    image = models.ImageField(upload_to='.\dungreed\static\image\item', max_length=100) # 이미지 파일 로컬 주소..?
    grade = models.CharField(max_length=10) # 일반. 고급. 희귀. 전설.
    use = models.CharField(max_length=20) # 한손 (보조무기) 15byte
    nature = models.CharField(max_length=15) # 원거리무기 10byte (인게임에 없지만 검색을 돕기 위해)
    data = models.TextField()
    tag = models.CharField(max_length=20,blank=True) # #충전형,#카타나 7byte (앞으로 뭐가 나올지 몰라서.)
    group = models.CharField(max_length=25,blank=True) # (set)마나폴리 인형들 15byte (앞으로 뭐가 나올까?)
    state = models.CharField(max_length=25,) # json사용 공격력,공속,방어력,탄창,장전속도
    state_spc = models.CharField(max_length=25) # json사용 오른쪽에 설명되어있음

    def __str__(self):
        return self.name


'''
class Skill(models.Model):
    name = models.CharField(max_length=30)
    name_skill = models.CharField(max_length=30)
    image_skill = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    data_skill = models.TextField()
    cooldown = models.IntegerField() # 후에 쿨탐 소수점 나오면 고칠 아이


class Set(models.Model):
    pass
'''