#Get_Treasure(-1) # do infinite runs
clear()
n = 1
upgrade_multiplier = 5 # max multiplier is 500%
amount_of_treasure_each_full_run = (get_world_size()**2)*300*upgrade_multiplier
Get_Treasure((num_items(Items.Gold) + (amount_of_treasure_each_full_run * n) - 1)) # do only n runs

def Get_Treasure(Amount):
    completed_runs = 0
    total_time_passed = 0
    while (num_items(Items.Gold)<Amount or Amount==-1):
        start_time = get_time()
        StartMaze()
        Amount_of_operations = get_op_count()
        stop_time = get_time()
        time_to_completion = stop_time - start_time
        total_time_passed += time_to_completion
        completed_runs += 1
        average_time_of_completions = total_time_passed / completed_runs
        quick_print("Previous full maze run time to complete: ", time_to_completion)
        quick_print("Average time to complete each full maze run: ", average_time_of_completions)
        quick_print("Total full maze run time: ", total_time_passed)
        quick_print("Total full maze operational cost: ", Amount_of_operations)

def WallsandPathsAtCurrentPOS(Current_Node):
    Current_POS = [get_pos_x(), get_pos_y()]
    Cardinal_Directions = [North,East,South,West]
    List_of_no_walls = Current_Node[2][1]
    List_of_Blocked_Paths = Current_Node[3] 
    for i in range(0,len(Cardinal_Directions)):
        if Cardinal_Directions[i] not in Current_Node[2][1]:
            if move(Cardinal_Directions[i]):
                List_of_no_walls.append(Cardinal_Directions[i])
                List_of_Blocked_Paths.append(0)
                if i<2:
                    move(Cardinal_Directions[i+2])
                else:
                    move(Cardinal_Directions[i-2])
    Current_Node = [get_pos_x(), get_pos_y(), DetermineForks_and_corners(List_of_no_walls), List_of_Blocked_Paths]
    return Current_Node

def DetermineForks_and_corners(List_of_no_walls):
    if len(List_of_no_walls)<3:
        if (North in List_of_no_walls or South in List_of_no_walls) and (East in List_of_no_walls or West in List_of_no_walls):
            return [-1, List_of_no_walls]
        return [0,List_of_no_walls]
    else:
        return [1, List_of_no_walls]

def Navigate_Maze(World_Grid,Chest_Location,completed_runs):
    Prev_direction = None
    if get_entity_type()==Entities.Treasure:
        return World_Grid
    while True:
        Current_POS_Num = get_pos_x()+(get_pos_y()*get_world_size())
        if World_Grid[Current_POS_Num] == [None,None,[None, []],[]]:
            World_Grid[Current_POS_Num] = WallsandPathsAtCurrentPOS(World_Grid[Current_POS_Num])
        else:
            Current_Node = World_Grid[Current_POS_Num]
            if Prev_direction == None:
                random_direction = random() * len(Current_Node[2][1]) // 1
                Prev_direction = Current_Node[2][1][random_direction]
                move(Prev_direction)
            while True:
                if Prev_direction == North:
                    Opposite_Prev_direction = South
                elif Prev_direction == South:
                    Opposite_Prev_direction = North
                elif Prev_direction == West:
                    Opposite_Prev_direction = East
                elif Prev_direction == East:
                    Opposite_Prev_direction = West
                Current_POS_Num = get_pos_x()+(get_pos_y()*get_world_size())
                if get_entity_type()==Entities.Treasure:
                    return World_Grid
                World_Grid[Current_POS_Num] = WallsandPathsAtCurrentPOS(World_Grid[Current_POS_Num])
                Current_Node = World_Grid[Current_POS_Num]
                if Current_Node[2][0] == 0:
                    if move(Prev_direction) == False:
                        move(Current_Node[2][1][0])
                        Prev_direction = Current_Node[2][1][0]
                elif Current_Node[2][0] == -1:
                    for i in Current_Node[2][1]:
                        if (Prev_direction in [North, South]) and (i in [East, West]):
                            move(i)
                            Prev_direction = i
                            break
                        elif (Prev_direction in [East, West]) and (i in [North, South]):
                            move(i)
                            Prev_direction = i
                            break
                elif Current_Node[2][0] == 1:
                    List_of_Open_Paths = calculate_list_of_paths(Current_Node,Opposite_Prev_direction,Chest_Location)
                    if completed_runs < 00:
                        List_of_Open_Path = depth_search(List_of_Open_Path,World_Grid,Chest_Location)
                    for Path_to_move in List_of_Open_Paths:
                        if (Current_Node[3][Path_to_move[1]]<2):
                            move(Path_to_move[0])
                            Current_Node[3][Path_to_move[1]] += 1
                            Prev_direction = Path_to_move[0]
                            break
                        else:
                            move(Path_to_move[0])
                            Current_Node[3][Path_to_move[1]] += 1
                            Prev_direction = Path_to_move[0]
                            break

def calculate_list_of_paths(Current_Node,Opposite_Prev_direction,Chest_Location):
    List_of_Open_Paths = []
    Desired_direction = []
    if Chest_Location != [-1,-1]:
        if get_pos_x() < Chest_Location[0]:
            Desired_direction.append(East)
        elif get_pos_x() > Chest_Location[0]:
            Desired_direction.append(West)
        if get_pos_y() < Chest_Location[1]:
            Desired_direction.append(North)
        elif get_pos_y() > Chest_Location[1]:
            Desired_direction.append(South)
    for i in range(0,len(Current_Node[2][1])):
        Path_to_consider = Current_Node[2][1][i]
        if Path_to_consider == Opposite_Prev_direction and Current_Node[3][i] != 2:
            Current_Node[3][i] += 1
        if Current_Node[3][i] < 2 and Path_to_consider in Desired_direction:
            if len(List_of_Open_Paths) == 0:
                List_of_Open_Paths.append([Path_to_consider,i])
            elif Current_Node[3][i] > Current_Node[3][List_of_Open_Paths[0][1]]:
                List_of_Open_Paths.append([Path_to_consider,i])
            else:
                List_of_Open_Paths.insert(0,[Path_to_consider,i])
    for i in range(0,len(Current_Node[2][1])):
        Path_to_consider = Current_Node[2][1][i]
        if Current_Node[3][i] < 2 and Path_to_consider not in Desired_direction:
            List_of_Open_Paths.append([Path_to_consider,i])
    if len(List_of_Open_Paths)==0:
        for i in range(0,len(Current_Node[2][1])):
            if Current_Node[3][i] >= 2:
                Current_Node[3][i] = 1
            if Current_Node[2][1][i] != Opposite_Prev_direction:
                Path_to_consider = Current_Node[2][1][i]
                List_of_Open_Paths.insert(random() * len(List_of_Open_Paths) // 1,[Path_to_consider,i])
    return List_of_Open_Paths

def depth_search(List_of_Open_Path,World_Grid):
    measure()
    Current_POS_Num = get_pos_x()+(get_pos_y()*get_world_size())
    Current_Node = World_Grid[Current_POS_Num]
    for paths in List_of_Open_Path:
        measure()

def Create_Grid():
    World_Grid = []
    for i in range(0,get_world_size()**2):
        World_Grid.append([None,None,[None, []],[]])
    return World_Grid

def StartMaze():
    completed_runs = 0
    total_time_passed = 0
    start_time = get_time()
    #start Chest_Location at center of world because it is unknown
    Chest_Location = [-1,-1]
    if num_items(Items.Fertilizer) < 1000:
        trade_management(Items.Fertilizer, 1000-num_items(Items.Fertilizer))
    entity_type = get_entity_type()
    if entity_type not in [Entities.Hedge,Entities.Treasure]:
        clear()
        plant(Entities.Bush)
        while get_entity_type()==Entities.Bush:
            use_item(Items.Fertilizer)
    World_Grid = Create_Grid()
    while True:
        completed_runs += 1
        if get_entity_type()!=Entities.Treasure:
            World_Grid = Navigate_Maze(World_Grid,Chest_Location,completed_runs)
            for Positions in World_Grid:
                if Positions != [None,None,[None, [None]],[]]:
                    for i in range(0,len(Positions[2][1])):
                        Positions[3][i] = 1
        stop_time = get_time()
        time_to_completion = stop_time - start_time
        total_time_passed += time_to_completion
        average_time_of_completions = total_time_passed / completed_runs
        quick_print("Previous run's time to complete: ", time_to_completion)
        quick_print("Average time to complete each run: ", average_time_of_completions)
        quick_print("Total run time: ", total_time_passed)
        if measure() != None and num_items(Items.Fertilizer) > 1:
            Chest_Location = [measure()[0], measure()[1]]
            while num_items(Items.Fertilizer) > 1:
                if get_entity_type()==Entities.Treasure:
                    use_item(Items.Fertilizer)
                else:
                    break
        else:
            harvest()
            break
        start_time = get_time()
