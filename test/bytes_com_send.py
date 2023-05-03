import serial

from variable import flag_tagetnum, Software_RightLeft_Flag, Machine_RightLeft_Flag, taget_update, Jamming_Number, \
    Jamming_Num, Jamming_Azim, Jamming_Pitch

ser = serial.Serial("COM3", 115200)
Jamming_Number=[b'\x00',b'01',b'\x00']
a=b'\x01'
b='1'
a=a+Jamming_Number[1]
print(hex(int(b,16)))
ser.write(Jamming_Number[1])
#print(hex(sum([int(i,16) for i in Jamming_Number])))