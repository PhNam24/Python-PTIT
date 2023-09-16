def is_palindrome_in_base(number, base):
    decimal_number = int(number)
    converted_number = ""

    while decimal_number > 0:
        remainder = decimal_number % base
        converted_number += str(remainder)
        decimal_number = decimal_number // base

    return converted_number == converted_number[::-1]

def count_palindromes_in_range(a, b, m):
    count = 0

    for number in range(a, b+1):
        is_palindrome = True
        for base in range(2, m+1):
            if not is_palindrome_in_base(number, base):
                is_palindrome = False
                break
        if is_palindrome:
            count += 1

    return count
a, b, m = map(int, input().split())
result = count_palindromes_in_range(a, b, m)
print(result)