#!/usr/bin/env python3

""" Simple vector rotation functions

    This little script was designed for use when aligning ships with the
    landing pads in Privateer: Wing Commander Universe
    using the original Privateer as a visual guide.

    The Vega Strike engine uses a left-handed coordinate system where
    positive X is to the right, positive Y is up and positive Z is into the
    screen. Origo lies on the center of the monitor XY plane.

    The ship model is placed on the screen according to 3 vectors:
    position vector (Vpos), up vector (Vup), nose vector (Vnose).

    The purpose of this script is to take the initial unit vectors

    Vup = positive Y unit vector = (x, y, z) = (0, 1, 0)
      and
    Vnose = positive Z unit vector = (x, y, z) = (0, 0, 1) 

    and transform them using rotations around the X, Y and the Z axis for
    easy input to the Base.Ship(...) statements in the various ./bases/foo.py
    files.

    Rotations are counter-clockwise in a right-handed coordinate system,
    such that RotZ(90, (1,0,0)) returns (0, 1, 0).

    But since Vega Strike uses a left-hand coordinate system, the sign is
    in the rotate function; rotating a negative amount of degrees is the same
    as going from counter-clockwise to clockwise in a right-handed coordinate
    system, and thus from clockwise to counter-clockwise in a left-handed
    coordinate system.

     LH:          RH:

     +Y +Z        +Z  +Y
     | /            \ |
     |/___ +X  +X ___\|
       
    The rotation matrices are applied in the order RotZ*RotY*RotX*vec3.

"""
from math import sin, cos, pi

radians_per_degree = 2 * pi / 360
rpd = radians_per_degree

unitX = (1, 0, 0)
unitY = (0, 1, 0)
unitZ = (0, 0, 1)


def RotZ(rotation, vec3=unitZ):
    """ Rotate vec3 = (x, y, z) rotation degrees anti-clockwise around the Z axis. """

    (x, y, z) = vec3
    x_ = cos(rotation*rpd)*x - sin(rotation*rpd)*y
    y_ = sin(rotation*rpd)*x + cos(rotation*rpd)*y
    z_ = z

    return (x_, y_, z_)


def RotY(rotation, vec3=unitY):
    """ Rotate vec3 = (x, y, z) rotation degrees anti-clockwise around the Y axis. """

    (x, y, z) = vec3
    x_ = cos(rotation*rpd)*x + sin(rotation*rpd)*z
    y_ = y
    z_ = -sin(rotation*rpd)*x + cos(rotation*rpd)*z

    return (x_, y_, z_)


def RotX(rotation, vec3=unitX):
    """ Rotate vec3 = (x, y, z) rotation degrees anti-clockwise around the X axis. """

    (x, y, z) = vec3
    x_ = x
    y_ = cos(rotation*rpd)*y - sin(rotation*rpd)*z
    z_ = sin(rotation*rpd)*y + cos(rotation*rpd)*z

    return (x_, y_, z_)


def round6(f):
    return round(f, 6)


def pack(t3):
    return str(tuple(t3))


def rotate(vec3, pitchX, yawY, rollZ):
    """ Rotate vec3 by pitch(+noseup), yaw(+port) and roll(+starboard)
        
        Returns a vector RotZ*RotY*RotX*vec3 rounded to six digits
        of precision per component.
   
    """
    return pack(map(round6, RotZ(-rollZ, RotY(-yawY, RotX(-pitchX, vec3)))))

def base_rotate(base="default", pitchX=0, yawY=0, rollZ=0):
    """ Return nice rotation strings for use in game files """

    print(
    "base(s): %s\n pitch = %.2f\n yaw   = %.2f\n roll  = %.2f\n Vup   = %s\n Vnose = %s"
        % (base, pitchX, yawY, rollZ, 
        rotate(unitY, pitchX, yawY, rollZ),
        rotate(unitZ, pitchX, yawY, rollZ)))


def test_RotZ():
    print("unitX = %s ?-> %s = unitY" % (str(unitX), str(unitY)))
    print("RotZ(90, unitX) = %s\n" % (pack(map(round, RotZ(90, unitX)))))
    return pack(map(round, RotZ(90, unitX))) == pack(map(round, unitY))


def test_RotY():
    print("unitZ = %s ?-> %s = unitX" % (str(unitZ), str(unitX)))
    print("RotY(90, unitZ) = %s\n" % (pack(map(round, RotY(90, unitZ)))))
    return pack(map(round, RotY(90, unitZ))) == pack(map(round, unitX))


def test_RotX():
    print("unitY = %s ?-> %s = unitZ" % (str(unitY), str(unitZ)))
    print("RotX(90, unitY) = %s\n" % (pack(map(round, RotX(90, unitY)))))
    return pack(map(round, RotX(90, unitY))) == pack(map(round, unitZ))


def run_tests():
    test_RotZ()
    test_RotY()
    test_RotX()


def main():
    base_rotate("mining_base + pleasure_land + pirate",
                pitchX=1, yawY=180-32.5, rollZ=0)
    
if __name__ == "__main__":
    run_tests()
    main()
