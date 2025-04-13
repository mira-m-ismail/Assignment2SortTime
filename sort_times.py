"""This Python program records the sort time taken for 8 unsorted arrays of different sizes,
and compares sorting times of three different sorts (insertion, merge & quick.) Then, the same
solrting algorithms are used & timed on sorted arrays, and a hybrid sort function is also created in order
to efficiently deal with sorted arrays.

Group: Mira, Salma, Misbah, Reem"""

import time
import random
import plotter
from sorts import insertion_sort, merge_sort, quick_sort, quick_insertion_sort


SIZES = [200, 500, 800, 1100, 1400, 1700, 2000] # no. of random elements in arrays


def sort_function_timer(sort_function, an_array):
    start = time.perf_counter()     # timer starts
    sort_function(list(an_array))   # passes the array to the passed sort function
    end = time.perf_counter()       # timer ends
    return (end - start)            # calculated time is returned/stored


def random_array(size):
    
    randomArray = []        # creates empty array
    for i in range(size):
        num = random.randint(1, 9999)
        randomArray.append(num)
    return randomArray


def plot_sort_time_using_random_arrays(sort_function):
    # for unsorted arrays

    print("timing", sort_function.__name__)
    plotter.new_series() # new color/line on the graph
    
    for size in SIZES:
        an_array = random_array(size) # calls the function to create array for each size
        time_taken = sort_function_timer(sort_function, an_array)
        
        plotter.add_data_point(time_taken) # plots time for each sort



def  plot_sort_time_using_sorted_z(sort_function):
    # for sorted arrays

    print("timing (sorted)", sort_function.__name__)
    plotter.new_series()

    for size in SIZES:
        an_array = list(range(size))
        time_taken = sort_function_timer(sort_function, an_array)
        
        plotter.add_data_point(time_taken)




def main():
    plotter.init("Sort Time", "Array Size", "Time")
    
    #plot_sort_time_using_random_arrays(insertion_sort)
    #plot_sort_time_using_random_arrays(merge_sort)
    #plot_sort_time_using_random_arrays(quick_sort)
    #plot_sort_time_using_random_arrays(quick_insertion_sort)
    
# for random arrays, quick sort works relatively best.

    plot_sort_time_using_sorted_z(insertion_sort)
    plot_sort_time_using_sorted_z(merge_sort)
    #plot_sort_time_using_sorted_z(quick_sort)
    plot_sort_time_using_sorted_z(quick_insertion_sort)

# for sorted arrays, quick insertion sort works relatively best.

    plotter.plot()

    input("Press Enter to exit:")  # keeps the plot window open

main()