import math

ang = float(input('Digite um ângulo em graus: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Sin({0}) = {1:.2f}\nCos({0}) = {2:.2f}\nTan({0}) = {3:.2f}'.
      format(ang, sen, cos, tan))
