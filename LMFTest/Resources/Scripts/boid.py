#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
import LMF
import LMFMathLib
import math
import random
import steering
#//\============================================= ENUM
MOVE_SEEK = 0
MOVE_PATH = 1
MOVE_WANDER = 2
#//\============================================= Zombie
class cBoid(steering.cSteering):
	def __init__(self,fx,fy):
		self.Create()
		#//\==== Visual Variables
		self.vPosition.x = fx
		self.vPosition.y = fy
		self.vVelocity = LMFMathLib.Vector2(0.,0.)
		self.vRotationVector = LMFMathLib.Vector2(0.,0.)
		self.iSpeed = 100 + (random.random() * 100)
		self.fRotation = 0.
		self.movement = MOVE_SEEK
		self.path = []
		#//\==== Sprite
		self.SpriteID = LMF.SpriteLoad("./Images/instances/ZombieWalk.png", 44, 30, 22, 15)
		self.animTimer = 0.
		self.UV = [0,0]
		self.UVInc = [0.25,1.]
		LMF.SpriteUVset(self.SpriteID, self.UV[0], self.UV[1], self.UV[0] + self.UVInc[0], self.UV[1] + self.UVInc[1])
	   #//\==== End Of __init__
	def Update(self,fDelta,level,PositionCamera):

		self.NodePosition = list(level.GetPos(3))
		self.tX = int(self.NodePosition[0] * level.GridSize[2])
		self.tY = int(self.NodePosition[1] * level.GridSize[2])
		#//\==== Check where we are looking
		self.nodeID = level.GetID(self.NodePosition[0],self.NodePosition[1])
		self.nodeID = level.GetPosIDFromGridID(self.nodeID)
		if (self.nodeID == 3):
			self.movement = MOVE_PATH
			self.NodePosition = [self.tX,self.tY]
		else:
			self.movement = MOVE_SEEK
			MousePos = LMF.MousePosGet()
			self.NodePosition[0] = (MousePos[0] + PositionCamera[0])
			self.NodePosition[1] = (MousePos[1] + PositionCamera[1])

		if (self.movement == MOVE_SEEK):
			self.Seek(self.NodePosition)
		if (self.movement == MOVE_PATH):
			if (self.path == []):
				self.path = [(self.tX,self.tY)]
			self.Path(fDelta,level,self.path)
		if (self.movement == MOVE_WANDER):
			self.Wander(fDelta,level)
		self.Move(fDelta,level)
		self.Draw(fDelta)
	  #//\==== End Of Update
	def Move(self,fDelta,level):
		#self.Avoid(fDelta,self.iSpeed,level)
		self.animTimer += fDelta
		self.Steering(fDelta,level)
		self.vAhead.Normalise()
		self.vPosition.x += self.vAhead.x * self.iSpeed * fDelta
		self.vPosition.y += self.vAhead.y * self.iSpeed * fDelta
	  #//\==== End Of Move
	def Draw(self,fDelta):
		self.Animate()
		self.Rotate()
		LMF.SpriteRotate(self.SpriteID,self.fRotation)
		LMF.SpriteMove(self.SpriteID,self.vPosition.x,self.vPosition.y,1.)
		LMF.SpriteDraw(self.SpriteID,0)
		#//\==== End Of Draw
	def Rotate(self):
		self.vRotationVector.x = self.vAhead.x
		self.vRotationVector.y = self.vAhead.y
		self.fRotation = self.vRotationVector.Vect2Deg()
		#//\==== End Of Rotate
	def Animate(self):
		if (self.animTimer >= 0.25):
			self.animTimer = 0.
			self.UV[0] += self.UVInc[0]	
			if (self.UV[0] >= 1.0):
				self.UV[0] = 0.0
			LMF.SpriteUVset(self.SpriteID, self.UV[0], self.UV[1], self.UV[0] + self.UVInc[0], self.UV[1] + self.UVInc[1])
		#//\==== End Of Animation
	def SpriteRemove(self):
		LMF.SpriteUnload(self.SpriteID)
		#//\==== Remove Sprites
#//\=============================================EOF