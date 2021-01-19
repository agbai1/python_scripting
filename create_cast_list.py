def create_cast_list(filename):
"""
    Isolates and returns only the names of actors from a text file

    INPUT:
    filename: txt file. Text file containing actor's name and some other movie informations

    OUTPUT:
    cast_list: file object: Returns a list of a actors froma TV show
"""
    cast_list = []

    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            file_data = line.split(',')[0]

            cast_list.append(file_data)

    return cast_list


cast_list = create_cast_list('/Users/ekea./python_scripting/flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
