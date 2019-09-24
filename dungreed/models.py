from django.db import models
from django.conf import settings


class Calc():
    def basic(self, a):
        result = ( (a[0]+a[1])/2 * (1+a[2]/100) * (1+a[3]*a[4]/10000) + a[5] )* a[6]
        # ((무기최소공격력+무기최대공격력)/2) * (1+위력/100) * (1+크확*크뎀/10000) + 고정뎀)
        # * 공격속도
        return round(result,3)


class Test(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):  
        return self.name

'''
class Item(models.Model):
    name = models.CharField(max_length=30) # 9.16일 기준, 최대 길이가 한글9개 공백 3개 21byte
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) # 이미지 파일 로컬 주소..?
    grade = models.CharField(max_length=10) # 일반. 고급. 희귀. 전설.
    use = models.CharField(max_length=20) # 한손 (보조무기) 15byte
    nature = models.CharField(max_length=15) # 원거리무기 10byte (인게임에 없지만 검색을 돕기 위해)
    data = models.TextField()
    tag = models.CharField(max_length=20) # #충전형,#카타나 7byte (앞으로 뭐가 나올지 몰라서.)
    set = models.CharField(max_length=25) # 마나폴리 인형들 15byte (앞으로 뭐가 나올까?)

class State(models.Model):
    name = models.CharField(max_length=30)
    state_min_damage = models.IntegerField()
    state_max_damage = models.IntegerField()
    state_attack_speed = models.FloatField() # NAN값으로 인한 오류를 DecimalField 로 해결가능.
    state_defense = models.IntegerField()
    state_gun_magazine = models.IntegerField() # 탄창 = 매거진
    state_gun_reload_speed = models.FloatField() # 장전속도 -20% 면 값을 받아서 0.8로 바꿔 저장


class SpecialState(models.Model):
    pass


class Skill(models.Model):
    name = models.CharField(max_length=30)
    name_skill = models.CharField(max_length=30)
    image_skill = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    data_skill = models.TextField()
    cooldown = models.IntegerField() # 후에 쿨탐 소수점 나오면 고칠 아이


class Set(models.Model):
    pass
'''