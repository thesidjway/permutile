import random

class Tile(object):
	def __init__(self, targetx,targety,curx,cury):
		self.targetx = targetx
		self.targety = targety
		self.curx=curx
		self.cury=cury
	def x(self):
		return self.targetx
	def y(self):
		return self.targety

def printmat():
	for i in range(20,25):
		print abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety),
	print
	for i in range(15,20):
		print abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety),
	print
	for i in range(10,15):
		print abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety),
	print
	for i in range(5,10):
		print abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety),
	print
	for i in range(0,5):
		print abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety),
	print

def countzero():
	cnt=0
	for i in range(25):
		if abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety)==0:
			cnt=cnt+1
	return cnt

def swapnum(x1,y1,x2,y2):
	num1=y1*5+x1
	num2=y2*5+x2
	pos[num1].targetx,pos[num2].targetx=pos[num2].targetx,pos[num1].targetx
	pos[num1].targety,pos[num2].targety=pos[num2].targety,pos[num1].targety

tiles=[]

for i in range(25):
	tiles.append(i)

random.shuffle(tiles)
random.shuffle(tiles)

pos=[]

for i in range(25):
	targy=tiles[i]/5
	targx=tiles[i]%5
	curry=i/5
	currx=i%5
	til=Tile(targx,targy,currx,curry)
	pos.append(til)

print
print


while countzero()!=25:
	printmat()
	a=raw_input("Enter Indices to swap in x1,y1,x2,y2 format: ")
	b=a.split(',')
	for j in range(len(b)):
		b[j]=int(b[j])
	swapnum(b[0],b[1],b[2],b[3])

print "You've Won! Congrats!"

print "Thanks for playing. Siddharth here!"