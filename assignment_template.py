"""
This is the assignment template for the COMP1730/COMP6730 major assignment
for Semester 1, 2021.

The assignment is due at 9:00am on Monday 24 May.

Please include the student IDs of all members of your group here
Student Ids:
"""


import csv
import math

# Question 1:
def read_dataset(file):
    dam_file = open (file, mode = "r")
    file_reader = csv.reader (dam_file)
    table = [row for row in file_reader]
    dam_file.close ()
    
    file_data = []
    for row in table:
        file_data.append([float(element) for element in row])
    
    return file_data
        
data_small = read_dataset("elevation_data_small.csv")


# Question 2:
def minimum_elevation(data_set):
    
    min_elevation = 1000
    
    for i in range (len (data_set)):
        if min (data_set [i]) < min_elevation:
            min_elevation = min (data_set [i])
            
    return min_elevation

def maximum_elevation(data_set):
    
    max_elevation = 0
    
    for i in range (len (data_set)):
        if max (data_set [i]) > max_elevation:
            max_elevation = max (data_set [i])
            
    return max_elevation

def average_elevation(data_set):
    
    total_sum = 0
    
    for i in data_set:
        total_sum += sum (i)
        
    total_elevation_num = len (data_set) * len (data_set [0])
    
    avg_elevation = total_sum / total_elevation_num
    
    return avg_elevation


# Question 3
def slope(data_set, x_coordinate, y_coordinate):
    
    if x_coordinate == 0:
        horizontal_difference = (data_set [y_coordinate] [1] - 
                                 data_set [y_coordinate] [0]) / 10
    elif x_coordinate == len(data_set[0])-1:
        horizontal_difference = (data_set [y_coordinate] [x_coordinate]- 
                                 data_set [y_coordinate] [x_coordinate-1]) / 10
    else:
        horizontal_difference = (data_set [y_coordinate] [x_coordinate+1]- 
                                 data_set [y_coordinate] [x_coordinate-1]) / 10
        
    if y_coordinate == 0:
        vertical_difference = (data_set [1] [x_coordinate] - 
                               data_set [0] [x_coordinate]) / 10
    elif y_coordinate == len(data_set)-1:
        vertical_difference = (data_set [y_coordinate] [x_coordinate]- 
                               data_set [y_coordinate-1] [x_coordinate]) / 10
    else:
        vertical_difference = (data_set [y_coordinate+1] [x_coordinate]- 
                               data_set [y_coordinate-1] [x_coordinate]) / 10
        
    slope = math.sqrt ((horizontal_difference**2) + (vertical_difference**2))
    
    return slope


# Question 4
def surface_area (data_set, x_coordinate, y_coordinate):
    
    sf_area = 0
    
    tolerance_level = 0.5
    
    reference_height = data_set [y_coordinate] [x_coordinate] + tolerance_level
    
    inf = left_most_column(data_set, x_coordinate, reference_height)
    sup = right_most_column(data_set, x_coordinate, reference_height)
    
    origin_row_length = row_length (data_set [y_coordinate], reference_height,
                        inf, sup)

    up_num = y_coordinate
    
    while up_num >= 0 and origin_row_length != 0:
        current_row_length = row_length (data_set [up_num], reference_height,
                                inf, sup)
        sf_area += (current_row_length + origin_row_length) / 2 * 25
        origin_row_length = current_row_length
        
        up_num = up_num - 1
    
    origin_row_length = row_length (data_set [y_coordinate], reference_height,
                        inf, sup)
    
    down_num = y_coordinate
    
    while down_num < len (data_set) and origin_row_length != 0:
        current_row_length = row_length (data_set [down_num], reference_height,
                                inf, sup)
        sf_area += (current_row_length + origin_row_length) / 2 * 25
        origin_row_length = current_row_length
        
        down_num += 1
        
    return sf_area
        

def row_length (row, reference_height, inf, sup):
    
    length = 0
    last_point = False
    
    for i in range (inf, sup):
        
        if row [i] <= reference_height:
            if last_point == True:
                length += 1
            else: last_point = True
        
        else: last_point = False
    
    return length
                
    
def left_most_column (data_set, x_coordinate, reference_height):
    
    inf = x_coordinate
    case = True
    
    while inf >= 0 and case:
        
        for i in range (len (data_set)):
            if data_set [i] [inf] <= reference_height:
                case = True
                break
            case = False
        
        inf = inf - 1
    
    inf += 1
            
    return inf
            
        

def right_most_column (data_set, x_coordinate, reference_height):
    
    sup = x_coordinate
    case = True
    
    while sup < len (data_set [0]) and case:
        
        for i in range (len (data_set)):
            if data_set [i] [sup] <= reference_height:
                case = True
                break
            case = False
        
        sup += 1
            
    return sup
    

def surface_area(data_set, x_coordinate, y_coordinate):
    sf_area = 0
    origin_row_length = row_length (data_set [0], 
                        data_set [y_coordinate] [x_coordinate])
    current_row_length = 0
    
    for i in range (1, (len (data_set) - 1)):
        current_row_length = row_length (data_set [i], 
                                data_set [y_coordinate] [x_coordinate])
        if origin_row_length != 0:
            sf_area += (current_row_length + origin_row_length) / 2 * 25
        origin_row_length = current_row_length
        
    return sf_area


# Question 5:
def expanded_surface_area(data_set, water_level, x_coordinate, y_coordinate):
    
    expanded_area = 0

    inf = left_most_column(data_set, x_coordinate, water_level)
    sup = right_most_column(data_set, x_coordinate, water_level)
    
    origin_row_length = row_length (data_set [y_coordinate], water_level,
                        inf, sup)
    current_row_length = 0

    up_num = y_coordinate
    
    while up_num >= 0 and origin_row_length != 0:
        current_row_length = row_length (data_set [up_num], water_level,
                                inf, sup)
        expanded_area += (current_row_length + origin_row_length) / 2 * 25
        origin_row_length = current_row_length
        
        up_num = up_num - 1
    
    origin_row_length = row_length (data_set [y_coordinate], water_level,
                        inf, sup)
    
    down_num = y_coordinate
    
    while down_num < len (data_set) and origin_row_length != 0:
        current_row_length = row_length (data_set [down_num], water_level,
                                inf, sup)
        expanded_area += (current_row_length + origin_row_length) / 2 * 25
        origin_row_length = current_row_length
        
        down_num += 1
        
    return expanded_area


# Question 6:
def impute_missing_values(data_set):
    
    new_data_set = []
    
    for i in range (len (data_set)):
        
        new_row = []
        
        for j in range (len (data_set [i])):
            
            if data_set [i] [j] < -1:                               
                if i == 0:
                    new_data = (data_set [i+1] [j] + data_set [i] [j+1] + 
                                data_set [i] [j-1]) / 3
                elif i == len (data_set) - 1:
                    new_data = (data_set [i-1] [j] + data_set [i] [j+1] + 
                                data_set [i] [j-1]) / 3
                elif j == 0:
                    new_data = (data_set [i+1] [j] + data_set [i-1] [j] +
                                data_set [i] [j+1]) / 3
                elif j == len (data_set [i]) - 1:
                    new_data = (data_set [i+1] [j] + data_set [i-1] [j] +
                                data_set [i] [j-1]) / 3
                else: 
                    data_around = [data_set [i+1] [j], data_set [i-1] [j],
                                data_set [i] [j+1], data_set [i] [j-1]]
                    for dt in data_around:
                        if dt < -1:
                            data_around.remove (dt)                            
                    new_data = sum (data_around) / len (data_around)
                          
            else:
                new_data = data_set [i] [j]
                
            new_row.append(new_data)
            
        new_data_set.append(new_row)
        
    return new_data_set

def insert_correct_data (new_file):
    dam_file = open (new_file, mode = "w")
    content = csv.writer(dam_file)
    
    data_large = read_dataset("elevation_data_large.csv")
    new_data_large = impute_missing_values (data_large)
    
    content.writerows (new_data_large)
    dam_file.close()
    
data_large = read_dataset("elevation_data_large.csv")

# You'll need to decide what other functions you want for Question 6
# It should be clear from your code, what we need to do in order to produce the plot(s).


# Code in the following if statement will only be executed when this file is run - not when it is imported.
# If you want to use any of your functions (such as to answer questions) please write the code to
# do so inside this if statement. We'll cover it in more detail in an upcoming lecture.
if __name__ == "__main__":
    print (impute_missing_values (data_large) [0])
    print (impute_missing_values (data_large) [1])
    print (len(data_large))
    print (len(impute_missing_values (data_large)))