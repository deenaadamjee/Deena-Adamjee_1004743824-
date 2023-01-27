# Write a function that evaluates tanh-1(x) from the series
#
# tanh-1(x) = x + x3/3 + x5/5 + x7/7 + x9/9 + ...
#
# where x < 1.0 and x > -1.0.  The function should take x and, n, 
# the number of elements in the sum and return the approximation. 


def estimate_tanh_inv(x, N):
    '''(float, int) -> float
    Returns an estimate of tanh^-1 based on the series:
    tanh-1(x) = x + x3/3 + x5/5 + x7/7 + x9/9 + ...
    with N elements
    '''
    tanh_inv = x
    for i in range(3, 3 + 2 * (num - 1), 2):
        #print(i)
        tanh_inv += x**i / i
        
    return tanh_inv

x = -2
num = 0
while x < -1.0 or x > 1.0 or num < 5:
    x = float(input("Enter x between -1 and 1: "))
    num = int(input("Enter number of terms of series (5 or higher): "))

tanh_inv = estimate_tanh_inv(x,num)
print("tanh-1(", x, ") = ", tanh_inv, sep="")

