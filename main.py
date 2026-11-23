import random


# rprint("Hello from Python!")


def calculate_average(*args):
    # Return zero when no numbers are provided.
    if not args:
        return 0

    # Calculate the sum and divide it by the number of values.
    return sum(args) / len(args)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase.
    normalized_str = ''.join(s.split()).lower()
    return normalized_str == normalized_str[::-1]

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)   

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)  

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

def prime_factors(n):
    factors = []
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    return bin(n)[2:]  
# Remove the '0b' prefix
def binary_to_decimal(b):
    return int(b, 2)    

def decimal_to_hexadecimal(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    return hex(n)[2:]  # Remove the '0x' prefix 

def hexadecimal_to_decimal(h):
    return int(h, 16)

def roll_two_dice():
    import random
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

# print("roll_two_dice", roll_two_dice()) 

def rock_paper_scissors( ):
    choices = ['rock', 'paper', 'scissors']
    options={'r':"rock", 'p':"paper", 's':"scissors"}
    want_to_play_again = True
    while True and want_to_play_again == True: 
        user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")
        user_choose=options.get(user_choice.lower())
        computer_choice= random.choice(choices)
        if computer_choice not in choices or user_choose not in choices:
            raise ValueError("Choices must be 'rock', 'paper', or 'scissors'.")

        print(f"Computer chose: {computer_choice} and you chose: {user_choose}")
        if computer_choice == user_choose:
            print ("It's a tie!")
        elif (computer_choice == 'rock' and user_choose == 'scissors') or \
            (computer_choice == 'scissors' and user_choose == 'paper') or  \
            (computer_choice == 'paper' and user_choose == 'rock'):    
            print ("Computer wins!")
        else:
            print ("You win!")   
        want_to_play_again = input("Do you want to play again? (y/n): ").lower() == 'y'
    

# rock_paper_scissors()

def load_test_list_vs_dict_vs_tuples():
    import time

    # Create a large list, dictionary, and tuple
    large_list = list(range(1000000))
    large_dict = {i: i for i in range(1000000)}
    large_tuple = tuple(range(1000000))

    # Measure time to access an element in the list
    start_time = time.time()
    _ = large_list[500000]
    list_time = time.time() - start_time

    # Measure time to access an element in the dictionary
    start_time = time.time()
    _ = large_dict[500000]
    dict_time = time.time() - start_time

    # Measure time to access an element in the tuple
    start_time = time.time()
    _ = large_tuple[500000]
    tuple_time = time.time() - start_time

    return list_time*1000, dict_time*1000, tuple_time*1000
# print "list_time, dict_time, tuple_time" in milliseconds.
# The timings are returned in seconds; multiply each value by 1000 for milliseconds.  
# print("list_time, dict_time, tuple_time",load_test_list_vs_dict_vs_tuples())

# get_all_subset_of_string: Returns a subset of the string (exclusive).
def get_all_subset_of_string(s):
    if len(s) == 0:
        return ['']
    
    subsets = []
    first_char = s[0]
    rest_subsets = get_all_subset_of_string(s[1:])
    
    for subset in rest_subsets:
        subsets.append(subset)
        subsets.append(first_char + subset)
    
    return subsets

print("get_all_subset_of_string('abc')", get_all_subset_of_string('abc')) 
#print("get_all_subset_of_string('abc')", get_all_subset_of_string('abcdefghijklmnopqrstuvwxyz'))  # Example usage

seta = {23,45,34}
setb = {23,45,34,56,78}
union_set = seta.union(setb)
intersection_set = seta.intersection(setb)
minus_set = setb.difference(seta)
join_set = seta.symmetric_difference(setb)
print("union_set", union_set)
print("intersection_set", intersection_set)     
print("minus_set", minus_set)
print("join_set", join_set)