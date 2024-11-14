from tkinter import *
from Pixel import Pixel
import numpy as np
import random, time


class Grid:
        color = 'grey'
        def __init__(self,root,nrow,ncol,scale,color='grey'):
                '''grid takes in 5 arguments and is by default grey the goal is to seperate col & row with lines'''
                self.nrow = nrow
                self.ncol = ncol
                self.scale = scale
                self.color = Grid.color
                self.pixels = []
                self.canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black")
                self.canvas.pack()

                self.matrix = np.zeros((nrow,ncol), int)
                for i in range(ncol):
                        self.canvas.create_line(i*scale,0,i*scale,nrow*scale,fill=self.color,width=1)
                for j in range(nrow):
                        self.canvas.create_line(0,j*scale,ncol*scale,j*scale,fill=self.color,width=1)       
                                # self.matrix[i][j] = Pixel(self.canvas, i, j, nrow, ncol, scale, color)
                # we need to make a matrix of pixles and have them all start grey
                # matrix = [[0 for x in range(nrow.length)] for x in range(ncol.length)]
                # for every index in marix we initilize them to grey
                #for i in range(nrow):
                       # for j in range(ncol):
                              #  self.matrix[i][j] = Pixel(self.canvas, i, j, nrow, ncol, scale, color)
        def addij(self,row,col,c):
               '''adding the cords to list pixles so we can graph them'''
               if  c > 0:
                        self.pixels.append(Pixel(self.canvas,row,col,self.nrow,self.ncol,self.scale,c))
                        self.matrix[row,col]=c
                      
                        
                
        def random_pixels(self,npixels,c):
                '''two arguments where we place a pixle at a random point in the grid'''
                for k in range(npixels):
                        i=random.randint(0,self.nrow-1)
                        j=random.randint(0,self.ncol-1)
                        self.addij(i,j,c)
        
        def addxy(self,x,y):
                '''we are finding the row & col the pixle is in then calling the addij function'''
                row = y//self.scale
                col = x//self.scale
                print("insert %s %s %s %s %s"%(x,y,row,col,self.matrix[row,col]))
                if self.matrix[row,col] == 0:
                        self.addij(row,col,1)
                
                

        def delxy(self,x,y):
                '''finding the col & row so we know what pixle we are del also if we use on blank index we call flush row'''
                row = y//self.scale
                col = x//self.scale
                c = self.matrix[row,col]
                print("delete %s %s %s %s %s"%(x,y,row,col,int(self.matrix[row,col])))
                if self.matrix[row,col] == 0:
                         self.flush(row)
                else:         
                        self.delij(row,col)

        def delij(self,row,col):
                        '''called by the delxy takes in location and will take the pixel out of the matrix then calls reset'''
                        c = self.matrix[row,col]
                        if c != 0:
                                self.matrix[row,col] = 0
                                self.reset()

        def reset(self):
            '''reset will del all items in pixles and then adding the pixles in matrix back into pixles'''
            for pixel in self.pixels:
                    pixel.delete()
            self.pixels = []
            for row in range(self.nrow):
                        for col in range(self.ncol):
                                c = self.matrix[row,col]
                                if c > 0:
                                         self.addij(row,col,c)    
                        
        def flush(self,row):
                '''flush will clear the whole row of pixels and has purple pix as graphics'''
                c = 7
                leftpurplepix = [Pixel(self.canvas,row,0,self.nrow,self.ncol,self.scale,c,vector=[0,1]),Pixel(self.canvas,row,1,self.nrow,self.ncol,self.scale,c,vector=[0,1]),Pixel(self.canvas,row,2,self.nrow,self.ncol,self.scale,c,vector=[0,1])]
                rightpurplepix = [Pixel(self.canvas,row,self.ncol-1,self.nrow,self.ncol,self.scale,c,vector=[0,-1]),Pixel(self.canvas,row,self.ncol-2,self.nrow,self.ncol,self.scale,c,vector=[0,-1]),Pixel(self.canvas,row,self.ncol-3,self.nrow,self.ncol,self.scale,c,vector=[0,-1])]
                for i in range(3):
                        self.delij(row,i)
                        self.delij(row,self.ncol-1-i)
                while(True):
                        for pixel in leftpurplepix:
                                pixel.next()
                        for pixel in rightpurplepix:
                                pixel.next()
                        self.delij(row,leftpurplepix[2].j)
                        self.delij(row,rightpurplepix[2].j)
                        self.canvas.update()
                        time.sleep(0.02)
                        if leftpurplepix[2].j == rightpurplepix[2].j-1:
                                break
                for i in range(3):
                        leftpurplepix[i].delete()
                        rightpurplepix[i].delete()
                        self.canvas.update()
                        time.sleep(0.02)
                self.matrix[1:row+1,:]=self.matrix[0:row,:]
                for i in range(self.ncol-1):
                        self.matrix[0,i] = 0
                self.reset()

                
                




#########################################################
############# Main code #################################
#########################################################

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk()                # instantiate a tkinter window
        mesh = Grid(root,50,30,20) # instantiate a Grid object (root,nrow,ncol,scale)
        mesh.random_pixels(25,1) # generate 25 random (white) pixels in the Grid

        
        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:mesh.addxy(e.x,e.y))
        root.bind("<Button-3>",lambda e:mesh.delxy(e.x,e.y))
        

        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

