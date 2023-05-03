import serial

from variable import flag_tagetnum, Software_RightLeft_Flag, Machine_RightLeft_Flag, taget_update, Jamming_Number, \
    Jamming_Num, Jamming_Azim, Jamming_Pitch

ser = serial.Serial("COM3", 115200)
ckh = 0
ckl = 0
Send_Num = 0


def autojamming_len(name):
    if (flag_tagetnum == 1):
        write_data("2e")
        write_data("00")
    elif (flag_tagetnum == 2):
        write_data("66")#还不对
        write_data("00")
    print(name)
def BytestoHex(bins):
    return ''.join((["%02X" % x for x in bins])).strip()

def write_data(data1):
    global ckh
    global ckl
    global Send_Num
    ser.write(bytes.fromhex(data1))
    if ((Send_Num%2)==0):
        ckh += int(data1,16)
    else:
        ckl += int(data1,16)
    Send_Num=Send_Num+1
    print(data1,ckh)


head = {'54':autojamming_len}


def lensend(o,name):
    head.get(o)(name)


def autojamming(name):
    write_data("00")
    write_data(Machine_RightLeft_Flag)
    write_data("00")
    write_data("00")
    write_data("00")
    write_data("00")
    write_data("00")
    write_data("00")
    if (flag_tagetnum == 1):
        write_data("01")
        write_data("00")
    elif (flag_tagetnum == 2):
        write_data("02")
        write_data("00")
    if (taget_update[1] == 1):
        write_data("01")
        write_data("00")
    else:
        write_data("00")
        write_data("00")
    write_data(str(Jamming_Number[1]).zfill(2))#编号
    write_data("80")
    write_data(str(Jamming_Num[1]).zfill(2))#批号
    write_data("00")
    print('方位')
    write_data(str(Jamming_Azim[1]).zfill(2))
    write_data("00")
    print('俯仰')
    write_data(str(Jamming_Pitch[1]).zfill(2))
    write_data("00")


    write_data("00")#距离
    write_data("00")
    write_data("00")#速度
    write_data("00")
    write_data("00")#备份
    write_data("00")
    if (flag_tagetnum == 2):

        if (taget_update[2] == 1):
            write_data("01")
            write_data("00")
        else:
            write_data("00")
            write_data("00")
        write_data(Jamming_Number[2])#编号
        write_data("00")
        write_data(Jamming_Num[2])#批号
        write_data("00")
        print('方位')
        write_data(Jamming_Azim[2])
        write_data("00")
        print('俯仰')
        write_data(Jamming_Pitch[2])
        write_data("00")


        write_data("00")#距离
        write_data("00")
        write_data("00")#速度
        write_data("00")
        write_data("00")#备份
        write_data("00")
        print(name)


dataline = {'54': autojamming}


def data(o,name):
    dataline.get(o)(name)


def send_data(order):
    global ckh
    global ckl
    global Send_Num
    write_data("7e")
    write_data("7e")
    lensend(order,54)

    write_data("03")  # 源地址
    write_data("00")  # 源地址
    write_data("21")  # 目的地址
    write_data("00")  # 目的地址
    write_data("01")  # 子包数目
    write_data("00")  # 子包数目
    write_data("01")  # 子包序号
    write_data("00")  # 13子包序号
    if order=='54':
        write_data("54")  # 14数据包编码
    write_data("10")  # 15数据包编码
    data(order,54)

    if ckh>255:
        ckh=ckh-256
        high = str(hex(ckh))[2:]
    else:
        high=str(hex(ckl))[2:]
    if ckl > 255:
        ckl = ckl - 256
        low = str(hex(ckl))[2:]
    else:
        low = str(hex(ckl))[2:]
    write_data(low) # 和校验
    write_data(high)# 和校验
    write_data("0D")  # 帧尾
    write_data("0A")  # 帧尾
    ckh = 0
    ckl = 0
    Send_Num = 0
