def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]# slice operator = start : end : pas

def find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None
    for number in numbers:
        if is_palindrome(number):
            palindrome_count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number
    return (palindrome_count, greatest_palindrome)


number_list = [121, 12321, 45654, 123, 98789, 256]
result = find_palindromes(number_list)
print(result) 