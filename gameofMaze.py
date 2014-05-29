from stack import Stack
from py_array import Array2D
from Linked import LinkedList


class GameOfMaze:

    def __init__(self,row,col):
        self._Matrix=Array2D(row,col)
        self._DirectionStack=Stack()
        self._Divergent=LinkedList()
        self._current=None
        self._previous=None
        self._finish=None
        self._Dict={}


    def seeds(self,List1,List2):
        self._Matrix.clear('x')
        for tup in List1:
            self._Matrix[tup[0],tup[1]]=''
        
        start=List2[0]
        finish=List2[1]

        self._Matrix[start[0],start[1]]='S'
        self._finish=finish
       
        self._Matrix[finish[0],finish[1]]='F'
        self._current=(start[0],start[1])
        print 'Initiating the  game with following configuration:\n'
        self._Matrix.getMatrix()
        


    def gameStart(self):
        self._current=self._start
        
        while self._Dict[self._current]!=0:
            self._Dict[self._current]-=1
            if self._Dict[self._current]!=0:
                self._current=self._DiversionStack.peek()
            else:
                self._current=self._Diversion.pop()
            

        print self._Matrix.getMatrix()
    def getNeighbours(self,tup):
        
        #getting the cordinates with the direction
        count=0
        row=tup[0]
        col=tup[1]
       
        if tup==self._finish:
            self._finish=='Y'
            return
        if (row+1<self._Matrix.rows()):
            if self._Matrix[row+1,col]!='x':
                
                newTup=(row+1,col)
                if self._previous!=newTup:

                    self._DirectionStack.push(('S',newTup))
                    count+=1
        if (row-1>=0):
            if self._Matrix[row-1,col]!='x':
                newTup=(row-1,col)
                if self._previous!=newTup:
                    self._DirectionStack.push(('N',newTup))
                    count+=1
        if (col+1<self._Matrix.cols()):
            if self._Matrix[row,col+1]!='x':
                newTup=(row,col+1)
                if self._previous!=newTup:
                    self._DirectionStack.push(('E',newTup))
                    count+=1
        if (col-1>=0):
            if self._Matrix[row,col-1]!='x':
                newTup=(row,col-1)
                if self._previous!=newTup:
                    self._DirectionStack.push(('W',newTup))
                    count+=1
                    
        self._Dict[tup]=count
        #self.move(tup)
        if count>1:
            print '\n Diversion Point met : '
            self._Divergent.prepend(tup)
        print 'tup in dictionary : ',self._Dict
 

    def _isDivergent(self,tup):
        if tup in self._Divergent:
            return True
        return  False

    def move(self,tup):
        self.getNeighbour(tup)
        while self.isDivergent(tup):
            self._Dict[tup]-=1
            self._previous=self._current
            self._current=self._DirectionStack.pop()
            self._print(self._current)
            tup=self._current
            
            if self._Dict[tup]==0:
                self._Divergent.remove(tup)


    def print (self,tup):
        self._Matrix[tup[0],tup[1]]='#'
            
