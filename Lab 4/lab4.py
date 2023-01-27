def seasons(year, month, day):
    """
    (int, int, int) -> [str, int]
    A function that is passed a month and day, determines the season, and then 
    calculates the number of days since the current season begins and returns
    the season and days as a two element list.

    Students may assume that the seasons begin on the 21st day of March, June,
    September and December. Student SHOULD consider leap year. 

    Please refer to the handout for test cases and error conditions.
    """
    if year % 100 == 0 and year % 400 == 0:
        feb = list (range(1,30));
        leap = True 
    elif not year % 100 == 0 and year % 4 == 0: 
        feb = list (range(1,30));
        leap = True
    else: 
        feb = list (range(1,29));   
        leap = False
    
    if month == 3 and day >= 21 and day <= 31: 
        season = 'spring', (day - 21)
        
    elif month == 4 and day >= 1 and day <= 30:
        season = 'spring', (10 + day)
        
    elif month == 5 and day >= 1 and day <= 31:
        season = 'spring', (40 + day)
        
    elif month == 6 and day >= 1 and day < 21:
        season = 'spring', (70 + day)
        
    elif month == 6 and day >= 21 and day <= 30:
        season = 'summer', (day - 21) 
        
    elif month == 7 and day >= 1 and day <= 31:
        season = 'summer', (10 + day)   
        
    elif month == 8 and day >= 1 and day <= 30:
        season = 'summer', (40 + day) 
        
    elif month == 9 and day >= 1 and day < 21:
        season = 'summer', (70 + day) 
        
    elif month == 9 and day >= 21 and day <= 30:
        season = 'autumn', (day - 21)
        
    elif month == 10 and day >= 1 and day <= 31:
        season = 'autumn',(10 + day) 
        
    elif month == 11 and day >= 1 and day <= 30:
        season = 'autumn', (40 + day)
        
    elif month == 12 and day >= 1 and day < 21:
        season = 'autumn', (70 + day)   
        
    elif month == 12 and day >= 21 and day <= 31:
        season = 'winter', (day)
        
    elif month == 1 and day >= 1 and day <= 31:
        season = 'winter', (day + 10)
        
    if month == 2 and day >= 1 and day <= 28:
        season = 'winter', (40 + day)  
        
    elif month == 3 and day >= 1 and day < 21:
        season = 'winter', (40 + len(feb) + day)
        
    elif month == 2 and day == 29 and leap: 
        season = 'winter', (40 + day)
        
    if month == 2 and day >= 29 and not leap:  
        season = 'invalid day', (0-1)
    elif month > 12: 
        season = 'invalid month', (0-1)
    elif month <= 0:
        season = 'invalid month', (0-1)
    elif day > 31: 
        season = 'invalid day', (0-1) 
    elif day <= 0: 
        season = 'invalid day', (0-1)
        
    return season
        
    
        
    
        
    
#jan = list(range(1,32))
#mar = list (range(1,32))
#apr = list (range(1,31))
#may = list (range(1,32))
#jun = list (range(1,31))
#jul = list (range(1,32))
#aug = list (range(1,32))
#sep = list (range(1,31))
#octo = list (range(1,32))
#nov = list (range(1,31))
#december = list (range(1,32))



