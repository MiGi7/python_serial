import serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port = "COM6"
ser.open()
ser.is_open
data = []
while 1:
    line = ser.readline()
    new_line = line.decode("utf-8")
    print(new_line)
    if "E" in new_line:
        break;
    data.append(new_line)
ser.close()

x = input("Name of file: ")
f = open(x, "w")
for p in data:
    f.write(p)
f.close()
