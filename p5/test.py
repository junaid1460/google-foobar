# working solution for 8 test cases
import math

# return mirrored targets on left right top bottom sides
def getMirroredTargets(target):
    x = target[0]
    y = target[1]
    mirrored_targets = []
    
    newx, newy = 2 * 0 - x,y
    mirrored_targets.append(( newx, newy)) # left side mirror
    mirrored_rooms[str(newx) + "_" + str(newy)] = [deltaX + newx, deltaY + newy]
    
    newx, newy = 2 * DIM[0] - x, y 
    mirrored_targets.append(( newx, newy)) # right
    mirrored_rooms[str(newx) + "_" + str(newy)] = [deltaX + newx, deltaY + newy]
    
    newx, newy = x, 2*DIM[1] - y
    mirrored_targets.append((newx, newy))
    mirrored_rooms[str(newx) + "_" + str(newy)] = [deltaX + newx, deltaY + newy]
    
    newx, newy = x, 2 * 0 - y
    mirrored_targets.append((newx, newy))
    mirrored_rooms[str(newx) + "_" + str(newy)] = [deltaX + newx, deltaY + newy]
    
    return mirrored_targets


# returns all possible mirrors of the target within a reachable distance
def getAllTargets(captain_pos, badguy_pos, distance):
    #print(getMirroredTargets(badguy_pos))
    new_targets = set()
    final_targets = set()
    new_targets.add((badguy_pos[0], badguy_pos[1]))
    #print(new_targets)
    while True:
        mirrored_targets = set()
        for target in new_targets:
            reachable_targets = getMirroredTargets(target)
            reachable_targets = set(x for x in reachable_targets  if math.hypot(x[0] - captain_pos[0], x[1] - captain_pos[1]) <= distance)
            reachable_targets -= final_targets
            mirrored_targets |= reachable_targets
        if not mirrored_targets:
                break

        final_targets |= mirrored_targets
        new_targets = mirrored_targets
        
    return final_targets


    
    

def quad(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return 1

def answer(dimensions, captain_pos, badguy_pos, distance):
    global DIM
    global mirrored_rooms
    global deltaX, deltaY
    DIM = list(dimensions)
    
    mirrored_rooms = {}
    
    deltaX = badguy_pos[0] - captain_pos[0]
    deltaY = badguy_pos[1] - captain_pos[1]

    
    possible_targets = getAllTargets(captain_pos, badguy_pos, distance)

    print possible_targets
    ds = {}
    for i in possible_targets:
        x = i[0] - captain_pos[0]
        y = i[1] - captain_pos[1]
        if quad(x,y) == 0:
            key = "undefined"
        else:
            key = str(math.atan2(x,y))
        ds[key] = True
        
    return len(ds)



dimensions = [3, 2]
captain_position = [1, 1]
badguy_position = [2, 1]
distance = 4



dimensions = [300, 275]
captain_position = [150, 150]
badguy_position = [180, 100]
distance = 500

print answer(dimensions, captain_position, badguy_position, distance)