import re
from PIL import Image,ImageDraw

xmin=float("inf");
xmax=-float("inf");
ymin=float("inf");
ymax=-float("inf");

def setScale(x,y):
	global xmin,xmax,ymin,ymax
	if(x<xmin):
		xmin=x
	if(x>xmax):
		xmax=x
	
	if(y<ymin):
		ymin=y
	if(y>ymax):
		ymax=y

sC=[]
def inputCoordinates():
	a=input()
	b=a.split('; ')
	c=[]
	for i in b:
		d=i.split('/')
		e=re.findall('(\d+|[A-Za-z]+)',d[0])
		f=re.findall('(\d+|[A-Za-z]+)',d[1])
		x=float(e[0])+float(e[1])/60+float(e[2])/3600
		if (e[3] == 'S'):
			x=-x
		y=float(f[0])+float(f[1])/60+float(f[2])/3600
		if (f[3] == 'W'):
			y=-y
		g=(x,y)
		c.append(g)
		setScale(x,y)
	h=(b,c)
	sC.append(h)

while True:
	print('Type Sector Coordinates: ')
	inputCoordinates()
	print('Do you want to add another sector(y/n): ')
	a=input()
	if(a!='y'):
		break

#Generating image with lines

img=Image.new("RGB",size=(1200,2400),color="white")
img1=ImageDraw.Draw(img)

def line(points,m,n):
	x1=points[m][0]
	y1=points[m][1]
	x2=points[n][0]
	y2=points[n][1]
	x1=100 - 1000/(ymax-ymin)*(x1-xmax)
	y1=1100 + 1000/(ymax-ymin)*(y1-ymax)
	x2=100 - 1000/(ymax-ymin)*(x2-xmax)  
	y2=1100 + 1000/(ymax-ymin)*(y2-ymax)
	return [(y1,x1),(y2,x2)]

for i in sC:
	for j in range(len(i[1]) - 1):
		img1.line(line(i[1],j,j+1),fill="black",width=2)
	img1.line(line(i[1],0,len(i[1])-1 ),fill="black",width=2)

img.show()
