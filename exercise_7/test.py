#!/Users/jeff/.pyenv/shims/python

import os
import re

func_dict = {}
func_name = ''
temp_str = ''
for file in os.listdir('.'):
    if file.startswith('server_func_'):
        func_name = re.sub('^server_func_', '', file)
        func_name = re.sub('\.py$', '', func_name)
        with open(file, 'r') as fh:
            temp_str = ''
            for line in fh.readlines():
                if line.startswith('def '):
                    temp_str = temp_str + line
                elif not line.startswith('def '):
                    temp_str = temp_str + line
            func_dict[func_name] = temp_str
        temp_str = ''
        func_name = ''

for keys, values in func_dict.items():
    print(keys)
    print(values)
    print('\n')
