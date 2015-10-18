import random
from gi.repository import Gtk
swapx1=0
swapx2=0
swapy1=0
swapy2=0
numofswaps=0
state=1
labtext=[]


class Handler:
	def call1(self, button1):
		global state,swapx1,swapx2
		global swapy1,swapy2
		if state==1:
			swapx1=0
			swapy1=0
			global state
			state=0
		elif state==0:
			swapx2=0
			swapy2=0
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call2(self, button2):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=1
			swapy1=0
			global state
			state=0
		elif state==0:
			swapx2=1
			swapy2=0
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call3(self, button3):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=2
			swapy1=0
			global state
			state=0
		elif state==0:
			swapx2=2
			swapy2=0
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call4(self, button4):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=3
			swapy1=0
			global state
			state=0
		elif state==0:
			swapx2=3
			swapy2=0
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call5(self, button5):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=4
			swapy1=0
			global state
			state=0
		elif state==0:
			swapx2=4
			swapy2=0
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call6(self, button6):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=0
			swapy1=1
			global state
			state=0
		elif state==0:
			swapx2=0
			swapy2=1
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call7(self, button7):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=1
			swapy1=1
			global state
			state=0
		elif state==0:
			swapx2=1
			swapy2=1
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call8(self, button8):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=2
			swapy1=1
			global state
			state=0
		elif state==0:
			swapx2=2
			swapy2=1
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call9(self, button9):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=3
			swapy1=1
			global state
			state=0
		elif state==0:
			swapx2=3
			swapy2=1
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call10(self, button10):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=4
			swapy1=1
			global state
			state=0
		elif state==0:
			swapx2=4
			swapy2=1
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call11(self, button11):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=0
			swapy1=2
			global state
			state=0
		elif state==0:
			swapx2=0
			swapy2=2
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call12(self, button12):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=1
			swapy1=2
			global state
			state=0
		elif state==0:
			swapx2=1
			swapy2=2
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call13(self, button13):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=2
			swapy1=2
			global state
			state=0
		elif state==0:
			swapx2=2
			swapy2=2
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call14(self, button14):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=3
			swapy1=2
			global state
			state=0
		elif state==0:
			swapx2=3
			swapy2=2
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call15(self, button15):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=4
			swapy1=2
			global state
			state=0
		elif state==0:
			swapx2=4
			swapy2=2
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call16(self, button16):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=0
			swapy1=3
			global state
			state=0
		elif state==0:
			swapx2=0
			swapy2=3
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call17(self, button17):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=1
			swapy1=3
			global state
			state=0
		elif state==0:
			swapx2=1
			swapy2=3
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call18(self, button18):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=2
			swapy1=3
			global state
			state=0
		elif state==0:
			swapx2=2
			swapy2=3
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call19(self, button19):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=3
			swapy1=3
			global state
			state=0
		elif state==0:
			swapx2=3
			swapy2=3
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call20(self, button20):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=4
			swapy1=3
			global state
			state=0
		elif state==0:
			swapx2=4
			swapy2=3
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call21(self, button21):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=0
			swapy1=4
			global state
			state=0
		elif state==0:
			swapx2=0
			swapy2=4
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call22(self, button22):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=1
			swapy1=4
			global state
			state=0
		elif state==0:
			swapx2=1
			swapy2=4
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call23(self, button23):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=2
			swapy1=4
			global state
			state=0
		elif state==0:
			swapx2=2
			swapy2=4
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call24(self, button24):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=3
			swapy1=4
			global state
			state=0
		elif state==0:
			swapx2=3
			swapy2=4
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1
	def call25(self, button25):
		global state,swapx1,swapx2,swapy1,swapy2
		if state==1:
			swapx1=4
			swapy1=4
			global state
			state=0
		elif state==0:
			swapx2=4
			swapy2=4
			swapnum(swapx1,swapy1,swapx2,swapy2)
			setval()
			changelabel()
			global state
			state=1

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
	global numofswaps
	print str(numofswaps)+" swaps"
	numofswaps+=1
	labtext[num1],labtext[num2]=labtext[num2],labtext[num1]

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


builder = Gtk.Builder()
builder.add_from_file("permutile.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
label1=builder.get_object("label1")
label2=builder.get_object("label2")
label3=builder.get_object("label3")
label4=builder.get_object("label4")
label5=builder.get_object("label5")
label6=builder.get_object("label6")
label7=builder.get_object("label7")
label8=builder.get_object("label8")
label9=builder.get_object("label9")
label10=builder.get_object("label10")
label11=builder.get_object("label11")
label12=builder.get_object("label12")
label13=builder.get_object("label13")
label14=builder.get_object("label14")
label15=builder.get_object("label15")
label16=builder.get_object("label16")
label17=builder.get_object("label17")
label18=builder.get_object("label18")
label19=builder.get_object("label19")
label20=builder.get_object("label20")
label21=builder.get_object("label21")
label22=builder.get_object("label22")
label23=builder.get_object("label23")
label24=builder.get_object("label24")
label25=builder.get_object("label25")
button1=builder.get_object("button1")
button2=builder.get_object("button2")
button3=builder.get_object("button3")
button4=builder.get_object("button4")
button5=builder.get_object("button5")
button6=builder.get_object("button6")
button7=builder.get_object("button7")
button8=builder.get_object("button8")
button9=builder.get_object("button9")
button10=builder.get_object("button10")
button11=builder.get_object("button11")
button12=builder.get_object("button12")
button13=builder.get_object("button13")
button14=builder.get_object("button14")
button15=builder.get_object("button15")
button16=builder.get_object("button16")
button17=builder.get_object("button17")
button18=builder.get_object("button18")
button19=builder.get_object("button19")
button20=builder.get_object("button20")
button21=builder.get_object("button21")
button22=builder.get_object("button22")
button23=builder.get_object("button23")
button24=builder.get_object("button24")
button25=builder.get_object("button25")

def initializer():
	for i in range(25):
		labtext.append(0)
def setval():
	for i in range(25):
		labtext[i]=(abs(pos[i].curx-pos[i].targetx)+abs(pos[i].cury-pos[i].targety))

def changelabel():
	label1.set_text(str(labtext[0]))
	label2.set_text(str(labtext[1]))
	label3.set_text(str(labtext[2]))
	label4.set_text(str(labtext[3]))
	label5.set_text(str(labtext[4]))
	label6.set_text(str(labtext[5]))
	label7.set_text(str(labtext[6]))
	label8.set_text(str(labtext[7]))
	label9.set_text(str(labtext[8]))
	label10.set_text(str(labtext[9]))
	label11.set_text(str(labtext[10]))
	label12.set_text(str(labtext[11]))
	label13.set_text(str(labtext[12]))
	label14.set_text(str(labtext[13]))
	label15.set_text(str(labtext[14]))
	label16.set_text(str(labtext[15]))
	label17.set_text(str(labtext[16]))
	label18.set_text(str(labtext[17]))
	label19.set_text(str(labtext[18]))
	label20.set_text(str(labtext[19]))
	label21.set_text(str(labtext[20]))
	label22.set_text(str(labtext[21]))
	label23.set_text(str(labtext[22]))
	label24.set_text(str(labtext[23]))
	label25.set_text(str(labtext[24]))

initializer()
setval()
changelabel()
window.show_all()

Gtk.main()




