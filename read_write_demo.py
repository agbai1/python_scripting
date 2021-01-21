with open('/Users/ekea./python_scripting/some_file.txt', 'r') as f:
    file_data = f.read()


print("File Data for some_file.txt: \n" + file_data)

with open('/Users/ekea./python_scripting/another_file.txt', 'w') as new_f:
    new_f.write(file_data)

with open('/Users/ekea./python_scripting/another_file.txt', 'r') as f:
    print("File Data for another_file.txt:")
    for line in f:
        print(line, end='')
