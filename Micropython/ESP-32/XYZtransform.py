import math


try:
    xyz = input("Enter xyz coordinates (example: 102 36 74): ")
    coords = [int(tkn) for tkn in xyz.split()]
    coords.append(1)
    print(coords)
    x = coords[0]
    y = coords[1]
    z = coords[2]
    xyproj = (x**2 + y**2)**0.5
    yzproj = (y**2 + z**2)**0.5
    xzproj = (x**2 + z**2)**0.5
    alpha = abs(math.degrees(math.atan(y/x)))
    beta = abs(math.degrees(math.atan(x/y)))
    gamma = abs(math.degrees(math.atan(z/x)))
    print('X:',x)
    print('Y:',y)
    print('Z:',z)
    print('Alpha:',alpha,'Beta:',beta)
    print('xyproj:',xyproj,'yzproj:',yzproj,'xzproj:',xzproj)               
except ValueError:       # if the entered number was of invalid int format
    print('Invalid integer format: {}'.format(tkn))
    raise
