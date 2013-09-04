import Base

def MakeMilitia(room1, time_of_day=''):
    room = Base.Room ('Militia_Guild_Office')
    room3 = room
    Base.Texture (room, 'background', 'bases/Heimdall/milgui.spr', 0, 0)
    Base.Python (room3, 'talk_militia', -0.85, 0.2, 0.3, 0.3, 'ComLink_to_Militia_Officer', 'bases/militia_talk.py',0)
    Base.Link (room3, 'my_room_id', 0.65, 0.1, 0.3, 0.6, 'Leave', room1)
    return room3;
