#import turtle 

#tina = turtle.Turtle() 
#def drawcircle(t,x,y,size,clr):
    #''' (turtle,int,int,int,str) -> NoneType Draws a filled circle using details provided ''' 
    
    #t.color(clr) 
    #t.up()
    #t.goto(x,y)
    #t.down() 
    #t.begin_fill() 
    #t.circle(size,360) 
    #t.end_fill()
    
    
    #details = [[20,'red'],[40,'green'],[20,'blue']]
    #for i in [0,1,2]: 
        #drawcircle(tina, -200+i*100,0, details[i][0], details[i][1])
        
    #turtle.done()
    
#count = [1,2,3,4]
#for x in range(3): 
    #print (x) 
    
#def count_adjacent_repeats(s): 
    #'''(str)->(int)'''
    
    #repeats=0 
    #for c in s[1:]:
        #if 
        #repeats += 1 
        #return repeats

#lst = [1,2,3,4,5]       
#def shift_list(lst): 
    #'''(lst) --> (lst)''' 
    #for i in range(len(lst)-1): 
        #lst.replace(i,i+1) 
    #for i[5] in lst:
        #lst.replace(i[5],i[1])
    #return lst 

#def shift_left(L):
    #'''(list) -> None Type Shift eachiteminLonepositiontotheleftandfirst itemtothelastposition.'''
    #first_item = L[0] 
    #for i in range(len(L)-1): 
        #L[i] =L[i+1]
    #L[-1]=first_item
    #return L
    
#def change_of_grades(grades): 
    #''' lst --> (str)''' 
    
    #average = []    
    #for marks in grades: 
        #total = 0
        #for e in marks:
            #total = e + total
        #s = total/len(marks)
        #average.append(s) 
    #print (average)
            
#import math
#def pi_over_4(k): 
    #''' (float) ---> (float,int) '''
    #d = []
    #for i in range(k): 
        #s = (-1)**(i)
        #a = (2*(i))+1
        #f = s/a
        #d.append(f)
        #pi_4 = sum(d)
    #j = [pi_4 , (k)]
    #m = tuple(j)
    #print(j) 
#wHILE LOOP DICTIONARY: 
#lst1 = ('a','b','c','d')
#lst2 = ['w','w','w,','w']
#dicti = {} 
#i = lst1[0]
#while i in lst1 != 'd': 
    #dicti[lst1[:]] = lst2[:]
    #lst1[i] = i + 1
    #print (dicti)

#{name: {birthmonth: 'month', birthmonth: 'month'}  } = dic 

#print (dic[name][birthmonth])
      
#x = int(input('enter on odd integer'))
          
#while x/2 == int(x/2):
    #print('I said an odd integer bitch')
    #x = int(input('enter on odd integer'))

#def sum_of(x):
    #print ('wow you can follow instructions') 
    #d = sum(range(x+1)) 
    #print (d)
           
#print(sum_of(x))    
        
        
        
#n = -1
#while (n % 2 == 0) or (n < 1):    
    #n = int(input("Please enter an odd, positive value: "))
    
#s = sum_of_odd(n)
#print("The sum of odd numbers from 1 to", n, "is", s)
    
#s = sum_of_odd(n)
#print("The sum of odd numbers from 1 to", n, "is", s)
    
    
    
#sum_u_need = sum_of_int(x) 

#def reverse(lst):
    #'''(list)->(list)reversesthecontentsofalist''' 
    #lst_len = len(lst)
    #for x in range(lst_len//2):
        #print(lst[x] , lst[lst_len-1])
        #print (lst[lst_len-1]) 
        #lst[x] , lst[lst_len-1-x] = lst[lst_len-1-x] , lst[x]
        #print(lst[lst_len-1-x] , lst[x])
    #print(lst)

#dicti = {}    
#lst = [] 
#s = input ('word') 
#stri = s.lower()
#for i in s: 
    #lst.append(i)

#for i in lst:
    #dicti[i]=id(i)

#count = 0 
#for i in s: 
    #if dicti.value(i) = 
#print (dicti)
#print(s)


    
    

    #if category_sel == 'Chemistry': 
        #s = win_dict['Marie Curie']['year']
        #a = win_dict
        #print (s)
    #elif category_sel == 'Physics': 
        #s = win_dict.get('Physics') 
        #print (s)
    #if category_sel == 'Literature': 
        #s = win_dict.get('Literature') 
        #print (s) 
    #else: 
        #print('No winners were found in')
    
#def func1(mult=10, reps=2):
    #result_list=[]
    #for i in range(1,reps+1):
        #result_list.append(i*mult)
    #return mult, result_list

#print (func1(5,3)) 
#print (func1(reps=1))

#import math
#def e_distance(p,q): 
    #'''fdmskdmksldmskl'''
    #sumx = []
    #for i in range(len(p)): 
        #for i in range(len(q)):
            #x = (p[i]-q[i])**2
            #sumx.append(x)
    #print(sumx)
    #d = math.sqrt(sum(x))