from django.db import models


class damage(models.Model):
    weapon_damage_min = models.CharField(max_length=3)
    weapon_damage_max = models.CharField(max_length=3)
    power = models.CharField(max_length=3)
    critical_chance = models.CharField(max_length=3)
    critical_damage = models.CharField(max_length=3)
    fix_damage = models.CharField(max_length=2)
    attack_speed = models.CharField(max_length=4)
    