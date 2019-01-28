terms = ['computer', 'ram', 'binary', 'io', 'network', 'ethernet',
         'java', 'yeet', 'printer', 'hexadecimal', 'megabyte',
         'kilobyte', 'bit', 'code', 'python', 'logic', 'algorithm'
         'heuristic', 'fortnite', 'tik tok', 'octal', 'usb',
         'hdmi', 'server', 'ip', 'mountain dew', 'dell' , 'linux',
         'ubuntu', 'windows', 'mac', 'zip', 'compression', 'jpeg', 
         'gif', 'png', 'unicode', 'ascii', 'rom', 'memory', 'mouse',
         'hard drive',  'peripheral', 'rgb', 'byte', 'dvi', 'html',
         'technology', 'idle', 'holy grail', 'operating system',
         'ide', 'javascript', 'css', 'text editor']


# write functions here

def num_letters(word_list):
    ''' return the total number of characters in terms '''
    
    count = 0

    for word in word_list:
        count += len(word)

    return count

def first_letter_b(word_list):
    ''' return the number of terms with b as the first letter '''

    count = 0

    for word in word_list:
        if word[0] == 'b':
            count += 1

    return count

def has_e_fourth(word_list):
    ''' return the number of terms with e as the fourth letter '''

    count = 0

    for word in word_list:
        if len(word) > 3 and word[3] == 'e':
            count += 1

    return count

def len_word(word_list):
    ''' returns the number of 5 character terms '''
    
    count = 0

    for word in word_list:
        if len(word) == 5:
            count += len(word)

    return count

def average_len(word_list):
    ''' returns the average length of all terms '''

    count = 0

    for word in word_list:
        if sum (map(len, word) ) / len(word):
            count += 1

    return count


def len_letter(word_list):
    ''' returns the number of letters in the longest terms '''

    count = 50

    for word in word_list:
        if len(word) > count:
            count = len(word)

        return count

    
def longest_term(word_list):
    ''' returns the longest term '''

    count = 0

    for word in word_list:
         if len(word) >= 4:
             count +=1

         return count
             

def has_s_last(word_list):
    ''' returns the number of terms with 's' as the last letter '''

    count = 0

    for word in word_list:
        if word[-1] == 's':
            count += 1

    return count

def total_num_e(word_list):
    ''' returns the total number of e's in the terms '''

    count = 0

    for word in word_list:
        if len(word) or word == 'e':
            count += 1

    return count 

def total_num_letters(word_list):
    ''' returns the total number of letters in terms '''

    count = 0

    for word in word_list:
        if len(word):
            count += 10

    return count
    
# test functions here

print( num_letters(terms) )
print( first_letter_b(terms) )
print( has_e_fourth(terms) )
print( len_word(terms) )
print( average_len(terms) )
print( len_letter(terms) )
print( longest_term(terms) )
print( has_s_last(terms) )
print( total_num_e(terms) )
print( total_num_letters(terms) )

'''
Your turn...

1) - Write a function that returns the number of 5 character terms.
2) - Write a function that returns the average length of all terms.
3) Write a function that returns the number of letters in the
   longest terms.
4) Write a function that returns the longest term.
5) - Write a function that returns the number of terms with 's' as
   the last letter.

Trickier...

6) - Write a function that returns the total number of e's in the
   terms.
7) - Write a function that returns the total number of letters in
   terms. (Don't count the spaces.)
'''
