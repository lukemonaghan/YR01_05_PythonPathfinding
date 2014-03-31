#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
import KEYDEFS
import LMFMathLib
import operator
#//\============================================= AStar Class
class cAStar():
	#//\============================================= Init
	def __init__(self):
		print "Loading cAStar"
		self.closedset = []
		self.openset = []
		self.pathlist = []
		print "Loaded cAStar"
	#//\============================================= Pathing Setup
	def PathSetupPos(self,level,x,y):
		print "AStar Started"
		level.ResetGrid(2)
		#//\====================== Set Node Positions checking they exist
		self.MaxSteps = 500
		self.StartNode = (x,y)
		self.EndNode = level.GetPos(3)
		if (self.EndNode == (0,0)):
			print "!!End Position Not Set!!"
			return 0
		#//\====================== reset and add first node to open
		self.closedset = []
		self.openset = []
		self.pathlist = []
		self.openset.append(list(self.StartNode))
		#//\====================== setup default scores
		self.g_Score = 0
		self.stepnum = 0
		return 1
	def PathSetup(self,level):
		print "AStar Started"
		level.ResetGrid(2)
		#//\====================== Set Node Positions checking they exist
		self.MaxSteps = 500
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
		#//\====================== setup default scores
		self.g_Score = 0
		self.stepnum = 0
		return 1
	#//\============================================= Pathing Step
	def Path(self,level):
		#//\====================== Vars
		i_fScore = 999999
		i_fScoreOld = i_fScore
		CheapestNode = [0,0]
		#//\====================== Loop through nodes
		if (len(self.openset) > 0):
			self.stepnum += 1
			CurrentNode = self.openset[0]
			CheapestNode[0] = CurrentNode[0]
			CheapestNode[1] = CurrentNode[1]
			self.openset.remove(CurrentNode)
			self.closedset.append(CurrentNode)
			#//\====================== cycle through nearby nodes
			for i in range(CurrentNode[0]-1,CurrentNode[0]+2):
				for j in range(CurrentNode[1]-1,CurrentNode[1]+2):
					ID = level.GetID(i,j)
					level.DoneGrid[ID] = 1
					if (level.CheckWalkable(level.GetID(i,j)) and level.CheckGridBounds(i,j)):
						g_Score = self.GetGCost(i,j,CurrentNode)
						i_fScore = g_Score + self.GetHCost(i,j,self.EndNode)
						if (self.CheckList(i,j,self.closedset) == 1 and i_fScore >= i_fScoreOld):
							break
						if ((i,j) == self.EndNode):
							self.pathlist.append(CurrentNode)
							self.pathlist.append([i,j])
							return self.Finish(level)
						if (self.CheckList(i,j,self.closedset) == 0 and i_fScore < i_fScoreOld):
							i_fScoreOld = i_fScore
							level.DoneGrid[ID] = 1
							CheapestNode[0] = i
							CheapestNode[1] = j
							self.openset.insert(0,CheapestNode)
			if (CurrentNode != CheapestNode or self.stepnum < self.MaxSteps):
				self.pathlist.append(CurrentNode)
			else:
				print "cDijkstras Failed to find node!"
				return 0
		return 1
	#//\============================================= Other Functions
	def Finish(self,level):
		path = self.FixPath(self.pathlist,list(self.EndNode),level)
		for Node in path:
			level.DoneGrid[level.GetID(Node[0],Node[1])] = 2
		print "AStar Finished!"
		return path
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
			PathList.remove(Node)
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