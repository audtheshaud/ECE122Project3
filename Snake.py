from tkinter import *
from Grid import Grid
from Pixel import Pixel
import time


class Snake(Grid):
    def __init__(self, root, obst, fruit):
        '''snake takes fruit and obst that we are randomly placing in the canvas snake has access to grid'''
        super().__init__(root,50,30,20)
        self.fruit = fruit
        super().random_pixels(fruit,3)#making fruit
        super().random_pixels(obst,1)#making obst
        self.snakei = self.nrow//2
        self.snakej = self.ncol//2
        self.snake = [Pixel(self.canvas,self.snakei,self.snakej-3,self.nrow,self.ncol,self.scale,5,vector=[0,1]),Pixel(self.canvas,self.snakei,self.snakej-2,self.nrow,self.ncol,self.scale,5,vector=[0,1]),Pixel(self.canvas,self.snakei,self.snakej-1,self.nrow,self.ncol,self.scale,5,vector=[0,1]),Pixel(self.canvas,self.snakei,self.snakej,self.nrow,self.ncol,self.scale,4,vector=[0,1])]
        self.__gameover = False
        self._pause = False
        
    def pause(self):
         self._pause =  not self._pause
    
    def is_game_over(self):
         return self.__gameover

    def is_pause(self):
         return self._pause

    def next(self):
        '''loop that keeps snake moving when the snake turns it will create a value in the matix that tells the other pixels when to turn'''
        for pixel in self.snake:
            ploc = self.matrix[pixel.i,pixel.j]
            if ploc == -1:
                pixel.right()
            if ploc == -2:
                pixel.up()
            if ploc == -3:
                pixel.left()
            if ploc == -4:
                pixel.down()
            if ploc < 0 and pixel == self.snake[0]:
                self.matrix[pixel.i,pixel.j] = 0 #reseting point
            pixel.next()


        headi,headj = self.snake_head(-1) #point of interest
        if self.matrix[headi,headj] == 3: #eating fruit will del one fruit and add length to snake
            self.fruit = self.fruit-1
            self.delij(headi,headj)

            endi,endj = self.snake_head(0)
            end = self.snake[0].vector
            self.snake.insert(0,Pixel(self.canvas,endi-end[0],endj-end[1],self.nrow,self.ncol,self.scale,5,end))
        if self.matrix[headi,headj] == 1: # if we run into white then the game is over :(
            self.__gameover = True
            print("GAME OVER!")
        if self.fruit == 0: #eat all the fruits win game :)
            self.__gameover = True
            print("YOU WON!")




    def snake_head(self,i):
        return self.snake[i].i,self.snake[i].j

    def right(self):
        if self.snake[-1].vector != [0,1] and self.snake[-1].vector != [0,-1]: #turning conditions cant be going right or left
            self.matrix[self.snake_head(-1)] = -1 #giving matrix the value -1 so we know to turn here


    def up(self):
        if self.snake[-1].vector != [1,0] and self.snake[-1].vector != [-1,0]:
            self.matrix[self.snake_head(-1)] = -2

    def left(self):
        if self.snake[-1].vector != [0,1] and self.snake[-1].vector != [0,-1]:
            self.matrix[self.snake_head(-1)] = -3
        
   
    def down(self):
        if self.snake[-1].vector != [1,0] and self.snake[-1].vector != [-1,0]:
                 self.matrix[self.snake_head(-1)] = -4

    


#########################################################
############# Main code #################################
#########################################################
    

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        python = Snake(root,20,20) #20 obstacles, and 20 fruits
        #python = Snake(root,5,5,25,25,30) # 5 obstacles/fruits, 25 row, 25 column, 30 scale
        
        
        ####### Tkinter binding mouse actions
        root.bind("<Right>",lambda e:python.right())
        root.bind("<Left>",lambda e:python.left())
        root.bind("<Up>",lambda e:python.up())
        root.bind("<Down>",lambda e:python.down())
        root.bind("<p>",lambda e:python.pause())
       
        while True:
            if not python.is_pause(): python.next()
            root.update()
            time.sleep(0.15)  # wait few second (simulation)
            if python.is_game_over(): break
            
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

