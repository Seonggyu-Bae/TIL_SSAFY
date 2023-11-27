import math

x1, y1 = 76.00, 76.0
x2, y2 = 12.0, 3.0
x3,y3 = 128.0,0.0
ball_radius = 5.76

white = [(x1, y1)]
target = [(x2, y2)]
hole = [(x3,y3)]

dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

a = math.atan(-1)
# atan은 radian으로 줌

b = math.degrees(a)
print(b)

x = x2 - x1
y = y2 - y1
degree = math.degrees(math.atan(y / x))

if x > 0 and y < 0:
    degree = 270 + degree
elif x < 0 and y < 0:
    degree = 180 + degree
elif x < 0 and y > 0:
    degree = 90 + degree


# another

degree = math.atan(x/y) + math.acos(dis+)