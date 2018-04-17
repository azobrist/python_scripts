import serial

def sercom(port="/dev/ttyACM0",baud="115200"):
    ser=serial.Serial(port,baud)

    try:
        ser.open
        print 'Accessing port: ',port
    except:
        print 'Port not open...'

def close(ser):
    ser.close()
