
import timeit

min_val = 100
max_val = 200
stop = None

data = [4, 5, 104, 105, 110, 
        120, 130, 130, 150, 
        160, 170, 183, 185, 
        187, 188, 191, 350, 
        360, 400, 600, 750, 
        1000]




def clean_values(data):

    # Deleting values outside the set range backwards
    top_index = len(data) - 1

    for index, value in enumerate(reversed(data)):
        # Because the index
        print(f"Index: {index} Value: {value}")
        if value > max_val or value < min_val:
            print(f"Top Index: {top_index}, {value}")
            print(f"Top Index: ({top_index} - {index} = {top_index-index}) ")
            del data[top_index-index]


def cleanvalues2(data):
    # Deleting values outside the set range backwards
    top_index = len(data) - 1
    temp_data = list(data)
    for index, value in enumerate(reversed(temp_data)):
        # Because the index
        print(f"Index: {index} Value: {value}")
        if value > max_val or value < min_val:
            print(f"Top Index: {top_index}, {value}")
            print(f"Top Index: ({top_index} - {index} = {top_index-index}) ")
            del temp_data[top_index-index]
    return temp_data

cleaned_data2 = cleanvalues2(data)  # Does not change original data
clean_values(data)                   # Changes original data.
