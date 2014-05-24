import sys
from py_array import Array2D


if float(sys.version[:3])>3:
    print 'Must be executed with python 2.7 or below'
    sys.exit()

class GameOfLife:


    def __init__(self,rows,cols):
        self.object_gol=Array2D(rows,cols) #A 2D Array to hold the initial structure
        self.object_gol.clear('')
        self.List=[]
       
        
        self.neighbourDict={}
        self.inactiveList=[]
        self.alive=[]
        self.inactiveDict={}
        
    def seeds(self,listValue):
        #print 'Inside seeds!'
        assert len(listValue)>0,' Can\'t start a game with no seeds!'
        
        for tup in listValue:
            self.List.append(tup)
            self.object_gol[tup[0],tup[1]]='x'
        
        
        self.object_gol.getMatrix()


    def nextGenCheck(self):
        
        for tup in self.List:
            self.neighbourDict[tup]=self.getNeighbours(tup)
            
        for key in self.neighbourDict:
            
            count=self.getActiveCount(self.neighbourDict[key])
            if count in (2,3):
                
                self.alive.append(key)
        
        
        for tup in self.inactiveList:
            self.inactiveDict[tup]=self.getNeighbours(tup)
            
            
        for key in self.inactiveDict:
            
            count=self.getActiveCount(self.inactiveDict[key])
            if count==3:
                
                self.alive.append(key)

        self.List=[]
        """
        for values in self.alive:
            self.List.append(values)
        self.alive=[]
        """
        self.object_gol.clear('')
        self.seeds(self.alive)
        
        self.alive=[]
        self.neighbourDict={}
        self.inactiveList=[]
        self.alive=[]
        self.inactiveDict={}

    def getNeighbours(self,tup):
        

        getNeighbour=[]
        
        if tup[0]+1<self.object_gol.rows():
            getNeighbour.append((tup[0]+1,tup[1]))
            
            if tup[1]+1<self.object_gol.cols():
                getNeighbour.append((tup[0]+1,tup[1]+1))
                
            if tup[1]-1>=0:
                getNeighbour.append((tup[0]+1,tup[1]-1))
                
        if tup[0]-1>=0:
            getNeighbour.append((tup[0]-1,tup[1]))
            
            if tup[1]+1<self.object_gol.cols():
                getNeighbour.append((tup[0]-1,tup[1]+1))
                
            if tup[1]-1>=0:
                getNeighbour.append((tup[0]-1,tup[1]-1))
                
        #calculation for col neighbours!
        if tup[1]+1<self.object_gol.cols():
            getNeighbour.append((tup[0],tup[1]+1))
        if tup[1]-1>=0:
            getNeighbour.append((tup[0],tup[1]-1))
        
        

        return getNeighbour
    

    
    def getActiveCount(self,List):

        ActiveCount=0

        for vals in List:
            if self.object_gol[vals[0],vals[1]]=='x':
                ActiveCount+=1
            else:
                self.inactiveList.append(vals)

        return ActiveCount
