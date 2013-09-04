import Base
def MakeCommodity(room1,time_of_day='_day'):
    room = Base.Room ('Commodity_Exchange')
    room2 = room
    Base.Texture (room, 'background', 'bases/Commodity.spr', 0, 0)
    Base.Comp (room2, 'my_comp_id', -0.9525, 0.176667, 0.735, 0.79, 'Buy/Sell', 'Cargo')
    Base.Link (room2, 'my_link_id', -0.975, -0.973333, 1.9575, 0.116667, 'Main_Concourse', room1)
    return room2;
