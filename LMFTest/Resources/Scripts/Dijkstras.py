#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
#//\====================== Imports
import KEYDEFS
import LMFMathLib
import operator
#//\====================== Class
class cDijkstras():
	#//\============================================= Init
	def __init__(self):
		print "Loading cDijkstras"
		self.closedset = []
		self.openset = []
		self.pathlist = []
		print "Loaded cDijkstras"
	#//\============================================= Pathing Setup
	def PathSetup(self,level):
		print "cDijkstras Started"
		level.ResetGrid(2)
		#//\====================== Set Node Positions checking they exist
		self.MaxSteps = 1000
		self.StartNode = level.GetPos(2)
		self.EndNode = level.GetPos(3)
		if (self.StartNode == (0,0)):
			print "!!Start Position Not Set!!"
			return 0
		if (self.EndNode == (0,0)):
			print "!!End Position Not Set!!"
			return 0
		#//\====================== reset and add first node to open
		self.closedset = []
		self.openset = []
		self.pathlist = []
		self.openset.append(list(self.StartNode))
		self.pathlist.append(list(self.StartNode))
		#//\====================== setup default scores
		self.stepnum = 0
		return 1
	#//\============================================= Pathing Step
	def Path(self,level):
		#//\====================== Vars
		CheapestNode = [0,0]
		#//\====================== Loop through nodes
		if (len(self.openset) > 0):
			#//\====================== Vars
			self.stepnum += 1
			CurrentNode = self.openset[0]
			#//\====================== Sets
			self.openset.remove(CurrentNode)
			self.closedset.append(CurrentNode)
			#//\====================== cycle through nearby nodes
			for i in range(CurrentNode[0]-1,CurrentNode[0]+2):
				for j in range(CurrentNode[1]-1,CurrentNode[1]+2):
					ID = level.GetID(i,j)
					level.DoneGrid[ID] = 1
					if (level.CheckWalkable(level.GetID(i,j)) and level.CheckGridBounds(i,j)):
						if ((i,j) == self.EndNode):
							self.pathlist.append([i,j])
							return self.Finish(level)
						if (self.CheckList(i,j,self.closedset) == 0):
							level.DoneGrid[ID] = 1
							self.closedset.append((i,j))
							self.openset.append((i,j))
							self.pathlist.append([i,j])
			if (self.stepnum >= self.MaxSteps):
				print "cDijkstras Failed to find node!"
				return 0
		return 1
	#//\============================================= Other Functions
	def Finish(self,level):
		path = self.FixPath(self.pathlist,list(self.EndNode),level)
		for Node in path:
			level.DoneGrid[level.GetID(Node[0],Node[1])] = 2
		print "cDijkstras Finished!"
		return 0
	def CheckList(self,x,y,list):
		for pos in list:
			if (pos[0] == x and pos[1] == y):
				return 1
		return 0
	def FixPath(self,came_from,CurrentNode,level):
		ReturnPath   = []
		PathList     = came_from
		Node         = CurrentNode
		i_fScoreOld  = 99999999
		i_fScore     = 0
		NextNode     = Node
		count = 0
		while (list(Node) != list(self.StartNode)):
			ReturnPath.append(Node)
			i_fScoreOld = 999999
			for i in range(Node[0]-1,Node[0]+2):
				for j in range(Node[1]-1,Node[1]+2):
					i_fScore = self.GetGCost(i,j,Node) + self.GetHCost(i,j,self.StartNode)
					if (level.CheckAround(Node,i,j) and self.CheckList(i,j,PathList) and i_fScore <= i_fScoreOld):
						if (list([i,j]) != Node):
							i_fScoreOld = i_fScore
							NextNode = [i,j]
			try:
				PathList.remove(Node)
			except ValueError:
				return ReturnPath
			Node = NextNode
		return ReturnPath

	def GetGCost(self,i_X,i_Y,i2_CurrentPos):
		if (i_X != i2_CurrentPos[0]):
			if (i_Y != i2_CurrentPos[1]):
				return 14
		return 10
	def GetHCost(self,i_X,i_Y,i2_EndPos):
		ColmAway = abs(i2_EndPos[0] - i_X)
		RowsAway = abs(i2_EndPos[1] - i_Y)
		return (RowsAway + ColmAway) * 10
#//\============================================= EOF