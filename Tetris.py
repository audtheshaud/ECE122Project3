from tkinter import *
from Grid import Grid
from Tetrominoes import Tetrominoes
import numpy as np
import time

class Tetris(Grid):
    def __init__(self,root,nrow,ncol,scale):
            '''tetris class child of grid and uses shapes in tetrominoes'''
            super().__init__(root,nrow,ncol,scale)
            self._pause = False
            self.block = None
            self.__gameover = False
            self._pause = False

    def place(self):
        '''taking the pixles of the pattern saving in the canvas then moves on to another pattern'''
        for (row,col),color in np.ndenumerate(self.block.get_pattern()):    
            self.addij(self.block.i+row,self.block.j+col,color)
        self.block.delete()
        self.block = None                
    
    def next(self):
        '''will take a random tetromino and move it down checking for overlaping, flushing a row and filling all the way to the top'''
        if self.block == None:
            self.block = Tetrominoes.random_select(self.canvas,self.nrow,self.ncol,self.scale)
            self.block.activate() 
        self.block.down()
        if self.block.i == self.nrow-3:
            self.place()
        if self.is_overlapping(self.block.i+1,self.block.j):
            self.place() 
        for row in range(self.nrow):
            if all(self.matrix[row,:]):
                 self.flush(row)
            if row < 3 and any(self.matrix[row,:] != 0):
                 self.__gameover = True
                 print("GAME OVER!")
                 
    
            

    def up(self):
        self.block.rotate()#up key rotates shape
    def down(self):
        while self.block != None:
             self.next()#down will place shape
             
    def left(self):
        if not(self.block.j == 0) or self.is_overlapping(self.block.i,self.block.j-1) == False:#moves left if there is space
            self.block.left()
    def right(self):
        if not(self.block.j == self.ncol-3 or self.is_overlapping(self.block.i,self.block.j+1)):
            self.block.right()
    
    def is_overlapping(self,ii,jj):#will return true if the shapes will overlap
        for (row,col),c in np.ndenumerate(self.block.get_pattern()):
            if c != 0 and self.matrix[row+ii,col+jj] != 0:
                return True
                
     
    def is_pause(self):
         return self._pause
    def pause(self):
         self._pause =  not self._pause
    def is_game_over(self):
         return self.__gameover
    

    

    
def main():
    ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        game=Tetris(root,36,12,25) 
        
        ####### Tkinter binding mouse actions
        root.bind("<Up>",lambda e:game.up())
        root.bind("<Left>",lambda e:game.left())
        root.bind("<Right>",lambda e:game.right())
        root.bind("<Down>",lambda e:game.down())
        root.bind("<p>",lambda e:game.pause())        

        while True:
            if not game.is_pause(): game.next()
            root.update()   # update the graphic
            time.sleep(0.25)  # wait few second (simulation)
            if game.is_game_over(): break
        
        root.mainloop() # wait until the window is closed


        

if __name__=="__main__":
    main()

