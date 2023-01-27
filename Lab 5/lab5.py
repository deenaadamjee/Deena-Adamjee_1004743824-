import random
 
def deck(categories, num_of_cards_per_cat):
    """
    (list, int) -> list
    Given a list of strings representation as category names and an integer
    indicating the number of cards in one category,
    return a deck of cards as a list. For example, with ["spades", "hearts"], 2,
    return a list of list: [["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]],
    where 1 and 2 are the index of the cards.
    >> deck(["spades", "hearts"], 2)
    [["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]]
    >> deck(["spades", "hearts"], -5)
    []
    """     
    cat = []
    for x in categories:
        for y in range(1, num_of_cards_per_cat+1):
            card = [x,y]
            cat.append(card)
    return cat
        
def random_shuffle(lst):
    """
    (list) -> list
    Receives a deck of cards and returns a randomly ordered
    list containing all of the same elements.
    The returned list should preserve the order of the categories. See below
    console outputs as an example, where "s" and "d" stay in the same order as
    the input and only the numbers are shuffled.
    >> random_shuffle([["s",1],["s",2],["s",3],["d",1],["d",2],["d",3]])
    [["s",3],["s",1],["s",2],["d",2],["d",1],["d",3]]
    """
    a = len(lst)    
    num = (random.sample(range(1,(lst[-1][-1])+1),(lst[-1][-1])))*len(lst)
    x = 0     
    for A_Number in range(a):
        lst[A_Number][-1] = num[x]
        x = x + 1        
    return lst







#shuffle = []  
#for x in range(0,len(lst)+1): 
    #for n in num:
        #shuffle1 = [x,n]
        #shuffle.append(shuffle1) 
#return shuffle


#a = lst[-1][-1]
#rand = random.sample(range(1,a+1),a)
#rand = rand*len(lst)
    
    

def reverse(lst):
    """
    (list) -> list
    Receives a list and returns a reverse ordered list containing all of the same elements.
    >> reverse([["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]])
    [["hearts", 2], ["hearts", 1], ["spades", 2],["spades",1]]
    """
    
    lst = lst[::-1]
    return (lst)