import re

CastLocation_bound_value = "[808,92][944,250]"
Search_Position_Bound_value = '[944,103][1080,238]'
parent_bound_value = '[808,92][1080,250]'

cast_num_val = re.findall(r'\d+', CastLocation_bound_value)
print(cast_num_val)

search_num_val = re.findall(r'\d+', Search_Position_Bound_value)
print(search_num_val)

parent_num_val = re.findall(r'\d+', parent_bound_value)
print(parent_num_val)

cast_top_left_x_coordinate = cast_num_val[0]
cast_top_left_y_coordinate = cast_num_val[1]
cast_bottom_right_x_coordinate = cast_num_val[2]
cast_bottom_right_y_coordinate = cast_num_val[3]

print("cast_tl_x: ", cast_top_left_x_coordinate)
print("cast_tl_y: ", cast_top_left_y_coordinate)
print("cast_br_x: ", cast_bottom_right_x_coordinate)
print("cast_br_y: ", cast_bottom_right_y_coordinate)

search_top_left_x_coordinate = search_num_val[0]
search_top_left_y_coordinate = search_num_val[1]

print("search_tl_x: ",search_top_left_x_coordinate)
print("search_tl_y: ",search_top_left_y_coordinate)

parent_top_left_x_coordinate = parent_num_val[0]
parent_top_left_y_coordinate = parent_num_val[1]

print("parent_tl_x: ",parent_top_left_x_coordinate)
print("parent_tl_y: ",parent_top_left_y_coordinate)

if cast_top_left_x_coordinate <= parent_top_left_x_coordinate and cast_top_left_y_coordinate <= parent_top_left_y_coordinate\
        and cast_bottom_right_x_coordinate <= search_top_left_x_coordinate and cast_bottom_right_y_coordinate >= search_top_left_y_coordinate:
    print("Castg icon is within the bound value")
else:
    print("out of bound")