def get_more_tanks(failed_watering):
    if num_items(Items.Water_Tank) < 3 and num_items(Items.Wood) > (failed_watering * 100 * 5):
        trade_management(Items.Empty_Tank, failed_watering * 100)
    return 0

def Use_Water_Tank():
    if get_water() < 0.9:
        if num_items(Items.Water_Tank) > 0:
            if use_item(Items.Water_Tank):
                return 0
            else:
                get_more_tanks(1)
                return 1
    return 0