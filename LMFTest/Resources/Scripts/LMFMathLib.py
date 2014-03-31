#---------------------------#
#------ Luke Monaghan ------#
#---------------------------#
import math
#//\============================================= DEFINES
PI      = math.pi
RAD2DEG = 57.2957795
DEG2RAD = 0.01745329
#//\============================================= Global Functions
def Rad2Deg(f_Radian):
	return (f_Radian * RAD2DEG)

def Deg2Rad(f_Degree):
	return (f_Degree * DEG2RAD)

def GetAngle(xvec,yvec):
	return (180 - (math.atan2(xvec,yvec) * RAD2DEG))

def Lerp(float_1, float_2, float_T):
	return((float_2 - float_1) * float_T + float_1)

def Magnitude2D(float_x,float_y):
	return (math.sqrt((float_x*float_x)+(float_y*float_y)))

def LineCircle(Vector2Ahead,Vector2Ahead2,fObjRad,Vector2Object):
	if (Vector2Object.Magnitude(Vector2Ahead) <= fObjRad or Vector2Object.Magnitude(Vector2Ahead2) <= fObjRad):
		return True
	return False
def Truncate(vector,maxval):
	i = maxval / vector.Magnitude()
	if (i > 1.0):
		i = 1.0
	else:
		i = 0.
	vector.Scale(i)
#//\============================================= Vector 2
class Vector2():
	def __init__(self , float_x , float_y):
		self.x = float_x
		self.y = float_y

	def Magnitude(self):
		return (math.sqrt((self.x*self.x)+(self.y*self.y)))

	def MagnitudeSquared(self):
		return ((self.x*self.x)+(self.y*self.y))

	def DotProduct(self):
		return (self.x * self.x + self.y * self.y)

	def IsUnit(self):
		return (self.Magnitude() <= 1.0)

	def Normalise(self):
		mag = self.Magnitude()
		if (mag == 0.):
			mag = 1.
		self.x/=mag
		self.y/=mag

	def Deg2Vect(self,f_degree):
		f_degree = Deg2Rad(f_degree)
		self.x = math.cos(f_degree)
		self.y = math.sin(f_degree)
		self.Normalise()

	def Vect2Deg(self):
		return (90 - math.atan2( self.x , self.y ) * RAD2DEG)

	def Project(self,f_angle,f_distance):
		self.x += f_distance * math.cos(f_angle)
		self.y += f_distance * math.cos(f_angle)

	def RotateRad(self,fangle):
		xt = (self.x * math.cos(fangle)) - (self.y * math.sin(fangle))
		yt = (self.x * math.sin(fangle)) + (self.y * math.cos(fangle))
		self.x = xt
		self.y = yt

	def RotateDegree(self,fangle):
		fangle = Deg2Rad(fangle)
		self.RotateRad(fangle)

	def Scale(self,fValue):
		self.x *= fValue
		self.y *= fValue

	def Lerp(self,v2Other,f_t):
		xx = (v2Other.x - self.x)*f_t + self.x
		yy = (v2Other.y - self.y)*f_t + self.y
		self.y = yy
		self.x = xx

	def Zero(self):
		self.x = 0.
		self.y = 0.

	def One(self):
		self.x = 1.
		self.y = 1.

	def Sum(self):
		return (self.x + self.y)

	def Min(self):
		return min(self.x,self.y)

	def Max(self):
		return max(self.x,self.y)

	def Show(self):
		print self.x
		print self.y
	#--------------------------- overloads
	def __add__(self,v2Other):
		xx = self.x + v2Other.x
		yy = self.y + v2Other.y
		return Vector2(xx,yy)

	def __sub__(self,v2Other):
		xx = self.x - v2Other.x
		yy = self.y - v2Other.y
		return Vector2(xx,yy)

	def __div__(self,v2Other):
		xx = self.x / v2Other.x
		yy = self.y / v2Other.y
		return Vector2(xx,yy)

	def __mul__(self,v2Other):
		xx = self.x * v2Other.x
		yy = self.y * v2Other.y
		return Vector2(xx,yy)

	def __iadd__(self,v2Other):
		xx = self.x + v2Other.x
		yy = self.y + v2Other.y
		return Vector2(xx,yy)

	def __isub__(self,v2Other):
		xx = self.x - v2Other.x
		yy = self.y - v2Other.y
		return Vector2(xx,yy)

	def __idiv__(self,v2Other):
		xx = self.x / v2Other.x
		yy = self.y / v2Other.y
		return Vector2(xx,yy)

	def __imul__(self,v2Other):
		xx = self.x * v2Other.x
		yy = self.y * v2Other.y
		return Vector2(xx,yy)
	def __str__(self):
		return "%f %f" % (self.x,self.y)
#//\============================================= Vector 3
class Vector3():
	x = 0.
	y = 0.
	z = 0.

	def __init__(self , float_x , float_y,float_z):
		self.x = float_x
		self.y = float_y
		self.x = float_z

	def Magnitude(self):
		return (math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z)))

	def MagnitudeSquared(self):
		return ((self.x*self.x)+(self.y*self.y)+(self.z*self.z))

	def DotProduct(self,v2Other):
		return (self.x * v2Other.x + self.y * v2Other.y + self.z * v2Other.z)

	def IsUnit(self):
		return (self.Magnitude() <= 1.0)

	def Normalise(self):
		mag = self.Magnitude()
		self.x/=mag
		self.y/=mag
		self.z/=mag

	def Project(self,f_angle,f_distance):
		self.x += f_distance * math.cos(f_angle)
		self.y += f_distance * math.cos(f_angle)
		self.z += f_distance * math.cos(f_angle)

	def Lerp(self,v2Other,f_t):
		xx = (v2Other.x - self.x)*f_t + self.x
		yy = (v2Other.y - self.y)*f_t + self.y
		zz = (v2Other.z - self.z)*f_t + self.z
		self.y = yy
		self.x = xx
		self.x = zz

	def Zero(self):
		self.x = 0.
		self.y = 0.
		self.z = 0.

	def One(self):
		self.x = 1.
		self.y = 1.
		self.z = 1.

	def Sum(self):
		return (self.x + self.y+ self.z)

	def Min(self):
		return min(min(self.x,self.y),self.z)

	def Max(self):
		return max(max(self.x,self.y),self.z)

	def Show(self):
		print self.x
		print self.y
		print self.z
	#--------------------------- overloads
	def __add__(self,v2Other):
		xx = self.x + v2Other.x
		yy = self.y + v2Other.y
		zz = self.z + v2Other.z
		return Vector3(xx,yy,zz)

	def __sub__(self,v2Other):
		xx = self.x - v2Other.x
		yy = self.y - v2Other.y
		zz = self.z - v2Other.z
		return Vector3(xx,yy,zz)

	def __div__(self,v2Other):
		xx = self.x / v2Other.x
		yy = self.y / v2Other.y
		zz = self.z / v2Other.z
		return Vector3(xx,yy,zz)

	def __mul__(self,v2Other):
		xx = self.x * v2Other.x
		yy = self.y * v2Other.y
		zz = self.z * v2Other.z
		return Vector3(xx,yy,zz)

	def __iadd__(self,v2Other):
		xx = self.x + v2Other.x
		yy = self.y + v2Other.y
		zz = self.z + v2Other.z
		return Vector3(xx,yy,zz)

	def __isub__(self,v2Other):
		xx = self.x - v2Other.x
		yy = self.y - v2Other.y
		zz = self.z - v2Other.z
		return Vector3(xx,yy,zz)

	def __idiv__(self,v2Other):
		xx = self.x / v2Other.x
		yy = self.y / v2Other.y
		zz = self.z / v2Other.z
		return Vector3(xx,yy,zz)

	def __imul__(self,v2Other):
		xx = self.x * v2Other.x
		yy = self.y * v2Other.y
		zz = self.z * v2Other.z
		return Vector3(xx,yy,zz)
	def __str__(self):
		return "%f %f %f" % (self.x,self.y,self.z)
#//\============================================= EOF