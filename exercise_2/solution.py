#!/Users/jeff/.pyenv/shims/python

def tr(str1, str2):
    # Test for null argument to the tr function.
    # Throw a TypeError if one or both arguments are null.
    if str1 == '' or str2 == '':
        raise TypeError('ERROR. The tr function requires two non-null arguments.')

    def translate(str3):
        # create list containing str1 chars
        str1_list = list(str1)
        str2_list = list(str2)
        str3_list = list(str3)

        if len(str1_list) == len(str2_list):
            for index, letter in enumerate(str3_list):
                if letter in str1_list:
                    index_position = str1_list.index(letter)
                    str3_list[index] = str2_list[index_position]
                # Combine updated str3_list chars and clobber str3 var to return
                str3 = ''.join(str3_list)
            return(str3)

        elif len(str1_list) > len(str2_list):
            ## Code this section
            delta = len(str1_list) - len(str2_list)
            temp_str = str2_list.copy()
            str2_last_char = temp_str.pop()
            str2_list.extend(str2_last_char * delta)

            for index, letter in enumerate(str3_list):
                if letter in str1_list:
                    index_position = str1_list.index(letter)
                    str3_list[index] = str2_list[index_position]
                # Combine updated str3_list chars and clobber str3 var to return
                str3 = ''.join(str3_list)
            return(str3)

        else:
            raise TypeError('ERROR. str1 cardinality less than str2. Exiting.')
    return translate

vowels_to_c = tr('eq', 'ip')
print(vowels_to_c('the quick brown fox jumps over the lazy dog'))
