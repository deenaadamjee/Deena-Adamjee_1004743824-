class Matrix(object):
    def __init__(self, matrix):
        '''(Matrix, list)-> NoneType
        creates a data attribute elements and instantiate it to the matrix.

        Preconditions: list e contains 2 sublists, all the sublists in e have the same length.

        Complete the instance variable definitions DO NOT CHANGE THE VARIABLE NAMES. Feel free to
        add new ones
        '''
         
        self.elements = matrix
        self.cols = len(matrix[0]) # number of columns
        self.rows = len(matrix) # number of rows
                     
                    
#m = Matrix([[1,2], [3,4]])
#print (m.row1)
      
    def __str__(self):
        '''(Matrix) -> str 
        returns should a string representation of the elements of the matrix. When passed to print() this
        representation result in the original matrix being displayed as follows: each row
        will be displayed on a separate line, with each element in a row separated from the next by
        one, and only one blank space. The string representation should not contain any additional
        blank spaces. Print nothing if the matrix is empty.

        >>> print(Matrix([[1,2], [3,4]]))
        1 2
        3 4
        >>> print(Matrix([[0,-1.5,2.0], [-1, 4.5, 0]]))
        0 -1.5 2.0
        -1 4.5 0 
        >>> print(Matrix([[]]))

        '''
        i_x = '' 
        for i in range(self.rows): 
            for j in range(self.cols):
                i_x = i_x + str(self.elements[i][j]) + ' '
            i_x = i_x.strip()
            i_x += '\n'
        return i_x.strip()
        

    def __repr__(self):
        """Do not change this."""
        return self.__str__()

    def __eq__(self, other):
        ''' (Matrix) -> bool
        #Returns if the self matrix is equal (elementwise) to the other matrix

        #>>> Matrix([[1,1],[1,1]]) == Matrix([[1,1],[1,1]])
        #True
        #>>> Matrix([[1,1],[1,2]]) == Matrix([[1,1],[1,1]])
        #False
        #'''
        
        if self.elements == other.elements: 
            return True 
        else: 
            return False         
        
        
    def add(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Returns the result (as a new Matrix object) of adding the second input Matrix to the first.
        Return an empty matrix if the matrices has mismatching sizes.
        
        >>> Matrix([[1,1],[1,1]]).add(Matrix([[-1,3],[0,0]]))
        0 4
        1 1
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).add(Matrix([[2,-0.5,1],[0,0,0],[0,0,1]]))
        1 2.5 1
        0 0 0
        1.5 1 2
        '''
        add = []
        
        if self.rows == other.rows and self.cols == other.cols:
            for x in range(self.rows): 
                add.append([0]*(self.cols))
            
            for x in range(self.rows): 
                for y in range(self.cols): 
                    add[x][y] = self.elements[x][y] + other.elements[x][y] 
        else: 
            
            add = [[]] 
                
                
        return Matrix(add) 

    def mul(self, k):
        '''(Matrix, Matrix) -> Matrix
        Returns the scalar product of the input matrix with scalar k as a new matrix onject.
        
        >>> Matrix([[1,1],[1,1]]).mul(1)
        1 1
        1 1
        >>> Matrix([[1,3],[-2,-1]]).mul(-1)
        -1 -3
        2 1
        '''
        mult = []
        for x in range(self.rows): 
            mult.append([0]*(self.cols))
            
        for x in range(self.rows): 
            for y in range(self.cols): 
                mult[x][y] = self.elements[x][y] * k 
              
        return Matrix(mult)       

    def sub(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Returns the result (as a new Matrix object) of subtract the second input Matrix to the
        first. Return an empty matrix if the matrices has mismatching sizes.

        >>> Matrix([[1,1],[1,1]]).sub(Matrix([[-1,3],[0,0]]))
        2 -2
        1 1
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).sub(Matrix([[2,-0.5,1],[0,0,0],[0,0,1]]))
        -3 3.5 -1
        0 0 0
        1.5 1 0
        '''
        
        sub = []
        
        if self.rows == other.rows and self.cols == other.cols:
        
            for q in range(self.rows): 
                sub.append([0]*(self.cols))
            
            for q in range(self.rows): 
                for u in range(self.cols): 
                    sub[q][u] = self.elements[q][u] - other.elements[q][u] 
        else: 
            sub = [[]]
              
        
        return Matrix(sub)        

    def trace(self):
        '''(Matrix) -> float
        Returns the trace of the input matrix as a floating point number. If the matrix is not
        square, return float('inf')

        >>> Matrix([[1,1],[2,2]]).trace() 
        3.0 
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).trace()
        0.0
        '''
        trac = []
        
        if self.rows != self.cols: 
            return float('inf')
        else: 
            for r in range(self.rows): 
                trac.append([0]*(self.cols))
            
            for r in range(self.rows): 
                for r in range(self.cols): 
                    trac[r][r] = self.elements[r][r]
        
        trac1 = []
        trac_rows = len(trac) 
        trac_cols = len(trac[0]) 
        for f in range(trac_rows): 
            for g in range(trac_cols):
                trac1.append(trac[f][g])
        
        sum_of_diagonal = float(sum(trac1))
        return sum_of_diagonal
        
        
        

    def transpose(self):
        '''(Matrix) -> Matrix
        Returns the transpose of the input matrix as a new Matrix object.
        
        >>> Matrix([[1,2],[3,4]]).transpose()
        1 3
        2 4
        '''
        trans = []
        for ka in range(self.cols): 
            trans.append([0]*(self.rows))
        
        for ka in range(self.rows): 
            for l in range(self.cols):
                trans[l][ka] += self.elements[ka][l] 

        return Matrix(trans)         
                
                
    def dot(self, other):
        '''(Matrix, Matrix) -> Matrix
        Returns a matrix product between self and other.

        If self and other has mismatching dimension, return an empty Matrix object. If not, return
        the result of self (dot) other

        >>> 
        >>> A.dot(A.transpose()) 
        5 11 17
        11 25 39
        17 39 61
        '''
        self.other = other

        dotp = []
        for dp in range(self.rows): 
            dotp.append([0]*(other.cols))
        
        #dotp1 = []
        for u in range(self.rows):
            #dotp.append([])
            for z in range(other.rows): 
                #dotp[u].append(0)
                for v in range(other.cols):  
                    dotp[u][v] += self.elements[u][z] * other.elements[z][v]
        
        return  Matrix(dotp)