from django.db import models


class Calc():
    def basic(self, a):
        result = ( (a[0]+a[1])/2 * (1+a[2]/100) * (1+a[3]*a[4]/10000) + a[5] )* a[6]
        # ((무기최소공격력+무기최대공격력)/2) * (1+위력/100) * (1+크확*크뎀/10000) + 고정뎀)
        # * 공격속도
        return round(result,3)