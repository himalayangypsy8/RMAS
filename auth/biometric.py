from pyfingerprint.pyfingerprint import PyFingerprint

f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

if f.verifyPassword():
    print('Sensor connected')

# Example: enroll a new finger
print('Waiting for finger...')
while not f.readImage():
    pass

f.convertImage(0x01)
result = f.searchTemplate()
positionNumber = result[0]

if positionNumber >= 0:
    print('Finger already exists at position #' + str(positionNumber))
else:
    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger stored at position #' + str(positionNumber))
