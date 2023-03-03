# python3

import sys
import threading
import numpy as np

            
def compute_height(n, values):
    # Write this function
    max_height = 0
    heights = np.zeros(n, dtype=int)

    def get_height(i):
        if heights[i] != 0:
            return heights[i]
        
     

        if values[i] == -1:
            heights[i] = 1
        else:
            heights[i] = get_height(values[i]) + 1

        
        return heights[i]

    for i in range(n):
        height = get_height(i)
        if height > max_height:
            max_height = height
    # Your code here
    return max_height

def main():
    source = input("Enter I or F: ").strip().upper()

    if source == 'I':
        n = int(input("Enter element count: "))
        values = np.asarray(list(map(int, input("Enter values: ").split())))
    elif source == 'F':
        filename = input("Enter file name: ")
        if 'a' in filename:
            return
        with open(f"./test/{filename}", "r") as file:
            n = int(file.readline())
            values = np.asarray(list(map(int, file.readline().split())))
    else:
            print("Invalid source")
            return

    max_height = compute_height(n, values)

    print(max_height)


    

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=solve).start()
