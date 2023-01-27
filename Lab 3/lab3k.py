#Lab3
#Use the design recipe to implement the functions within

s = input("what were your 4 test scores") 

def average_number(s):
    '''
    (str) -> float

    Given s, a string representation of a sequence of four floating
    point numbers formatted as 'number1,number2,number3,number4',
    e.g., '1.0,12.0,13.0,2.0', remove the largest and smallest number,
    calculate the average of the remaining two numbers, which in this case are
    (13.0, 2.0), and return the average in s as a floating point number (e.g. 7.5).

    >>> average_number('10.0,20.0,30.0,0.0')
    15.0
    '''
    
    marks = [float(x) for x in s.split(",")] 
    sorted_marks = sorted(marks)    
    del sorted_marks[0]
    del sorted_marks[2]    
    average = sum(sorted_marks)/2
    return average

print (average_number(s))

name = input ("What is your name?")

def first_name_last_name_to_email(name):
    '''
    (str) -> str

    Given a string name with the format "last_name first_name", return a string
    "first_name.last_name@mail.utoronto.ca", where all letters are lowercase.

    >>> first_name_last_name_to_email('Hastings Hana')
    'hana.hastings@mail.utoronto.ca'
    '''
    name = name.lower()
    last_name,first_name = name.split(" ")
    name_2 = first_name+'.'+last_name+'@mail.utoronto.ca'
    return name_2
    
print (first_name_last_name_to_email(name))

names = first_name_last_name_to_email(name)
test_marks = str(average_number(s))

def student_midterm_mark(names, test_marks):
    '''
    (str, str) -> str

    Given a student's name, with the format "last_name first_name", test
    marks formatted as 'floating_point_number1, floating_point_number2,
    floating_point_number3, floating_point_number_4', return a string
    "<email_address,midterm_mark>", where email_address has the format
    first_name.last_name@utoronto.ca and the midterm_mark is the average number
    in the sequence test_marks excluding the largest and smallest scores.
    All letters in email_address are lowercase. Note: return the string
    with no space after the comma

    >>> student_midterm_mark("Hastings Hanna",'10.0,20.0,30.0,0.0')
    '<hanna.hastings@mail.utoronto.ca,15.0>'
    '''

    midterm_mark = names+','+test_marks
    return midterm_mark
print (student_midterm_mark(names, test_marks)) 