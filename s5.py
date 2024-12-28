import serial,pynmea2,time
 
port = "/dev/ttyS3"

serialPort = serial.Serial(port, baudrate = 115200, timeout = 0.5)

while True:
    str = serialPort.readline().decode()
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print(round(msg.latitude,8),round(msg.longitude,8),msg.num_sats)