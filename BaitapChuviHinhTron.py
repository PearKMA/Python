import math
try:
    r = float(input('Mời bạn nhập bán kính: '))
    cv = 2*math.pi*r
    dt = math.pi*r**2
    print('Chu vi hình tròn là: cv= ',cv)
    print('Diện tích hình tròn là: dt= ',dt)
except:
    print('float dạng #.# bạn ei!')