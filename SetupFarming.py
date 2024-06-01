Farm_carrots_wood_hay(None,-1)
def Farm_carrots_wood_hay(Item_to_farm_for_trade, Amount):
    if Item_to_farm_for_trade == Items.Hay:
        Plants_to_Farm = [
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass]
                         ]
    elif Item_to_farm_for_trade == Items.Wood:
        Plants_to_Farm = [
                            [Entities.Tree,Entities.Grass],
                            [Entities.Grass,Entities.Tree],
                            [Entities.Tree,Entities.Grass],
                            [Entities.Grass,Entities.Tree],
                            [Entities.Tree,Entities.Grass],
                            [Entities.Grass,Entities.Tree],
                            [Entities.Tree,Entities.Grass],
                            [Entities.Grass,Entities.Tree],
                            [Entities.Tree,Entities.Grass],
                            [Entities.Grass,Entities.Tree]
                         ]
    else:
        Item_to_farm_for_trade = Items.Carrot
        Plants_to_Farm = [
                            [Entities.Tree,Entities.Carrots],
                            [Entities.Carrots,Entities.Tree],
                            [Entities.Tree,Entities.Carrots],
                            [Entities.Carrots,Entities.Tree],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass],
                            [Entities.Grass,Entities.Grass]
                         ]
    clear()
    
    while True:
        if num_items(Item_to_farm_for_trade) > Amount and Amount != -1:
            clear()
            return
        failed_watering=0
        get_more_tanks(failed_watering)
        for j in range(0,get_world_size()):
            for i in range(0,get_world_size()):
                failed_watering = Farm_all_in_one(Plants_to_Farm[j][i%2],failed_watering)
                move(North)
            move(East)