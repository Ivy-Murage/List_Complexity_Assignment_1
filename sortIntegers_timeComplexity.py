# Defining the sort function
def sort_integers(n):
    return sorted(n)

# importing the function as __main__
if __name__ == "__main__":
    import timeit
    import random
    import matplotlib.pyplot as plt

    # Creating different inputs. The size of the input is increasing
    value1 = random.sample(range(1, 100), 9)
    value2 = random.sample(range(1, 100), 20)
    value3 = random.sample(range(1, 100), 50)
    value4 = random.sample(range(1, 101), 100)
    million_inputs = random.sample(range(1, 1000001), 100000)

    # Defining the input size. It increases gradually
    input_size = [9, 20, 50, 100]
    # Defining the time taken as
    time_taken = [timeit.timeit("sort_integers(\"value1\")", setup="from __main__ import sort_integers"),
                  timeit.timeit("sort_integers(\"value1\")", setup="from __main__ import sort_integers"),
                  timeit.timeit("sort_integers(\"value1\")", setup="from __main__ import sort_integers"),
                  timeit.timeit("sort_integers(\"value1\")", setup="from __main__ import sort_integers")]

    # find time complexity when the input size is 1000000
    million_inputs_time = [timeit.timeit("sort_integers(\"million_size\")", setup="from __main__ import sort_integers")]

    # print the time complexity when input size is 1000000
    print(f"The approximate time complexity when the input size is 1000000 = {million_inputs_time[0]}")

    # Plotting the graph of input size and the time taken
    plt.plot(input_size, time_taken)
    # naming the axis
    plt.xlabel("input size")
    plt.ylabel("time taken")
    # Showing the graph to the user.
    plt.show()
