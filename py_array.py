import ctypes

class Array:
    
    def __init__(self,size):
        assert size>0 , 'Array size cannot be 0 or less'
        self._size=size
        PyArrayTypes=ctypes.py_object*self._size
        self._elements=PyArrayTypes()
        self.clear(None)
        
    def __len__(self):
        return self._size


    def __getitem__(self, index):
        assert index>=0 and index<(self._size), 'Array index out of range'
        return self._elements[index]

    def __setitem__(self,index,value):
        assert index>=0 and index<self._size ,'Array index out of  range'
        self._elements[index]=value

    def clear(self,value):
        for i in range(self._size):
            self._elements[i]=value
            
    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    
    def __init__(self, theArray):
        self._theArray=theArray
        self._curIndex=0

    def __iter__(self):
        return self

    def next(self):
        if self._curIndex<len(self._theArray):
            entry=self._theArray[self._curIndex]
            self._curIndex+=1
            return entry
        else:
            raise StopIteration
        

    
class Array2D:
    def __init__(self, numRows,numCols):
        self._theArr=Array(numRows)
        for i in range(len(self._theArr)):
            self._theArr[i]=Array(numCols)


    def rows(self):
        return len(self._theArr)


    def cols(self):
        return len(self._theArr[0])

    def __getitem__(self,ndxTuple):
        assert len(ndxTuple)==2, 'invalid numbe of argument passed'
        row=ndxTuple[0]
        col=ndxTuple[1]
        assert row >=0 and row<self.rows(), 'Row is out of index'
        theArr=self._theArr[row]
        assert col>=0 and col<self.cols(),'Col is out of index'
        return theArr[col]

    def __setitem__(self,ndxTuple,value):
        assert len(ndxTuple)==2, 'invalid numbe of argument passed'
        row=ndxTuple[0]
        col=ndxTuple[1]
        assert row >=0 and row<self.rows(), 'Row is out of index'
        theArr=self._theArr[row]
        assert col>=0 and col<self.cols(),'Col is out of index'
        theArr[col]=value


  
    def clear(self,value):
        for i in range(self.rows()):
            theArr=self._theArr[i]
            for j in range(self.cols()):
                theArr[j]=value
                
    def clearx(self,value):
        for i in range(self.rows()):
            theArr=self._theArr[i]
            for j in range(self.cols()):
                theArr[j]=value
                value+=value
    def getMatrix(self):
        
        for i in range(self.rows()):
            
            theArr=self._theArr[i]
            
            for j in range(self.cols()):
                print '%-1s'%(theArr[j])+' ',
            print '\n'
