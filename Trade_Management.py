def trade_management(Item_to_get_from_trade, Inventory_buffer):
    Tradeable_items = [
                        [Items.Carrot_seed, [ 
                                              [Items.Hay, Items.Wood], 
                                              [12, 12] 
                                            ] 
                        ],
                        [Items.Empty_Tank, [ 
                                              [Items.Wood], 
                                              [5] 
                                            ] 
                        ],
                        [Items.Fertilizer, [ 
                                              [Items.Pumpkin], 
                                              [10] 
                                            ] 
                        ],
                        [Items.Pumpkin_Seed, [ 
                                              [Items.Carrot], 
                                              [10] 
                                            ] 
                        ],
                        [Items.Sunflower_Seed, [ 
                                              [Items.Carrot], 
                                              [6] 
                                            ] 
                        ]
                      ]
    for Trade_option in Tradeable_items:
        if Trade_option[0]==Item_to_get_from_trade:
            for Item_cost_ID in range(0, len(Trade_option[1])-1):
                if num_items(Trade_option[1][0][Item_cost_ID]) < Inventory_buffer*Trade_option[1][1][Item_cost_ID]:
                    Farm_to_trade(Trade_option[1][0][Item_cost_ID], (Inventory_buffer*Trade_option[1][1][Item_cost_ID]))
    trade(Item_to_get_from_trade, Inventory_buffer)

def Farm_to_trade(Item_to_farm_for_trade, Amount):
    if Item_to_farm_for_trade == Items.Pumpkin:
        Farm_pumpkins(Amount)
    else:
        Farm_carrots_wood_hay(Item_to_farm_for_trade, Amount)
    
    