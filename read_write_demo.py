f = open('/Users/ekea./python_scripting/some_file.txt', 'r')
file_data = f.read()
f.close()

new_f = open('/Users/ekea./python_scripting/another_file.txt', 'w')
new_f.write(file_data)
new_f.close()
