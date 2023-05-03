import binascii
my_list = b'\x7e \x7e'
#b=[10,20,30]
#hex_list = [binascii.b2a_hex(bytes([i])) for i in my_list]
print(my_list[1])
str1=my_list.decode('utf-8')
def BytestoHex(bins):
    return ''.join((["%02X" % x for x in bins])).strip()
hex1=BytestoHex(my_list)
a=[hex(x) for x in list(my_list)]
print(hex1)
print(str1)
print(type(hex1))
if (a[0]=="0x7e"):
    print("my_list)")


ckh = 0
ckl = 0





def write_data(data1):
    global ckh
    ckh += data1

write_data(1)