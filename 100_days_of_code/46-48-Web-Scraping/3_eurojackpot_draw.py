import pandas as pd
import random
import os


# Get the full path of the current directory
PATH = os.path.dirname(__file__)

# Load data, change column name, delete duplicated column
euro_nums_occurrence = pd.read_csv(PATH + '/euro_nums_occurrence.csv', index_col=0)
euro_nums_occurrence['x times'] = euro_nums_occurrence['Euro']
euro_nums_occurrence = euro_nums_occurrence.drop('Euro', 1)

def get_main_numbers():
    for pool, numbers in (50, 5),:
        main_numbers = sorted(random.sample(range(1, pool + 1), numbers))
    return main_numbers

def get_euro_numbers():
    for pool, numbers in (10, 2), :
        euro_numbers = sorted(random.sample(range(1, pool + 1), numbers))
    return euro_numbers

def get_eurojackpot_numbers(number_of_draws):
    eurojackpot_nums = [(get_main_numbers(), get_euro_numbers())
                        for draw in range(int(number_of_draws))]
    print("The next Eurojackpot numbers may be: ")
    return eurojackpot_nums

def get_euro_nums_most_common(grater_then):
    # grater_then is the number of occurrence
    return euro_nums_occurrence[euro_nums_occurrence['x times'] > grater_then]

def check_even_odd_ratio(main_numbers):
    event_count = [num
                 for num in main_numbers
                 if num % 2 == 0]
    odd_count = [num
                 for num in main_numbers
                 if num % 2 != 0]
    return f"Even: {event_count}, Odd: {odd_count}"


if __name__ == "__main__":
    eurojackpot = get_eurojackpot_numbers(7)
    print(eurojackpot)

    print(f"Most common euro numbers are:")
    print(get_euro_nums_most_common(12))
