#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
import LMF
import LMFMathLib
import math
import random
#//\============================================= Zombie
class cSteering:
	def Create(self):
		self.vPosition = LMFMathLib.Vector2(0.,0.)
		self.vAhead = LMFMathLib.Vector2(0.,0.)

		self.vPathPos = LMFMathLib.Vector2(0.,0.)
		self.vSeek = LMFMathLib.Vector2(0.,0.)
		self.vSteering = LMFMathLib.Vector2(0.,0.)
		self.vAvoidance = LMFMathLib.Vector2(0.,0.)
		self.vWander = LMFMathLib.Vector2(0.,0.)

		self.max_force = 0.4
	   #//\==== End Of Create
	def Seek(self,Position):
		self.vSeek.x = Position[0] - self.vPosition.x
		self.vSeek.y = Position[1] - self.vPosition.y
		self.vAhead.x = self.vSeek.x
		self.vAhead.y = self.vSeek.y
		#//\==== End Of Seek
	def Path(self,fDelta,level,path):
		for Position in path:
			self.vPathPos.x = Position[0] - self.vPosition.x
			self.vPathPos.y = Position[1] - self.vPosition.y
		self.vAhead.x = self.vPathPos.x
		self.vAhead.y = self.vPathPos.y
		#//\==== End Of Path
	def Wander(self,fDelta,level):
		self.vAhead.x = self.vWander.x
		self.vAhead.y = self.vWander.y
		#//\==== End Of Wander
	def Steering(self,fDelta,level):
		self.vSteering.x = self.vAhead.x
		self.vSteering.y = self.vAhead.y
		LMFMathLib.Truncate(self.vSteering,self.max_force)
		self.vAhead += self.vSteering
		#//\==== End Of Steering
	def Avoid(self,fDelta,speed,level):
		self.tX = int((self.vPosition.x + (self.vAhead.x * speed)) / level.GridSize[2])
		self.tY = int((self.vPosition.y + (self.vAhead.y * speed)) / level.GridSize[2])
		#//\==== Check where we are looking
		if (level.CheckGridBounds(self.tX,self.tY)):
			self.nodeID = level.GetID(self.tX,self.tY)
			self.nodeID = level.GetPosIDFromGridID(self.nodeID)
			if (self.nodeID == 1):
				self.vAvoidance.x = self.tX * level.GridSize[2]
				self.vAvoidance.y = self.tY * level.GridSize[2]
				LMF.SpriteMove(7,self.vAvoidance.x,self.vAvoidance.y,1)
				LMF.SpriteDraw(7,0)
		self.vAvoidance.Normalise()
		self.vAhead += self.vAvoidance
		#//\==== End Of Avoid
	def __str__(self):
		string =  "%f %f \n" % (self.vPosition.x,self.vPosition.y)
		string += "%f %f \n" % (self.vPathPos.x,self.vPathPos.y)
		string += "%f %f \n" % (self.vSeek.x,self.vSeek.y)
		string += "%f %f \n" % (self.vAhead.x,self.vAhead.y)
		string += "%f %f \n" % (self.vAhead2.x,self.vAhead2.y)
		string += "%f %f \n" % (self.vSteering.x,self.vSteering.y)
		string += "%f %f \n" % (self.vAvoidance.x,self.vAvoidance.y)
		string += "%f %f \n" % (self.vWander.x,self.vWander.y)
		string += "%f %f \n" % (self.vAhead.x,self.vAhead.y)
		return string
	   #//\==== End Of __str__
#//\=============================================EOF