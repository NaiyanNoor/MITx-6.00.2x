Problem 7
20.0/20.0 points (graded)
Write a function that meets the specification below:

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

You are not allowed to import anything. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed.


def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    testNo = 0
    # Check both positive and negative integers
    while True:
        if test(testNo):
            return testNo
        if test(-testNo):
            return -testNo
        testNo += 1
		
		
		#correct