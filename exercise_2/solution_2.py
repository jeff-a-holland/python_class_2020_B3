#!/Users/jeff/.pyenv/shims/python

import re

def tr(str1, str2):
    # Test for null argument to the tr function.
    # Throw a TypeError if one or both arguments are null.
    if str1 == '' or str2 == '':
        raise TypeError('ERROR. The tr function requires two non-null arguments.')

    def translate(str3):
        # Check if str3_list chars are in str2_list. If so, replace with str2,
        # which is a single char.
        str1_list = list(str1)
        str3_list = list(str3)
        for letter in str3_list:
            if letter in str1_list:
                # Use regex to replace letter
                str3 = re.sub(rf'{letter}', str2, str3)
        return(str3)
    return translate

vowels_to_c = tr('aeiou', 'c')
print(vowels_to_c('The quick dog'))
