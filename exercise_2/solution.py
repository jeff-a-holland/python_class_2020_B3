#!/Users/jeff/.pyenv/shims/python

import re

def tr(str1, str2):
    # Test for null argument to the tr function.
    # Throw a TypeError if one or both arguments are null.
    if str1 == '' or str2 == '':
        raise TypeError('ERROR. The tr function requires two non-null arguments.')

    def translate(str3):
        # Check if str3_list chars are in str2_list. If so, replace with str2.
        str1_list = list(str1)
        # Build regex_string with conditional OR's for each char in str1_list
        regex_string='|'.join(str1_list)
        str3 = re.sub(rf'{regex_string}', str2, str3)
        return(str3)
    return translate

vowels_to_c = tr('eo', 'oe')
print(vowels_to_c('The quick dog'))
