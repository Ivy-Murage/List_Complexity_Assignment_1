# Importing the random package
import random

# Creating a function for the strings
def sort_integers():

    # creating empty list
    values = []

    # adding some random values to the list
    for i in random.sample(range(1, 1000), 100):
        values.append(i)

    # printing maximum value
    print("The sorted integers are:", sorted(values))

if __name__ == '__main__':
    sort_integers()

