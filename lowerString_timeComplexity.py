# Creating a function for strings
def string_lower(n):
    return n.lower()

# Declaring the main method
if __name__ == '__main__':
    import string
    import random
    import timeit
    import matplotlib.pyplot as plt

    # Defining the inputs(n) in an ascending order
    input1 = ("".join(random.choices(string.ascii_uppercase + string.ascii_letters, k=15)))
    input2 = ("".join(random.choices(string.ascii_uppercase + string.ascii_letters, k=45)))
    input3 = ("".join(random.choices(string.ascii_uppercase + string.ascii_letters, k=80)))
    input4 = ("".join(random.choices(string.ascii_uppercase + string.ascii_letters, k=100)))
    million_size = ("".join(random.choices(string.ascii_uppercase + string.ascii_letters, k=1000000)))

    # Putting all the input sizes in a list
    input_size = [15, 45, 80, 100]

    # Time taken for the program to run when a certain amount of input is used
    time_taken = [timeit.timeit("string_lower(\"input1\")", setup="from __main__ import string_lower"),
                  timeit.timeit("string_lower(\"input2\")", setup="from __main__ import string_lower"),
                  timeit.timeit("string_lower(\"input3\")", setup="from __main__ import string_lower"),
                  timeit.timeit("string_lower(\"input4\")", setup="from __main__ import string_lower")]

    million_size_time = [timeit.timeit("string_lower(\"million_size\")", setup="from __main__ import string_lower")]

    print(f"The time complexity when input length is 15 = {time_taken[0]}")
    print(f"The time complexity when input length is 45 = {time_taken[1]}")
    print(f"The time complexity when input length is 80 = {time_taken[2]}")
    print(f"The time complexity when input length is 100 = {time_taken[3]}")
    print("")
    print(f"The estimated time complexity when string length is 1000000 = {million_size_time[0]}")

    # Plotting the graph of input size and the time taken
    plt.plot(input_size, time_taken)
    # naming the axis
    plt.xlabel("input size")
    plt.ylabel("time taken")
    # Showing the graph to the user.
    plt.show()
