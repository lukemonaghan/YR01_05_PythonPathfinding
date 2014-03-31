#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
import LMF
import LMFMathLib
import math
import random
#//\============================================= Enum Pathing Types (sorta)
PATH_NONE = 0
PATH_FINDING = 1 
PATH_WANDERING = 2
#//\============================================= Enum Pathing Types
#//\============================================= Zombie
class cZombie:
	def __init__(self,fx,fy):
		#//\================================= "Init" ==================================/\\#
		#//\==== Visual Variables
		self.fPosition = [fx,fy]
		self.fPositionNew = [1.,1.]
		self.RotationVector = LMFMathLib.Vector2(0.,0.)
		self.NormalVector = LMFMathLib.Vector2(0.,0.)
		self.iSpeed = 100 + (random.random() * 100)
		self.fRotation = 0.
		#//\==== Sprite
		self.SpriteID = LMF.SpriteLoad("./Images/instances/ZombieWalk.png", 44, 30, 22, 15)
		self.animTimer = 0.
		self.UV = [0,0]
		self.UVInc = [0.25,1.]
		LMF.SpriteUVset(self.SpriteID, self.UV[0], self.UV[1], self.UV[0] + self.UVInc[0], self.UV[1] + self.UVInc[1])
		#//\==== Pathing
		self.Pos = (0,0)
		self.ThinkTimer = 0.
		self.pathing = PATH_NONE
		self.ViewDistance = self.iSpeed * 4
		#//\==== Wandering Variables
		self.WanderRad = 16.
		self.WanderDist = 64.
		self.WanderJitter = 10.
		self.WanderTargetPos = LMFMathLib.Vector2(0.,0.)
		self.WanderTarget = LMFMathLib.Vector2(0.,0.)
		self.WanderTimer = 0.
		#//\==== Avoidance
		self.Ahead = LMFMathLib.Vector2(0.,0.)
		self.AvoidanceTarget = LMFMathLib.Vector2(0.,0.)
		self.rotatedeg = 0
		self.tX = 0
		self.tY = 0
		self.nodeID = 0
		#//\==== Debug
		self.endsprite  = LMF.SpriteLoad("./Images/ahead.png", self.WanderRad  ,self.WanderRad  ,self.WanderRad/2,self.WanderRad/2)
		self.line = LMF.SpriteLoad("./Images/line.png", 128,2,1,1)
	   #//\==== End Of __init__
	def Pathing(self,fDelta,level):
		self.Pos = list(level.GetPos(3))
		
		if (self.Pos == [0,0]):
			self.Pos[0] = self.fPosition[0]
			self.Pos[1] = self.fPosition[1]
		else:
			self.Pos[0] = self.Pos[0] * level.GridSize[2]
			self.Pos[1] = self.Pos[1] * level.GridSize[2]
		return (self.Pos[0] ,self.Pos[1])

	def Avoid(self,fDelta,level):
		self.Ahead.x = self.NormalVector.x * self.iSpeed * fDelta
		self.Ahead.y = self.NormalVector.y * self.iSpeed * fDelta

		self.AvoidanceTarget.x = self.Ahead.x - (self.tX * level.GridSize[2])
		self.AvoidanceTarget.y = self.Ahead.y - (self.tY * level.GridSize[2])
		self.AvoidanceTarget.Normalise()
		self.AvoidanceTarget.Scale(level.GridSize[2]*2)

		return (self.fPosition[0] - self.AvoidanceTarget.x,self.fPosition[1] - self.AvoidanceTarget.y)
		#//\==== End Of Avoid
	def Wander(self,fDelta,level):
		self.rotatedeg = 0
		#//\=============================== "Wandering" ==============================/\\#
		self.WanderTarget.x += float(random.uniform(-1,1) * self.WanderJitter)
		self.WanderTarget.y += float(random.uniform(-1,1) * self.WanderJitter)
		self.WanderTarget.Normalise()
		self.WanderTarget.Scale(self.WanderRad)

		self.WanderTargetPos.x = self.WanderTarget.x
		self.WanderTargetPos.y = self.WanderTarget.y - self.WanderDist
		self.WanderTargetPos.RotateDegree(self.fRotation)

		return (self.fPositionNew[0] + (self.fPosition[0] - self.WanderTargetPos.x),self.fPositionNew[1] + (self.fPosition[1] - self.WanderTargetPos.y))
		#//\==== End Of Wander
	def Update(self,fDelta,level,intCamPos):
		#//\=============================== "Update" ================================/\\#
		self.ThinkTimer -= fDelta
		self.animTimer += fDelta
		#//\==== Find the movement Vector
		self.fPositionNew = self.Pathing(fDelta,level)
		self.fPositionNew = self.Wander(fDelta,level)
		#self.fPositionNew = self.Avoid (fDelta,level)
		print self.fPositionNew
		#//\==== Debug Circle
		LMF.SpriteMove(self.endsprite,self.fPositionNew[0],self.fPositionNew[1],45.)
		LMF.SpriteDraw(self.endsprite,0)
		self.Animate()
		#//\==== Rotation from oldXY
		self.Rotate()
		#//\==== Check how close we are to the node
		self.NormalVector.x = self.RotationVector.x
		self.NormalVector.y = self.RotationVector.y
		self.NormalVector.Normalise()
		self.tX = int((self.fPosition[0] + (self.NormalVector.x * self.WanderDist)) / level.GridSize[2])
		self.tY = int((self.fPosition[1] + (self.NormalVector.y * self.WanderDist)) / level.GridSize[2])
		#//\==== Check where we are looking
		if (level.CheckGridBounds(self.tX,self.tY)):
			self.nodeID = level.GetID(self.tX,self.tY)
			self.nodeID = level.GetPosIDFromGridID(self.nodeID)
			if (self.nodeID == 1):
				LMF.SpriteMove(7,self.tX * level.GridSize[2],self.tY * level.GridSize[2],1.)
				LMF.SpriteDraw(7,0)
		#//\==== Update Position
		self.fPosition[0] += self.NormalVector.x * self.iSpeed * fDelta
		self.fPosition[1] += self.NormalVector.y * self.iSpeed * fDelta
		#//\==== Update Sprite
		LMF.SpriteRotate(self.SpriteID,self.fRotation)
		LMF.SpriteMove(self.SpriteID,self.fPosition[0],self.fPosition[1],1.)
		LMF.SpriteDraw(self.SpriteID,0)
	  #//\==== End Of Update
	def Rotate(self):
		self.RotationVector.x = self.fPositionNew[0] - self.fPosition[0]
		self.RotationVector.y = self.fPositionNew[1] - self.fPosition[1]
		self.fRotation = 90 - math.atan2( self.RotationVector.x , self.RotationVector.y ) * LMFMathLib.RAD2DEG
	def Animate(self):
		#//\==== UV Animation
		if (self.animTimer >= 0.25):
			self.animTimer = 0.
			self.UV[0] += self.UVInc[0]	
			if (self.UV[0] >= 1.0):
				self.UV[0] = 0.0
			LMF.SpriteUVset(self.SpriteID, self.UV[0], self.UV[1], self.UV[0] + self.UVInc[0], self.UV[1] + self.UVInc[1])
		#//\==== UV Animation
	def SpriteRemove(self):
		#//\==== Remove Sprites
		LMF.SpriteUnload(self.endsprite)
		LMF.SpriteUnload(self.SpriteID)
		#//\==== Remove Sprites
#//\=============================================EOF