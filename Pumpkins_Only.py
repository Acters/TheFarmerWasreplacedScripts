Farm_pumpkins(-1)
def Farm_pumpkins(Amount):
    clear()
    while num_items(Items.Pumpkin)<=Amount or Amount==-1:
        Farm_pumpkins_loop(Amount)

def Farm_pumpkins_loop(Amount):
    failed_watering = 0
    planted = 0
    column_planted = 0
    Desired_Fertilizer_amount = (10*get_world_size()**2)-num_items(Items.Fertilizer)
    while True:
        if num_items(Items.Pumpkin) > Amount and Amount != -1:
            clear()
            return
        if num_items(Items.Fertilizer) < (get_world_size()**2) and num_items(Items.Pumpkin)>(Desired_Fertilizer_amount*10):
            trade_management(Items.Fertilizer, Desired_Fertilizer_amount)
            clear()
            failed_watering = 0
            planted = 0
            column_planted = 0
        failed_watering = get_more_tanks(failed_watering)
        for i in range(0,get_world_size()):
            #for waterplant in range(0,10-((get_water()*10)%10)):
                #failed_watering = failed_watering + Use_Water_Tank()
            if num_items(Items.Pumpkin_Seed) < (get_world_size()**2):
                trade_management(Items.Pumpkin_Seed, (get_world_size()**2)*100)
                return
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Pumpkin)
            move(North)
        move(East)
        column_planted += 1
        if column_planted == get_world_size():
            column_planted = 0
            while True:
                for i in range(0,get_world_size()):
                    while True:
                        if can_harvest():
                            break
                        else:
                            if num_items(Items.Pumpkin_Seed) < 1:
                                break
                            if get_ground_type() != Grounds.Soil:
                                till()
                            if plant(Entities.Pumpkin) == False:
                                if num_items(Items.Fertilizer) > 1:
                                    use_item(Items.Fertilizer)
                            
                    move(North)
                move(East)
                column_planted += 1
                if column_planted == get_world_size():
                    harvest()
                    column_planted = 0
                    break
        