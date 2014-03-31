#//\=======================/\\#
#//\==== Luke Monaghan ====/\\#
#//\=======================/\\#

#//\============================================= Imports
import LMF
import KEYDEFS
import Level
import AStar
import Dijkstras
import random
import boid
#//\============================================= Local Global Variables CLEAN THIS!
CameraPos = [0.,0.,0.]
PositionInitial = [0.,0.]
GridDimens = [0,0,0]
canpress = [True,True]
LevelGrid = None
ScreenSize = [0,0]
deltatime = 0.
middletimer = 0.
DijkstrasPathing = None
AStarPathing = None
pathing = [0,0]
MousePos = [0,0]
Boids = []
#//\============================================= Program Functions
def Load(iWidth,iHeight):
	#//\==== Load From Application
	print "Loading main"
	#//\==== ReLoad Modules (to make sure they are current when reloading)
	reload(KEYDEFS)
	reload(Level)
	reload(AStar)
	reload(Dijkstras)
	#//\==== Set BG colour and Grid Information
	LMF.FrameworkBGColour(0.1,0.6,0.09,1.)
	global GridDimens
	GridDimens = [40,24,64]
	#//\==== Dijkstras
	global DijkstrasPathing
	DijkstrasPathing = Dijkstras.cDijkstras()
	global AStarPathing
	AStarPathing = AStar.cAStar()
	#//\==== Setup ScreenSize
	global ScreenSize
	ScreenSize[0] = iWidth
	ScreenSize[1] = iHeight
	global Boids
	Boids = []
	Boids.append(boid.cBoid(CameraPos[0]+iWidth *0.5,CameraPos[1]+iHeight *0.5))
	#//\==== Setup the Tile able Level
	global LevelGrid
	LevelGrid = Level.cLevelGrid({'width':GridDimens[0], 'height':GridDimens[1] , 'size':GridDimens[2] })
	#//\==== center the view on the middle of the Grid and update the AIE camera
	CameraPos[0] = -(iWidth *0.5) + ((GridDimens[0]*GridDimens[2])*0.5 ) - (GridDimens[2]*0.5)
	CameraPos[1] =  (iHeight*0.5) + ((GridDimens[1]*GridDimens[2])*0.5 ) - (GridDimens[2]*0.5)
	LMF.CameraMove(-CameraPos[0],-CameraPos[1])
	print "Loaded main"
  #//\==== End of Load From Application
def Update():
	#//\==== Update
	global MousePos
	MousePos = LMF.MousePosGet()
	#//\==== DeltaTime Setting
	global deltatime
	deltatime = LMF.DeltaTimeGet()
	#//\==== LevelGrid Update
	global LevelGrid
	global CameraPos
	LevelGrid.Draw(CameraPos)
	LevelGrid.Update(CameraPos)
	MoveCamera()
	#//\==== Boids
	global Boids
	for boidin in Boids:
		boidin.Update(deltatime,LevelGrid,CameraPos)
	#//\==== Pathing	
	global DijkstrasPathing
	global AStarPathing
	global pathing
	UpdatePathing(15)
	global canpress
	if (LMF.MousePressed(KEYDEFS.MOUSE_BUTTON_RIGHT) and canpress[0]):
		canpress[0] = False
		Posx = 0
		Posy = 0
		#//\==== Pathing
		if (LMF.KeyDown(KEYDEFS.KEY_LALT)):
			print "starting DijkstrasPathing"
			pathing[0] = DijkstrasPathing.PathSetup(LevelGrid)
			pathing[1] = 1
		elif (LMF.KeyDown(KEYDEFS.KEY_LCTRL)):
			print "starting AStarPathing"
			pathing[0] = AStarPathing.PathSetup(LevelGrid)
			pathing[1] = 0
		else:
			Boids.append(boid.cBoid(CameraPos[0]+MousePos[0]+1,CameraPos[1]+MousePos[1]+1))
	if (LMF.MouseReleased(KEYDEFS.MOUSE_BUTTON_RIGHT)):
		canpress[0] = True
	#//\==== Show Help
	if (LMF.KeyDown(KEYDEFS.KEY_F1)):
		ShowHelp()
  #//\==== End of Update
def Unload():
	#//\==== Unload
	print "Unloading!"
	global LevelGrid
	LevelGrid.Unload()
	LMF.CameraMove(0,0)#reset to 0,0
	print "Unloaded!"
  #//\==== End of Unload
#//\============================================= Local Functions
def UpdatePathing(count):
	i = 0
	while (i < count):
		i += 1
		if (pathing[0] == 1):
			if (pathing[1]):
				pathing[0] = DijkstrasPathing.Path(LevelGrid)
			else:
				pathing[0] = AStarPathing.Path(LevelGrid)
	#//\==== UpdatePathingEND
def PassVariable(value):
	#//\==== PassVariable
	global AStarOrDijkstras
	global pathing
	pathing = 0
	AStarOrDijkstras = value
  #//\==== End of PassVariable
def ShowHelp():
	#//\==== ShowHelp
	global CameraPos
	intCamPos = [int(CameraPos[0]),int(CameraPos[1])]
	LMF.DrawString(LMF.DefaultFontID(),"F1 is help."                                     ,intCamPos[0],intCamPos[1],0,0)
	LMF.DrawString(LMF.DefaultFontID(),"F5 to reload main script."                       ,intCamPos[0],intCamPos[1]-24,0,0)
	LMF.DrawString(LMF.DefaultFontID(),"ESC to clear console window."                    ,intCamPos[0],intCamPos[1]-48,0,0)
	LMF.DrawString(LMF.DefaultFontID(),"Left click to change tile under mouse"           ,intCamPos[0],intCamPos[1]-96,0,0)
	LMF.DrawString(LMF.DefaultFontID(),"Left click + left Shift to multichange to trees" ,intCamPos[0],intCamPos[1]-120,0,0)
	LMF.DrawString(LMF.DefaultFontID(),"Left click + left Ctrl to multichange to grass"  ,intCamPos[0],intCamPos[1]-144,0,0)
	LMF.DrawString(LMF.DefaultFontID(),"middle click to move view"                       ,intCamPos[0],intCamPos[1]-192,0,0)
	LMF.DrawString(LMF.DefaultFontID(),"Right click to Add an NPC at Mouse"              ,intCamPos[0],intCamPos[1]-224,0,0)
  #//\==== End of ShowHelp
def MoveCamera():
	#//\==== MoveCamera
	global CameraPos
	global canpress
	global PositionInitial
	global deltatime
	global middletimer
	global MousePos
	if (middletimer > 0.):
		middletimer -= deltatime
	if (LMF.MousePressed(KEYDEFS.MOUSE_BUTTON_MIDDLE)):
		if (middletimer <= 0.):
			middletimer = 0.4
		elif (LMF.MousePressed(KEYDEFS.MOUSE_BUTTON_MIDDLE)):
			global ScreenSize
			global GridDimens
			CameraPos[0] = -(ScreenSize[0]*0.5) + ((GridDimens[0]*GridDimens[2])*0.5 ) - GridDimens[2]*0.5
			CameraPos[1] =  (ScreenSize[1]*0.5) + ((GridDimens[1]*GridDimens[2])*0.5 ) - GridDimens[2]*0.5
		if (canpress[1] == True):
			PositionInitial[0] = CameraPos[0] + MousePos[0]
			PositionInitial[1] = CameraPos[1] + MousePos[1]
			canpress[1] = False
		CameraPos[0] = (PositionInitial[0] - MousePos[0])
		CameraPos[1] = (PositionInitial[1] - MousePos[1])
		LMF.CameraMove(-CameraPos[0],-CameraPos[1])
	else:
		canpress[1] = True
  #//\==== End of MoveCamera
#//\============================================= EOF