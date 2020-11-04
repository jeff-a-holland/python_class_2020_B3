#!/Users/jeff/.pyenv/shims/python

def tr(str1, str2):
    # Test for null argument to the tr function.
    # Throw a TypeError if one or both arguments are null.
    if not str1 or not str2:
        raise TypeError('ERROR. The tr function requires two non-null arguments.')

    def translate(str3):
        # create lists containing string chars
        str1_list = list(str1)
        str2_list = list(str2)
        str3_list = list(str3)

        if len(str1_list) == len(str2_list):
            # Enumerate str3_list so we know index of char that needs to be
            # replaced with char from str1_list.
            for index, letter in enumerate(str3_list):
                if letter in str1_list:
                    index_position = str1_list.index(letter)
                    str3_list[index] = str2_list[index_position]
                # Combine updated str3_list chars and clobber str3 var to return
                str3 = ''.join(str3_list)
            return(str3)

        elif len(str1_list) > len(str2_list):
            # Determine how much shorter string2 is
            delta = len(str1_list) - len(str2_list)
            # Create copy of str2_list as it's mutable and need to pop last event
            # for operating on str2_list later
            temp_str = str2_list.copy()
            str2_last_char = temp_str.pop()
            # Pad string2_list with last char until it matches cardinality of
            # string1_list
            str2_list.extend(str2_last_char * delta)
            # DRY violation as repeating code for loop from above. Could put this
            # section in its own function and call it above and below, but the
            # complexity is not worth it.
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

vowels_to_c = tr('eqz', 'ip')
print(vowels_to_c('the quick brown fox jumps over the lazy dog'))
