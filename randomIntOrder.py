
# This program initializes a list
# with ten random integers
# and then prints five lines of output:
# 
# - every element at an even index;
# - every even element;
# - all elements in reverse order;
# - only the first and last elements;
# - all elements in the list.



import random


# Generates a list of ten random integers between 1 and 100.
def generateRandomInts():
    randomList = [random.randint(1, 100) for _ in range(10)]
    return randomList



# Main function evaluates and prints list elements.    
def main():
    randomList = generateRandomInts()
    # Prints every element at an even index.
    evenIndexElements = randomList[::2]
    print("Every element at an even index: ", evenIndexElements)
    print(" ")

    # Prints every even element.
    evenElements = [x for x in randomList if x % 2 == 0]
    print("Every even element: ", evenElements)
    print(" ")

    # Prints all elements in reverse order.
    reverseOrder = randomList[::-1]
    print("All elements in reverse order: ", reverseOrder)
    print(" ")

    # Prints only the first and last element.
    firstAndLast = [randomList[0], randomList[-1]]
    print("Only the first and last element: ", firstAndLast)
    print(" ")

    # Prints all elements in the list.
    print("All elements in the list: ", randomList)
    (" ")



main()



        
