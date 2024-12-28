import serial

gps = serial.Serial('/dev/ttyS3', baudrate=115200)

while True:
    ser_bytes = gps.readline()
    decoded_bytes = ser_bytes.decode("utf-8")
    data = decoded_bytes.split(",")
    if data[0] == '$GNRMC':
        lat_nmea = (data[3],data[4])
        lat_degrees = float(lat_nmea[0][0:2])
        lat_minutes = float(lat_nmea[0][2:])
        lat = lat_degrees + (lat_minutes/60)
        lon_nmea = (data[5],data[6])
        lon_degrees = float(lon_nmea[0][:3])
        lon_minutes = float(lon_nmea[0][3:])
        lon = lon_degrees + (lon_minutes/60)
        if lat_nmea[1] == 'S':
            lat = -lat
        if lon_nmea[1] == 'W':
            lon = -lon
        print("%0.8f" %lat, "%0.8f" %lon)