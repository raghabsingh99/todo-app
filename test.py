def get_average():
    with open("files/doc.txt") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    average_loc = sum(values)/len(values)


    return average_loc


average = get_average()
print(average)