# Importing the random package
import random

# Creating a function for the list of values
def maximumValue():

    # creating empty list
    values = []

    # adding some random values to the list
    for i in random.sample(range(1, 1000), 100):
        values.append(i)

    # printing maximum value
    print("The randomly generated list: ", values)
    print("The maximum value is:", max(values))

if __name__ == '__main__':
    maximumValue()

