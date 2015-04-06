import Base
import dynamic_mission
import VS

def MakePleasureAgriculturalLanding(time_of_day=''):
    room = Base.Room ('Landing_Pad')
    room0 = room
    Base.Texture (room, 'background', 'bases/pleasure/Jolson_LandingBay'+time_of_day+'.spr', 0, 0)
    Base.Texture (room, 'background', 'bases/pleasure/Jolson_LandingBay_wtr'+time_of_day+'.spr', -0.09375, -0.240234375)
    Base.Texture (room, 'background', 'bases/pleasure/Jolson_LandingBay_blt'+time_of_day+'.spr', 0.36875, -0.03515625)
    #Base.Ship (room, 'my_ship', (0.0,-0.25,3.5), (0.05, 0.9915, -0.12), ( -0.9, 0, -0.43406 ))  # original pos/orientation
    # (pos_vec), (up_vec), (nose_vec)
    # OK basic relative size and position of scale 12 Tarsus
    # (180-32.5 degrees yaw anti-clockwise around Y in ./tools/matrix_rotation.py)
    #Base.Ship (room, 'my_ship', (0.04, -0.18, 2.6), (0, 1, 0), (-0.5372996083, 0, -0.8433914458)) 
    # as above but with +1 degree pitch up (anti-clockwise) around X
    Base.Ship (room, 'my_ship', (0.04, -0.18, 2.6), (0.014065, 0.999657, 0.022077), (-0.537115, 0.026177, -0.843102))

    Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.3125, -0.543333, 0.8975, 0.54, 'Launch')
    return room0
