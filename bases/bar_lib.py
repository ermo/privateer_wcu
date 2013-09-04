import Base
import VS
import vsrandom

bartenders=['refinery','mining_base','perry','new_detroit','new_constantinople','agricultural']

def MakeBar(concourse, time_of_day, bartext, BaseTexture, createCampaignFixers=True, bar_sprite_320x200=False, defaultbtr=None, forcedefbtr=False, patrons=[],bartenderhead=None):

        
    if vsrandom.random()<.875:
        forcedefbtr=True # remove me if you want random bartenders at random bars
        chbtr=True
    import bartender
    bartender.speaktimes=0
    room0 = Base.Room ('Bar')
    x=0.0
    y=0.0
    if bar_sprite_320x200:
        x=0.0 #0.582
        y=0.0 #-0.2716
    Base.Texture (room0, 'background', BaseTexture+'.spr', x, y)
    for p in patrons:
        if vsrandom.random()<.85:
            Base.Texture(room0,str(p[0]),'bases/bar/'+str(p[0])+'.spr',float(p[1]),float(p[2]))
    if defaultbtr:
        if not forcedefbtr:
            defaultbtr=bartenders[vsrandom.randrange(len(bartenders))]
        Base.Texture(room0,'btr','bases/'+str(defaultbtr)+'/btr.spr', 0.925, -0.259765625) #0.89725, -0.2813)
        if not bartenderhead:
            bartenderhead = defaultbtr
        
    #Base.Texture (room0, 'texture', 'bases/bar/sandoval.spr', -0.43875, -0.373333)
    Base.Link (room0, 'concourse_link',  -0.9225, -0.973333, 1.8275, 0.146667, 'Exit the Bar',concourse)
    script="#\n"
    if bartenderhead:
        import campaign_lib
        if campaign_lib.doTalkingHeads():
            script+="import Base\nimport campaign_lib\ncampaign_lib.AddConversationStoppingSprite('Bartender','bases/heads/"+bartenderhead+".spr',(0,0),(3.2,2.0),'Return_To_Bar').__call__(Base.GetCurRoom(),None)\n"
    Base.Python (room0, 'talk', 0.5875, -0.373333, 0.285, 0.626667,'Talk to the Bartender',script+"import bartender\nbartender.Speak (bartender.GetBartenderText("+repr(bartext)+"))\n",0)
    Base.Python (room0, 'drink', 0.2875, -0.373333, 0.285, 0.326667,'Get a drink         ',script+"import bartender\nbartender.Drink(100)\n",0)
    import fixers
#was:
#   -0.53, -0.673333, 0.205, 0.61
#better:
#   -0.61, -0.86, 0.4105, 1
    func=fixers.CreateFixers
    if not createCampaignFixers:
        func=fixers.CreateMissionFixers
    func(room0,[(-0.80025, -0.9764, 0.776, 1.2416, "_1"),(-0.0725, -0.4058125, 0.1758125, 0.5385, "_2")])#add more locations? 288 844
    #func(room0,[(-0.80025, -1.0088, 0.776, 1.2416, "_1"),(-0.0725, -0.4058125, 0.1758125, 0.5385, "_2")])#add more locations? 288 844
    #func(room0,[(-0.825, -1.04, 0.8, 1.28, "_1"),(-0.0747, -0.418, 0.181, 0.555, "_2")])#add more locations?         280 850
    return room0;
