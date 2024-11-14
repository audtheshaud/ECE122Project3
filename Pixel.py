'''
Group members:
1. Adrian Nelson 33565066
2. Lane Beliveau 33810702
'''



from tkinter import *
import time
import random

class Pixel:
    color=['black','white','yellow','red','blue','green','orange','purple','brown','cyan']

    def __init__(self,canvas,i,j,nrow,ncol,scale,color,vector=[0,0]):
        '''pixel takes 8 arguments the which corisponds to location color and vector (direction)'''
        self.canvas = canvas
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.seti(i)
        self.setj(j)
        self.color = Pixel.color[color]
        self.vector = vector
        self.x = self.scale*self.i
        self.y = self.scale*self.j
        self.rect = self.canvas.create_rectangle(self.y, self.x, self.y + self.scale, self.x + self.scale, fill = self.color)

    def seti(self,i):
            if i>(self.nrow-1):
                i=i%self.nrow
            self.i=i
    
    def setj(self,j):
            if j>(self.ncol-1):
                j=j%self.ncol
            self.j=j

    def __str__(self):
        return f"(({self.i},{self.j}) {self.color})"

    def right(self):
        self.vector = [0,1]#the direction depends on the vector
    def left(self):
        self.vector = [0,-1]
    def up(self):
        self.vector = [-1,0]
    def down(self):
        self.vector = [1,0]

    def next(self):
        '''next is what acualy moves the pixel once it has its vector set'''
        self.canvas.move(self.rect,self.vector[1]*self.scale,self.vector[0]*self.scale)
        self.i = self.i + self.vector[0]
        self.j = self.j + self.vector[1]
        ploc = self.canvas.coords(self.rect)
        #canvas.move(object,x,y) 1. get coords 2. calculate new location with Vector 3. Check location if its in bounds
        #left, top, right and bottom coordinates
        pleft=ploc[0]//self.scale
        ptop=ploc[1]//self.scale
        pbot=ploc[3]//self.scale
        pright=ploc[2]//self.scale
        if pright > self.ncol:
            self.canvas.move(self.rect,(pright - self.ncol - self.ncol)*self.scale,0)
            self.j = 0
        if pbot > self.nrow:
            self.canvas.coords(self.rect,ploc[0],0,ploc[2],self.scale)
            self.i = 0
        if pleft < 0:
            self.canvas.move(self.rect,self.ncol*self.scale,0)
            self.j = self.ncol-1
        if ptop < 0:
            self.canvas.coords(self.rect,ploc[0],(self.nrow*self.scale)-self.scale,ploc[2],self.nrow*self.scale)
            self.i = self.nrow-1

    def delete(self):
        self.canvas.delete(self.rect)

















        
#################################################################
########## TESTING FUNCTION
#################################################################
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")


def test1(canvas,nrow,ncol,scale):
    print("Generate 10 points at random")
    random.seed(4) # for reselfroducibility
    for k in range(10):
        i=random.randint(0,nrow-1) 
        j=random.randint(0,ncol-1)
        c=random.randint(1,9)    # color number
        Pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(Pix)

def test2(canvas,nrow,ncol,scale):
    print("Generate 10 points at random (using modulo)")
    random.seed(5) # for reselfroducibility
    for k in range(10):
        i=random.randint(0,nrow-1)*34
        j=random.randint(0,ncol-1)*13
        ij=str(i)+","+str(j)
        c=random.randint(1,9)    # color number
        Pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(ij,"->",Pix)

        
def test3(root,canvas,nrow,ncol,scale):
    print("Move one point along a square")

    Pix=Pixel(canvas,35,35,nrow,ncol,scale,3)
    Pix.vector=[-1,0] # set up direction (up)
    for i in range(30):
        Pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    Pix.vector=[0,-1] # set up new direction (left)
    for i in range(30):
        Pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    Pix.vector=[1,0]   # set up new direction (down)
    for i in range(30):
        Pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    Pix.vector=[0,1]    # set up new direction (right)
    for i in range(30):
        Pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)

    #delete point
    Pix.delete()


  
def test4(root,canvas,nrow,ncol,scale):
    print("Move four point along a square")

    Pixs=[]
    Pixs.append(Pixel(canvas,35,35,nrow,ncol,scale,3,[-1,0]))
    Pixs.append(Pixel(canvas,5,35,nrow,ncol,scale,4,[0,-1]))
    Pixs.append(Pixel(canvas,5,5,nrow,ncol,scale,5,[1,0]))
    Pixs.append(Pixel(canvas,35,5,nrow,ncol,scale,6,[0,1]))
    
    print("Starting coords")
    for self in Pixs: print(self)

    for i in range(30):
        for self in Pixs:
            self.next()       # next move in the simulation     
        root.update()      # update the graphic
        time.sleep(0.05)   # wait in second (simulation)

    print("Ending coords")
    for self in Pixs:
        print(self)
        self.delete()


        
def test5(root,canvas,nrow,ncol,scale):
    print("Move one point any direction -use arrow commands")

    Pix=Pixel(canvas,20,20,nrow,ncol,scale,2)

    ### binding used by test5
    root.bind("<Right>",lambda e:Pix.right())
    root.bind("<Left>",lambda e:Pix.left())
    root.bind("<Up>",lambda e:Pix.up())
    root.bind("<Down>",lambda e:Pix.down())

    ### simulation
    while True:
        Pix.next()
        root.update()     # update the graphic
        time.sleep(0.05)  # wait in second (simulation)



        

###################################################
#################### Main method ##################
###################################################


def main():
       
        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        nrow=40
        ncol=40
        scale=20
        canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black") # create a canvas width*height
        canvas.pack()

        ### general binding events to choose a testing function
        root.bind("1",lambda e:test1(canvas,nrow,ncol,scale))
        root.bind("2",lambda e:test2(canvas,nrow,ncol,scale))
        root.bind("3",lambda e:test3(root,canvas,nrow,ncol,scale))
        root.bind("4",lambda e:test4(root,canvas,nrow,ncol,scale))
        root.bind("5",lambda e:test5(root,canvas,nrow,ncol,scale))
        root.bind("<d>",lambda e:delete_all(canvas))
        
       
        
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

