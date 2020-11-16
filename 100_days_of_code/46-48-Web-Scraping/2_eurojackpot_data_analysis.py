from collections import Counter
import numpy as np
import pandas as pd
import os


## >>>>> Preparing data for analysis <<<<<

# Get the full path of the current directory
PATH = os.path.dirname(__file__)

# Load data
df = pd.read_csv(PATH + '/eurojackpot_data.csv', index_col=0)

# Delete empty rows
df = df.dropna()

# Reset index starting from 1
df.index = np.arange(1, len(df) + 1)

# Changing names of the columns
df.columns = ['Number', 'Date', 'Numbers', 'Other']

# Cleaning dataset
df = df.drop(['Other'], axis=1)

#Split the column with results ['Number'] into two separate columns with main numbers and euro numbers
df[['Numbers','Euro']] = df.Numbers.str.split('+', expand=True)


## >>>>> Euro numbers analysis <<<<<

# Count occurrence of unique combinations of euro numbers
euro_nums_occurrence = df['Euro'].value_counts()

# Export euro_nums_occurrence to a CSV file
df_euro_nums_occurrence = pd.DataFrame(euro_nums_occurrence)
df_euro_nums_occurrence.to_csv('euro_nums_occurrence.csv')

# Split the column with results ['Euro'] into two separate columns with Euro_num_1 and Euro_num_2
df_euro = pd.DataFrame(df.Euro.str.split(' ').tolist(),columns = ['to_drop', 'Euro_num_1','Euro_num_2'])
df_euro = df_euro.drop('to_drop', axis=1)

# Assign every number to a list. Added by columns order.
euro_list_ball = list(df_euro.values.T.flatten())

# Count occurrence of unique euro number
Counter(euro_list_ball).most_common()

# Count occurrence of odd, even or mix combinations of euro numbers
# Count occurence of unique combinations of euro numbers
euro_list_ball = list(df['Euro'].values.T.flatten())

def odd_even_combination(nums):
    only_odds = []
    only_even = []
    even_odd = []
    for i in nums:
        if int(i[2]) % 2 == 0 and int(i[5]) % 2 == 0:
            only_even.append(i)
        elif int(i[2]) % 2 != 0 and int(i[5]) % 2 != 0:
            only_odds.append(i)
        else:
            even_odd.append(i)

    return f"Euro numbers stats: \n \
    1. Only even numbers: {len(only_even)} times. \n \
    2. Only odd numbers: {len(only_odds)} times. \n \
    3. Mix of even and odd numbers: {len(even_odd)} times."

print(odd_even_combination(euro_list_ball))


## >>>>> Main numbers analysis <<<<<

# Count occurrence of unique combinations of euro numbers
main_nums_occurrence = df['Numbers'].value_counts()

# Split the column with results ['Numbers'] into five separate columns from Main_num1 to Main_num5
df_nums = pd.DataFrame(df.Numbers.str.split(' ').tolist(),columns = ['Main_num1','Main_num2','Main_num3','Main_num4','Main_num5','to_drop'])
df_nums = df_nums.drop('to_drop', axis=1)

# Assign every number to a list. Added by columns order.
main_list_ball = list(df_nums.values.T.flatten())

# Count occurrence of unique euro number
Counter(main_list_ball).most_common()


# Count occurrence of odd, even or mix combinations of main numbers
main_ball = list(df['Numbers'].values.T.flatten())

def main_odd_even_combinations(nums):

    # Variables that count the occurrence of specific combination
    odd_0_even_5 = 0
    odd_1_even_4 = 0
    odd_2_even_3 = 0
    odd_3_even_2 = 0
    odd_4_even_1 = 0
    odd_5_even_0 = 0

    for combination in nums:

        # Init an empty list to store the second digits from drawn numbers. eg: 5 out of 15, 7 out of 27, etc.
        second_digits = ''
        # Add every 3rd digit to the list from all numbers of a particular combination
        second_digits += combination[1::3]

        # Count odd and even numbers in second_digits
        digit_counter = Counter('odd' if int(d) % 2 else 'even' for d in second_digits)

        # Iterate over a dictionary to check the number of occurrence of odd/even digits
        for key, value in digit_counter.items():
            if key == 'even' and value == 5:
                odd_0_even_5 += 1
            elif key == 'odd' and value == 1:
                odd_1_even_4 += 1
            elif key == 'odd' and value == 2:
                odd_2_even_3 += 1
            elif key == 'odd' and value == 3:
                odd_3_even_2 += 1
            elif key == 'odd' and value == 4:
                odd_4_even_1 += 1
            elif key == 'odd' and value == 5:
                odd_5_even_0 += 1

        # Set list for next for loop
        num_list = ''

    return f"Main numbers stats: \n \
    1. 0 Odd - 5 Even: {odd_0_even_5} times. \n \
    2. 1 Odd - 4 Even: {odd_1_even_4} times. \n \
    3. 2 Odd - 3 Even: {odd_2_even_3} times. \n \
    4. 3 Odd - 2 Even: {odd_3_even_2} times. \n \
    5. 4 Odd - 1 Even: {odd_4_even_1} times. \n \
    6. 5 Odd - 0 Even: {odd_5_even_0} times. "


print(main_odd_even_combinations(main_ball))

