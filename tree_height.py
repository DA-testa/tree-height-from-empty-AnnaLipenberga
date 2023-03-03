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


 
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
