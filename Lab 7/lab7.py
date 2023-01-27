def Kseq(start, stop, step):
    """ (int,int,int) -> list of integers

    Input: This function is passed start (>= 0), stop (>start), and step (>= 1) values that define a sequence of numbers.
    Output: This function returns a list of the corresponding K sequence.

    >>>Kseq(0,6,1)
    [2, 1, 9, 100, 11881, 143544361]
    >>>Kseq(2,6,2)
    [9, 11881]
    """
    
    
     
    def K_int(n):
        if n == 0: 
            return 2 
        if n == 1: 
            return 1 
        else: 
            return (K_int(n-1)+K_int(n-2))**2
    
    Kn = []
    for n in range(start,stop,step):
        Kn.append(K_int(n))        
        
    return (Kn) 
        
    

    
    
    

    
        
        
            
        
    
