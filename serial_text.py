import serial

ser = serial.Serial()
ser.baudrate = 9600
#Make sure to change ser.port to your correct port.
ser.port = "COM6"
ser.open()
ser.is_open
data = []
stopper = "E"
#The stopper variable ends the loop and saves everythin before that point to the text file
while 1:
    line = ser.readline()
    new_line = line.decode("utf-8")
    print(new_line)
    if  in new_line:
        break;
    data.append(new_line)
ser.close()

#No need to include the extension
x = input("Name of file: " + ".txt")
f = open(x, "w")
for p in data:
    f.write(p)
f.close()
