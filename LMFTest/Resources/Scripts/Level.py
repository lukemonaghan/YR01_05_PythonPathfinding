#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
import LMF
import KEYDEFS
import LMFMathLib
import random
#//\============================================= Level
class cLevelGrid:
	def __init__ (self,a_gridsize):
		print "Level Loading"
		reload(KEYDEFS)
		reload(LMFMathLib)
		self.MapGrid = []
		self.DoneGrid = []

		self.SpriteStartEnd = [0,0]
		self.SpritePathTiles = [0,0]
		self.canpress = 1

		self.GridSize           = [a_gridsize['width'],a_gridsize['height'],a_gridsize['size'],int(a_gridsize['size']*0.5)]
		self.SpriteTree         = LMF.SpriteLoad("./Images/Floor/Tree.png"  ,self.GridSize[2],self.GridSize[2],self.GridSize[3],self.GridSize[3] )
		self.SpriteGrass        = LMF.SpriteLoad( "./Images/Floor/Floor.png",self.GridSize[2],self.GridSize[2],self.GridSize[3],self.GridSize[3] )
		self.SpriteStartEnd[0]  = LMF.SpriteLoad( "./Images/Floor/Start.png",self.GridSize[2],self.GridSize[2],self.GridSize[3],self.GridSize[3] )
		self.SpriteStartEnd[1]  = LMF.SpriteLoad( "./Images/Floor/End.png"  ,self.GridSize[2],self.GridSize[2],self.GridSize[3],self.GridSize[3] )
		self.SpritePathTiles[0] = LMF.SpriteLoad( "./Images/Grid/Right.png" ,self.GridSize[2],self.GridSize[2],self.GridSize[3],self.GridSize[3] )
		self.SpritePathTiles[1] = LMF.SpriteLoad( "./Images/Grid/Wrong.png" ,self.GridSize[2],self.GridSize[2],self.GridSize[3],self.GridSize[3] )
		ID = 0
		for i in range(0,self.GridSize[0]):
			for j in range(0,self.GridSize[1]):
				if (i == 0 or i == self.GridSize[0]-1):
					self.MapGrid.append(1)
				elif (j == 0 or j == self.GridSize[1]-1):
					self.MapGrid.append(1)
				else:
					self.MapGrid.append(0)
				self.DoneGrid.append(0)
				ID += 1
		print "Level Loaded"

	def Draw(self,PositionCamera):
		ID = 0
		for i in range(0,self.GridSize[0]):
			for j in range(0,self.GridSize[1]):
				if (self.MapGrid[ID] == 0):
					LMF.SpriteMove(self.SpriteGrass,i*self.GridSize[2],j*self.GridSize[2],50.)
					LMF.SpriteDraw(self.SpriteGrass,0)
				if (self.MapGrid[ID] == 1):
					LMF.SpriteMove(self.SpriteTree,i*self.GridSize[2],j*self.GridSize[2],50.)
					LMF.SpriteDraw(self.SpriteTree,0)
				if (self.MapGrid[ID] == 2):
					LMF.SpriteMove(self.SpriteStartEnd[0],i*self.GridSize[2],j*self.GridSize[2],50.)
					LMF.SpriteDraw(self.SpriteStartEnd[0],0)
				if (self.MapGrid[ID] == 3):
					LMF.SpriteMove(self.SpriteStartEnd[1],i*self.GridSize[2],j*self.GridSize[2],50.)
					LMF.SpriteDraw(self.SpriteStartEnd[1],0)
				if (self.DoneGrid[ID] == 1):
					LMF.SpriteMove(self.SpritePathTiles[0],i*self.GridSize[2],j*self.GridSize[2],50.)
					LMF.SpriteDraw(self.SpritePathTiles[0],0)
				if (self.DoneGrid[ID] == 2):
					LMF.SpriteMove(self.SpritePathTiles[1],i*self.GridSize[2],j*self.GridSize[2],50.)
					LMF.SpriteDraw(self.SpritePathTiles[1],0)
				ID += 1
	def Update(self,PositionCamera):
		bShift = LMF.KeyDown(KEYDEFS.KEY_LSHIFT)
		bCtrl = LMF.KeyDown(KEYDEFS.KEY_LCTRL)
		bAlt = LMF.KeyDown(KEYDEFS.KEY_LALT)
		if (LMF.MouseDown(KEYDEFS.MOUSE_BUTTON_LEFT) and self.canpress == 1):
			if (bShift == 0 and bCtrl == 0 and bAlt == 0):
				self.canpress = 0
			ID = 0
			for i in range(0,self.GridSize[0]):
				for j in range(0,self.GridSize[1]):
					if (self.CheckBox(i,j,PositionCamera)):
						if (bAlt):
							LMF.DrawInt(LMF.DefaultFontID(),i,i*self.GridSize[2]-self.GridSize[3],j*self.GridSize[2],0,0)
							LMF.DrawInt(LMF.DefaultFontID(),j,i*self.GridSize[2],j*self.GridSize[2]+self.GridSize[3],0,0)
							return
						if (bShift):
							self.MapGrid[ID] = 1
							return
						if (bCtrl):
							self.MapGrid[ID] = 0
							return
						if (self.MapGrid[ID] == 3):
							self.MapGrid[ID] = 0
							return
						if (self.MapGrid[ID] == 2):
							self.MapGrid[ID] = 3
							return
						if (self.MapGrid[ID] == 1):
							self.MapGrid[ID] = 2
							return
						if (self.MapGrid[ID] == 0):
							self.MapGrid[ID] = 1
							return
					ID += 1  
		if (LMF.MouseUp(KEYDEFS.MOUSE_BUTTON_LEFT)):
			self.canpress = 1
	def Unload(self):
		print "Level unLoading"
		LMF.SpriteUnload(self.SpriteGrass)
		LMF.SpriteUnload(self.SpriteTree)
		LMF.SpriteUnload(self.SpriteStartEnd[0])
		LMF.SpriteUnload(self.SpriteStartEnd[1])
		LMF.SpriteUnload(self.SpritePathTiles[0])
		LMF.SpriteUnload(self.SpritePathTiles[1])
		print "Level unLoaded"

	def PickSpot(self):
		self.ResetGrid(1)
		InstanceID = 1
		while (InstanceID != 0):
			ID = self.GetID(random.randint(1,self.GridSize[0]-1),random.randint(1,self.GridSize[1]-1))
			if (self.MapGrid[ID] == 0):
				self.MapGrid[ID] = 2
				InstanceID = 0
		InstanceID = 1
		while (InstanceID != 0):
			ID = self.GetID(random.randint(1,self.GridSize[0]-1),random.randint(1,self.GridSize[1]-1))
			if (self.MapGrid[ID] == 0):
				self.MapGrid[ID] = 3
				InstanceID = 0
		return 1

	def WanderSpot(self):
		pos = self.GetPos(3)	
		self.ResetGrid(1)
		ID = self.GetID(pos[0],pos[1])
		self.MapGrid[ID] = 2
		InstanceID = 1
		while (InstanceID != 0):
			ID = self.GetID(random.randint(1,self.GridSize[0]-1),random.randint(1,self.GridSize[1]-1))
			if (self.MapGrid[ID] == 0):
				self.MapGrid[ID] = 3
				InstanceID = 0
		return 1
	def CheckWalkable(self,ID):
		if (self.MapGrid[ID] != 1):
			return 1
		return 0

	def CheckBox(self,iI,iJ,PositionCamera):
		MousePos = LMF.MousePosGet()
		xMin = (self.GridSize[2]*iI)-self.GridSize[3]
		xMax = (self.GridSize[2]*iI)+self.GridSize[3]
		yMin = (self.GridSize[2]*iJ)-self.GridSize[3]
		yMax = (self.GridSize[2]*iJ)+self.GridSize[3]
		if (MousePos[0]+PositionCamera[0] < xMax and MousePos[0]+PositionCamera[0] > xMin):
			if (MousePos[1]+PositionCamera[1] < yMax and MousePos[1]+PositionCamera[1] > yMin):
				return 1
		return 0

	def GetPosIDFromGridID(self,a_ID):
		return self.MapGrid[a_ID]
	def GetPos(self,a_ID):
		ID = 0
		for i in range(0,self.GridSize[0]):
			for j in range(0,self.GridSize[1]):
				if (self.MapGrid[ID] == a_ID):
					return (i,j)
				ID += 1
		return (0,0)
	def GetPosList(self,a_ID):
		Poslist = [(0,0)]
		ID = 0
		for i in range(0,self.GridSize[0]):
			for j in range(0,self.GridSize[1]):
				if (self.MapGrid[ID] == a_ID):
					Poslist.append((i,j))
				ID += 1
		return Poslist
	def GetID(self,i_X,i_Y):
		i_Xn = 0
		i_Yn = 0

		if (i_X > 0 and i_Y == 0):
			i_Yn = 0
		else:
			i_Yn = i_Y

		if (i_Y > 0 and i_X == 0):
			i_Xn = self.GridSize[1]
		else:
			i_Xn = i_X * self.GridSize[1]
		return (i_Xn + i_Yn)

	def ResetGrid(self,allordone):
		self.PathList = []
		ID = 0
		for i in range(0,self.GridSize[0]):
			for j in range(0,self.GridSize[1]):
				if (allordone == 0):
					if (i == 0 or i == self.GridSize[0]-1):
						self.MapGrid[ID] = 1
					elif (j == 0 or j == self.GridSize[1]-1):
						self.MapGrid[ID] = 1
					else:
						self.MapGrid[ID] = 0
				if (allordone != 2):
					if (self.MapGrid[ID] == 2 or self.MapGrid[ID] == 3):
						self.MapGrid[ID] = 0
				self.DoneGrid[ID] = 0
				ID += 1
	def CheckGridBounds(self,a_PosX,a_PosY):
		if (a_PosX >= 0 and a_PosX <= self.GridSize[0] and a_PosY >= 0 and a_PosY <= self.GridSize[1]):
			return 1
		return 0
	def CheckLists(self,ID,IDlist):
		for i_id in IDlist:
			if (ID == i_id):
				return 1
		return 0
	def CheckAround(self,CurrentNode,x,y):
		distx = abs(CurrentNode[0]-x)
		disty = abs(CurrentNode[1]-y)
		if (distx <= 1 and disty <= 1):
			return 1
		return 0
#//\============================================= EOF