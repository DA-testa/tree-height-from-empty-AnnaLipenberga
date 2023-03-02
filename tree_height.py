# python3

import sys
import threading
#import numpy as np

            
def compute_height(n, values):
    # Write this function
    max_height = 0
    visited = [False]*n

    def get_height(i):
        if visited[i]:
            return 0
        
        visited[i] = True

        if values[i] == -1:
            height = 1
        else:
            height = get_height(values[i]) + 1

        visited[i] = False
        return height

    for i in range(n):
        height = get_height(i)
        if height > max_height:
            max_height = height
    # Your code here
    return max_height

def solve():
    text = sys.stdin.readline().strip()
    if text.startswith('I'):
        n = int(sys.stdin.readline())
        values = list(map(int, sys.stdin.readline().split()))
    elif text.startswith('F'):
        filename = sys.stdin.readline().strip()
        if 'a' in filename:
            return
        with open("./test/" + filenam, "r") as file:
            n = int(file.readline())
            values = list(map(int, file.readline().split()))

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

if __name__ == "__main__":
    solve()
