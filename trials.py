"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    return result


def print_as_numbered_list(items):
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]}")


def get_range(start, stop):
    nums = []

    for i in range(start, stop):
        nums.append(i)
    
    return nums


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return "".join(chars)

def snake_to_camel(string):
    camel_case = []
    words = string.split('_')
    for word in words:
        word = word[0].upper() + word[1:]
        camel_case.append(word)
    return "".join(camel_case)    


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest


def truncate(string):
    result = []

    for char in string:
        if (len(result) == 0) or (char != result[-1]):
            result.append(char)

    return "".join(result)
            

def has_balanced_parens(string):
    paren = 0

    for char in string:
        if char == '(':
            paren += 1
        elif char == ')':
            paren -= 1
            if paren < 0:
                return False
    
    return paren == 0


def compress(string):
    pass  # TODO: replace this line with your code
