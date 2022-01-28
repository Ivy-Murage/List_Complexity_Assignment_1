# Creating the function to find the maximum value in a list
def maximumValue(n):
    return max(n)

# Declaring the main method
if __name__ == '__main__':
    import timeit
    import random
    import matplotlib.pyplot as plt

    # Creating different inputs. The size of the input is increasing
    value1 = random.sample(range(1, 100), 9)
    value2 = random.sample(range(1, 100), 20)
    value3 = random.sample(range(1, 100), 50)
    value4 = random.sample(range(1, 101), 100)
    value5 = random.sample(range(1, 1000001), 1000000)

    # Defining the input size. It increases gradually
    input_size = [9, 20, 50, 100]
    # Defining the time taken as
    time_taken = [timeit.timeit("maximumValue(\"value1\")", setup="from __main__ import maximumValue"),
                  timeit.timeit("maximumValue(\'value2\')", setup="from __main__ import maximumValue"),
                  timeit.timeit("maximumValue(\'value3\')", setup="from __main__ import maximumValue"),
                  timeit.timeit("maximumValue(\'value4\')", setup="from __main__ import maximumValue")]

    million_input = [timeit.timeit("maximumValue(\'value5\')", setup="from __main__ import maximumValue")]


    print(f'The maximum value from the first random input is: {maximumValue(value1)}')
    print(f'The maximum value from the second random input is: {maximumValue(value2)}')
    print(f'The maximum value from the third random input is: {maximumValue(value3)}')
    print(f'The maximum value from the fourth random input is: {maximumValue(value4)}')
    print("")
    print(f'Time complexity for each algorithm with respective input is : {time_taken}')
    print("")
    print(f'The approximate time it takes to find maximum value when the input size is 1000000 = {million_input}')

    # Plotting the graph of input size and the time taken
    plt.plot(input_size, time_taken)
    # naming the axis
    plt.xlabel("input size")
    plt.ylabel("time taken")
    # Showing the graph to the user.
    plt.show()