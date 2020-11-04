#!/Users/jeff/.pyenv/shims/python

def tr(str1, str2):
    # Test for null argument to the tr function.
    # Throw a TypeError if one or both arguments are null.
    if str1 == '' or str2 == '':
        raise TypeError('ERROR. The tr function requires two non-null arguments.')

    def translate(str3):
        # create list containing str1 chars
        str1_list = list(str1)
        # create list containing str3 chars
        str3_list = list(str3)

        # Check if str3_list chars are in str2_list. If so, replace with str2,
        # which is a single char.
        for index, letter in enumerate(str3_list):
            if letter in str1_list:
                str3_list[index] = str2
            # Combine updated str3_list chars and clobber str3 var to return
            str3 = ''.join(str3_list)
        return(str3)
    return translate

vowels_to_c = tr('aeiou', 'c')
print(vowels_to_c('The quick dog'))
