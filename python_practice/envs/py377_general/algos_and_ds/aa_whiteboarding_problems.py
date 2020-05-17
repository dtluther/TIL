## Day 1a
def digital_root(num):
    '''
    Write a method, digital_root(num). It should sum the digits of a positive
    integer. If it is greater than or equal to 10, sum the digits of the
    resulting number. Keep repeating until there is only one digit in the
    result, called the "digital root". Do not use string conversion within your
    method.
    '''

    if num < 10:
        return num

    import math

    sum = 0
    while num >= 10:
        digit = num % 10
        sum += digit
        num = math.floor(num / 10)
    
    sum += num

    if sum < 10:
        return sum
    else:
        return digital_root(sum)
        
print(digital_root(8))                  # 8
print(digital_root(11))                 # 2
print(digital_root(123))                # 6
print(digital_root(29))                 # 2
print(digital_root(999999999999992))    # 119 => 11 => 2

def caesar_cipher(message, increment):
    '''
    Write a function that takes a message and an increment amount and outputs
    the same letters shifted by that amount in the alphabet. Assume lowercase
    and no punctuation. Preserve spaces.
    '''

    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    indices = [i for i in range(0, 26)]
    letter_map = dict(zip(indices, alphabet))

    message_chars = list(message)
    for idx, char in enumerate(message_chars):
        if char == ' ':
            continue 
        letter_idx = ord(char) % ord('a')
        new_idx = (letter_idx + increment) % 26
        new_letter = letter_map[new_idx]
        message_chars[idx] = new_letter

    return ''.join(message_chars)

print(caesar_cipher('hey', 0))
print(caesar_cipher('hey', 1))
print(caesar_cipher('hey', 3))
print(caesar_cipher('hello', 15))

## Day 1b
def longest_common_substring(str1, str2):
    str2_indices = {}
    for idx, char in enumerate(str2):
        if str2_indices[char]:
            str2_indices[char].append(idx)
        else:
            str2_indices[char] = [idx]

    long = ''
    sub1 = ''
    sub2 = ''
        
    for idx, char in enumerate(str1):
        if char in str2_indices:
            idx2 = str2_indices[char]
            idx1 = idx

            sub1 = str1[idx1]
            sub2 = str2[idx2]

            while len(str2)-1 >= idx2 & len(str1)-1 >= idx1:
                


