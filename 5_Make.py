'''

Bracen Gruver
4/16/2025 

steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. 
The steps_to_miles() function raises a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
 Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the 
 steps_to_miles() function. Use a try-except block to catch any ValueError object raised by the steps_to_miles() function and output the exception message.
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

'''


def get_steps():
    steps = int(input ("enter number of steps: "))
    if steps < 0:
        raise ValueError('Negative step count entered.')
    return steps

def steps_to_miles(steps):
    tot_miles = steps/2000
    return tot_miles

if __name__ == "__main__":
    try:
        steps = get_steps()
        
        tot_miles = steps_to_miles(steps)
        print("that is equivalent to", (f'{tot_miles:.2f}'), "miles")
   
    except ValueError as excpt:
        print(excpt)
        print("could not calculate miles")
