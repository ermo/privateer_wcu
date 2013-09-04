import Base
import dynamic_mission
import VS

def MakePleasureAgriculturalLanding(time_of_day=''):
    room = Base.Room ('Landing_Pad')
    room0 = room
    Base.Texture (room, 'background', 'bases/pleasure/Jolson_LandingBay'+time_of_day+'.spr', 0, 0)
    Base.Texture (room, 'background', 'bases/pleasure/Jolson_LandingBay_wtr'+time_of_day+'.spr', -0.09375, -0.240234375)
    Base.Texture (room, 'background', 'bases/pleasure/Jolson_LandingBay_blt'+time_of_day+'.spr', 0.36875, -0.03515625)
    Base.Ship (room, 'my_ship', (0.0,-0.25,3.5), (0.05, 0.9915, -0.12), ( -0.9, 0, -0.43406 ))
    Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.3125, -0.543333, 0.8975, 0.54, 'Launch')
    return room0
