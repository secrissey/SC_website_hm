#Question 1 solution
def hello_name(user_name):
    """Display a simple greeting."""
    print("Hello, " + user_name.title() + "!")

hello_name('joanne')


#Question 2 solution
odd_numbers = list(range(1,101,2))
print(odd_numbers)


#Question 3 solution
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([1,2,3,4,5,6])
print(max_num_in_list([1,2,3,4,5,6]))


#Question 4 solution
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 4 1.b solution

def is_leap(a_year):
    if a_year % 4 == 0 or (a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2019)


#Question 5 solution
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)

is_consecutive([0,1,2,3,4,5])