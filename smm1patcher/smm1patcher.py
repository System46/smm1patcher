import sys, struct, binascii
from binascii import hexlify, unhexlify

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

main_binary = sys.argv[1]

def change_animation_speed(speed_float):
    global main
    with open(main_binary,'rb') as smm1binary:
            smm1data = smm1binary.read()
            smm1data = bytearray(smm1data)
            speed_float = hex(struct.unpack('<I', struct.pack('<f', speed_float))[0])
            speed_float = bytes.fromhex(str(speed_float).replace("0x",""))
            smm1data[0x8300:0x8304] = speed_float
            with open(main_binary,'wb') as smm1binary:
                smm1binary.write(smm1data)
                print('Successfully Patched ' + str(speed_float) + ' to 0x8300!')
