highest_num_Petals_Measured = 15
list_of_powers_on_field = []
list_of_highest_Power_Locations = {}
for i in range(0,get_pos_x()):
    move(West)
for i in range(0,get_pos_y()):
    move(South)
def measure_Sunflowers_on_field():
    for i in range(0,get_pos_x()):
        move(West)
    for i in range(0,get_pos_y()):
        move(South)
    list_of_powers_on_field = []
    list_of_highest_Power_Locations = {}
    for i in range(0,get_world_size()):
        for j in range(0,get_world_size()):
            move(North)
            if (get_pos_y()-1) % 3 == 0 or (get_world_size()-1 == get_pos_y()):
                if measure() != None:
                    if measure() not in list_of_powers_on_field:
                        list_of_powers_on_field.append(measure())
                    if measure() not in list_of_highest_Power_Locations:
                        list_of_highest_Power_Locations[measure()] = [[get_pos_x(),get_pos_y()]]
                    else:
                        list_of_highest_Power_Locations[measure()].append([get_pos_x(),get_pos_y()])
                if measure(North) != None and (get_world_size()-1 != get_pos_y()):
                    if measure(North) not in list_of_powers_on_field:
                        list_of_powers_on_field.append(measure(North))
                    if measure(North) not in list_of_highest_Power_Locations:
                        list_of_highest_Power_Locations[measure(North)] = [[get_pos_x(),get_pos_y()+1]]
                    else:
                        list_of_highest_Power_Locations[measure(North)].append([get_pos_x(),get_pos_y()+1])
                if measure(South) != None and (get_pos_y() != 0):
                    if measure(South) not in list_of_powers_on_field:
                        list_of_powers_on_field.append(measure(South))
                    if measure(South) not in list_of_highest_Power_Locations:
                        list_of_highest_Power_Locations[measure(South)] = [[get_pos_x(),get_pos_y()-1]]
                    else:
                        list_of_highest_Power_Locations[measure(South)].append([get_pos_x(),get_pos_y()-1])
        move(East)
    return list_of_powers_on_field,list_of_highest_Power_Locations
list_of_powers_on_field,list_of_highest_Power_Locations = measure_Sunflowers_on_field()
quick_print(list_of_powers_on_field)
quick_print(list_of_highest_Power_Locations)
highest_num_Petals_Measured = max(list_of_powers_on_field)
for k in range(0,len(list_of_highest_Power_Locations)):
    temp = list_of_highest_Power_Locations[highest_num_Petals_Measured]
    for j in temp:
        while (get_pos_x() != j[0] or get_pos_y()!=j[1]):
            if get_pos_x() < j[0]:
                move(East)
            elif get_pos_x() > j[0]:
                move(West)
            if get_pos_y() < j[1]:
                move(North)
            elif get_pos_y() > j[1]:
                move(South) 
        while measure() >= highest_num_Petals_Measured: 
            harvest()
            if num_items(Items.Sunflower_Seed) < 2:
                trade_management(Items.Sunflower_Seed, (get_world_size()**2)*100)
                return
            while can_harvest()==False:
                plant(Entities.Sunflower)
        list_of_highest_Power_Locations[measure()].append([get_pos_x(),get_pos_y()])
    list_of_highest_Power_Locations[highest_num_Petals_Measured] = []
    for j in range(0,len(list_of_powers_on_field)):
        if list_of_powers_on_field[j] == highest_num_Petals_Measured:
            list_of_powers_on_field[j] = 0
    highest_num_Petals_Measured = max(list_of_powers_on_field)
    quick_print(list_of_powers_on_field)
    quick_print(list_of_highest_Power_Locations)
for i in range(0,get_pos_x()):
    move(West)
for i in range(0,get_pos_y()):
    move(South)
for i in range(0,get_world_size()):
    for j in range(0,get_world_size()):
        move(North)
        if (get_pos_y()-1) % 3 == 0 or (get_world_size()-1 == get_pos_y()):
            if measure() != None:
                if measure() not in list_of_powers_on_field:
                    list_of_powers_on_field.append(measure())
                if measure() not in list_of_highest_Power_Locations:
                    list_of_highest_Power_Locations[measure()] = [[get_pos_x(),get_pos_y()]]
                else:
                    list_of_highest_Power_Locations[measure()].append([get_pos_x(),get_pos_y()])
            if measure(North) != None and (get_world_size()-1 != get_pos_y()):
                if measure(North) not in list_of_powers_on_field:
                    list_of_powers_on_field.append(measure(North))
                if measure(North) not in list_of_highest_Power_Locations:
                    list_of_highest_Power_Locations[measure(North)] = [[get_pos_x(),get_pos_y()+1]]
                else:
                    list_of_highest_Power_Locations[measure(North)].append([get_pos_x(),get_pos_y()+1])
            if measure(South) != None and (get_pos_y() != 0):
                if measure(South) not in list_of_powers_on_field:
                    list_of_powers_on_field.append(measure(South))
                if measure(South) not in list_of_highest_Power_Locations:
                    list_of_highest_Power_Locations[measure(South)] = [[get_pos_x(),get_pos_y()-1]]
                else:
                    list_of_highest_Power_Locations[measure(South)].append([get_pos_x(),get_pos_y()-1])
    move(East)
quick_print(list_of_powers_on_field)
quick_print(list_of_highest_Power_Locations)