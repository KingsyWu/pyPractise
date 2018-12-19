"""
python 不支持n++ / ++n / --n / n__
"""

a = 1
b = 1
c = ++a + 2
d = b++ + 2
print(a,b,c,d)