while True:
    clear()
    plant_SunFlowers()
    harvest_sunflower_power()

def harvest_sunflower_power():
    highest_num_Petals_Measured = 15
    list_of_powers_on_field = []
    list_of_highest_Power_Locations = []
    for x in range(0,15+2):
        list_of_highest_Power_Locations.append([])
    while True:
        for i in range(0,get_world_size()):
            for j in range(0,get_world_size()):
                move(North)
                if (get_pos_y()-1) % 3 == 0 or (get_world_size()-1 == get_pos_y()):
                    if measure() != None:
                        if measure() not in list_of_powers_on_field:
                            list_of_powers_on_field.append(measure())
                        list_of_highest_Power_Locations[measure()].append([get_pos_x(),get_pos_y()])
                    if measure(North) != None and (get_world_size()-1 != get_pos_y()):
                        if measure(North) not in list_of_powers_on_field:
                            list_of_powers_on_field.append(measure(North))
                        list_of_highest_Power_Locations[measure(North)].append([get_pos_x(),get_pos_y()+1])
                    if measure(South) != None and (get_pos_y() != 0):
                        if measure(South) not in list_of_powers_on_field:
                            list_of_powers_on_field.append(measure(South))
                        list_of_highest_Power_Locations[measure(South)].append([get_pos_x(),get_pos_y()-1])
            move(East)
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
                        trade_management(Items.Sunflower_Seed, (get_world_size()**2)*10)
                        return
                    while can_harvest()==False:
                        if get_entity_type() != Entities.Sunflower:
                            plant(Entities.Sunflower)
                            if len(temp) < get_world_size()**2:
                                if Use_Water_Tank() == 1:
                                    return
                        if num_items(Items.Fertilizer) > 0:
                            use_item(Items.Fertilizer)
                        else:
                            trade_management(Items.Sunflower_Seed, (get_world_size()**2)*100)
                            return
                list_of_highest_Power_Locations[measure()].append([get_pos_x(),get_pos_y()])
            list_of_highest_Power_Locations[highest_num_Petals_Measured] = []
            for j in range(0,len(list_of_powers_on_field)):
                if list_of_powers_on_field[j] == highest_num_Petals_Measured:
                    list_of_powers_on_field[j] = 0
            highest_num_Petals_Measured = max(list_of_powers_on_field)
        temp = {}
        for i in range(0,get_pos_x()):
            move(West)
        for i in range(0,get_pos_y()):
            move(South)
        highest_num_Petals_Measured = max(list_of_powers_on_field)
        if highest_num_Petals_Measured == 0:
            plant_SunFlowers()
            list_of_powers_on_field = []
            highest_num_Petals_Measured = 15
            list_of_highest_Power_Locations = []
            for x in range(0,15+2):
                list_of_highest_Power_Locations.append([])
       
def plant_SunFlowers():
    failed_watering=0
    if num_items(Items.Fertilizer) != get_world_size()**2*10:
        trade_management(Items.Fertilizer, (get_world_size()**2)*100)
    for i in range(0,get_world_size()):
        for j in range(0,get_world_size()):
            if num_items(Items.Sunflower_Seed) < 1:
                trade_management(Items.Sunflower_Seed, (get_world_size()**2)*100)
            if get_ground_type() != Grounds.Soil:
                till()
            if plant(Entities.Sunflower):
                failed_watering += Use_Water_Tank()
                failed_watering += Use_Water_Tank()
            move(North)
        move(East)
    get_more_tanks(failed_watering)
