Get_Treasure(-1)

def Get_Treasure(Amount):
    while (num_items(Items.Gold)<Amount or Amount==-1):
        StartMaze()

def WallsandPathsAtCurrentPOS():
    Current_POS = [get_pos_x(), get_pos_y()]
    Cardinal_Directions = [North,East,South,West]
    List_of_no_walls = []
    List_of_Blocked_Paths = []
    for i in range(0,len(Cardinal_Directions)):
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

def Navigate_Maze(World_Grid,Chest_Location):
    Prev_direction = None
    if get_entity_type()==Entities.Treasure:
        return
    while True:
        Current_POS_Num = get_pos_x()+(get_pos_y()*get_world_size())
        if World_Grid[Current_POS_Num] == [None,None,[None],[]]:
            World_Grid[Current_POS_Num] = WallsandPathsAtCurrentPOS()
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
                Current_Node = World_Grid[Current_POS_Num]
                if get_entity_type()==Entities.Treasure:
                    return
                if Current_Node == [None,None,[None],[]]:
                    break
                elif Current_Node[2][0] == 0:
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
                    List_of_Open_Paths = []
                    Desired_direction = []
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
                        if Path_to_consider == Opposite_Prev_direction and 1 not in Current_Node[3] and 2 not in Current_Node[3]:
                            Current_Node[3][i] += 1
                        if Current_Node[3][i] < 2 and Path_to_consider in Desired_direction:
                            List_of_Open_Paths.append([Path_to_consider,i])
                    for i in range(0,len(Current_Node[2][1])):
                        Path_to_consider = Current_Node[2][1][i]
                        if Path_to_consider == Opposite_Prev_direction and 1 not in Current_Node[3] and 2 not in Current_Node[3]:
                            Current_Node[3][i] += 1
                        if Current_Node[3][i] < 2 and Path_to_consider not in Desired_direction:
                            List_of_Open_Paths.append([Path_to_consider,i])
                    if len(List_of_Open_Paths)==0:
                        for i in range(0,len(Current_Node[2][1])):
                            Path_to_consider = Current_Node[2][1][i]
                            Current_Node[3][i] = 1
                            List_of_Open_Paths.append([Path_to_consider,i])
                        break
                    for i in range(0,len(List_of_Open_Paths)):
                        if (List_of_Open_Paths[i][0] in Desired_direction):
                            move(List_of_Open_Paths[i][0])
                            Current_Node[3][List_of_Open_Paths[i][1]] += 1
                            Prev_direction = List_of_Open_Paths[i][0]
                            break
                        elif Current_Node[3][List_of_Open_Paths[i][1]]==0:
                            move(List_of_Open_Paths[i][0])
                            Current_Node[3][List_of_Open_Paths[i][1]] += 1
                            Prev_direction = List_of_Open_Paths[i][0]
                            break
                        elif i+1==len(List_of_Open_Paths):
                            move(List_of_Open_Paths[i][0])
                            Current_Node[3][List_of_Open_Paths[i][1]] += 1
                            Prev_direction = List_of_Open_Paths[i][0]
                            break

def TravelBetweenNodes():
    measure()
    
def Create_Grid():
    World_Grid = []
    for i in range(0,get_world_size()**2):
        World_Grid.append([None,None,[None],[]])
    return World_Grid

def StartMaze():
    #start Chest_Location at center of world because it is unknown
    Chest_Location = [get_world_size()//2,get_world_size()//2]
    if num_items(Items.Fertilizer) < 1000:
        trade_management(Items.Fertilizer, 1000-num_items(Items.Fertilizer))
    if get_entity_type() != Entities.Hedge:
        clear()
        plant(Entities.Bush)
        while get_entity_type()==Entities.Bush:
            use_item(Items.Fertilizer)
    while True:
        World_Grid = Create_Grid()
        if get_entity_type()!=Entities.Treasure:
            Navigate_Maze(World_Grid,Chest_Location)
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
