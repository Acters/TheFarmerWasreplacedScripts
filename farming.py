def Farm_all_in_one(plant_to_plant,failed_watering):
    if plant_to_plant == Entities.Grass:
        if get_ground_type() == Grounds.Soil:
            till()
        if can_harvest():
            harvest()
        return failed_watering
    if can_harvest():
        if get_entity_type() != Entities.Grass:
            failed_watering += Use_Water_Tank()
        harvest()
    if plant_to_plant == Entities.Carrots:
        if num_items(Items.Carrot_Seed) < 1:
            trade_management(Items.Carrot_Seed, get_world_size()**2)
        if get_ground_type() != Grounds.Soil:
            till()
    plant(plant_to_plant)
    return failed_watering
