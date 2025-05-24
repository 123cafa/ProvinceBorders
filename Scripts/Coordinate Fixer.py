broken = input("Put untouched coordinates here: ") # Format [[[numbers],[numbers],[numbers]]]

broken = broken.replace(']]]', '')
broken = broken.replace('[[[', '')

coordinates = broken.split("],[")
fixed_coordinate = ''
fixed_coordinate_list = []

for i in range(0, len(coordinates)):
    split_coordinate = coordinates[i].split(",")
    first = split_coordinate[0]
    second = split_coordinate[1]
    fixed_coordinate = second + ", " + first
    fixed_coordinate_list.append(fixed_coordinate)

for i in range(0, len(fixed_coordinate_list)):
    print(fixed_coordinate_list[i])