def list_to_dict(titles,nobel_winners_list): 
    '''fnrjiefre''' 
    
    #titles1 = titles.remove('scientist')
    #nobel_winners_list.remove[1]('')
    nobel_winners = {} 
    
    part_0 = {}
    for i in range(len(titles)): 
        for i in range(len(nobel_winners_list[0])): 
            part_0[titles[i]] = nobel_winners_list[0][i]
    
    part_1 = {}
    for x in range(len(titles)): 
        for x in range(len(nobel_winners_list[1])): 
            part_1[titles[x]] = nobel_winners_list[1][x]
    
    part_2 = {}
    for y in range(len(titles)):
        for y in range(len(nobel_winners_list[2])): 
            part_2[titles[y]] = nobel_winners_list[2][y]
    
    part_0.pop('scientist')
    part_1.pop('scientist') 
    part_2.pop('scientist') 
            
    nobel_winners[nobel_winners_list[0][0]] = part_0
    nobel_winners[nobel_winners_list[1][0]] = part_1
    nobel_winners[nobel_winners_list[2][0]] = part_2
    
    print (nobel_winners)     
    return nobel_winners
    

#{'Marie Curie': {'year': 1911, 'category': 'Chemistry'}, 'Max Planck': {'year': 1918, 'category': 'Physics'}, 'Linus Pauling': {'year': 1955, 'category': 'Chemistry'}}

nobel_winners = {'Marie Curie': {'year': 1911, 'category': 'Chemistry'}, 'Max Planck': {'year': 1918, 'category': 'Physics'}, 'Linus Pauling': {'year': 1955, 'category': 'Chemistry'}}

def print_nobel_winners(win_dict, category_sel):
    '''fsnjfkdsnfjdksfsd''' 
    
    scientist = []
    for keys in nobel_winners: 
        scientist.append(keys)
    
    year_1 = []
    year_1.append(nobel_winners['Marie Curie']['year']) 
    year_1.append(nobel_winners['Linus Pauling']['category']) 
    year_2 = []
    year_2.append(nobel_winners['Max Planck']['year'])    
    
    
    marie_1= {} 
    marie_1[scientist[0]]=year_1[0]
    print(marie_1) 
    
    maxP_1 = {} 
    maxP_1[scientist[1]]=year_1[1]
    linus_1 = {} 
    linus_1[scientist[2]]=year_2
    
    
    if category_sel == 'Chemistry': 
        s = marie_1['Marie Curie']
        y = marie_1
    print (y) 
    
  