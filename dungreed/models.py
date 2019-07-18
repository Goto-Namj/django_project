from django.db import models


class Calc():
    def basic(self, a):
        return ( (a[0]+a[1])/2 * (1+a[2]/100) * (1+a[3]*a[4]/10000) + a[5] )* a[6]
        
# dps = 
# (무기공격력 *
# (1 + 위력/100) * 
# (1 + 크리티컬 확률*크리티컬 데미지/10000)
# +고정데미지)
# * 공격속도