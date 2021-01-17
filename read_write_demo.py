with open('/Users/ekea./python_scripting/some_file.txt', 'r') as f:
    file_data = f.read()


with open('/Users/ekea./python_scripting/another_file.txt', 'w') as new_f:
    new_f.write(file_data)
    new_f.close()
