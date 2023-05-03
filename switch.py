def jia(x,y):
    print(x+y)
operator={'54':jia}
def f(x,o,y):
    operator.get(o)(x, y)
Jamming_Number=[b'\x7e',0,0]
f(3,'54',2)
print(str(Jamming_Number[0]))