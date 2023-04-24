"""
A simple text-based adventure game called: Creepy House.

Available commands include:
    go <compass direction>
    take <object>
    quit
"""
# global dictionary of the movable objects in each location
items_in = {"bedroom" : ["aquarium", "bats"], 
            "hallway" : [ ], 
            "lounge" : ["stereo"]
            }

# current location: hallway, lounge or bedroom
state = "hallway"

# the objects that the player is carrying around (or "nothing").
carrying = [ ]


#####################################################
# Functions for describing the current location


def describe_bedroom():
    print("You are in a bedroom.")


def describe_hallway():
    print("You are in a dark hallway.")
    print("There is a table beside you, and a bright light to the west.")


def describe_lounge():
    print("You are in a brightly-lit lounge, with two red sofas.")


def describe():
    """Print a description of the current location."""
    if state == "hallway":
        describe_hallway()
    elif state == "lounge":
        describe_lounge()
    elif state == "bedroom":
        describe_bedroom()
    else:
        print("ERROR: unknown location: " + str(state))
    """Displays what objects in the room can be picked up"""
    moveable_obj = items_in[state]
    if moveable_obj:
        for item in items_in[state]:
            print("You can take: "+item)
    else: print("There are no moveable objects here.")


#######################################################
# Functions for moving between locations

def move_lounge(direction):
    if direction == "west":
        return "bedroom"
    elif direction == "east":
        return "hallway"
    return ""


def move_hallway(direction):
    if direction == "west":
        return "lounge"
    elif direction == "east" and carrying == "aquarium":
        return "outside"
    return ""


def move_bedroom(direction):
    if direction == "east":
        return "lounge"
    return ""


def move_cmd(direction):
    """Attempt to move in the given direction.

    This updates the 'state' variable to the new location,
    or leaves it unchanged and prints a warning if the move was not valid.
    :param direction: a compass direction, "north", "east", "south", or "west".
    :return: None
    """
    global state
    if state == "hallway":
        new_state = move_hallway(direction)
    elif state == "lounge":
        new_state = move_lounge(direction)
    elif state == "bedroom":
        new_state = move_bedroom(direction)
    else:
        print("WARNING: move_cmd sees unknown state: " + state)
        new_state = ""
    # now check to see if it was a valid move
    if new_state == "":
        print("You cannot go " + str(direction) + " from here.")
    else:
        state = new_state


#########################################################
# Functions for take, drop and inventory commands
def take_cmd(obj):
    """Try to pick up the given object.
    Most objects can only be picked up when in the correct room.
    """
    global items_in
    global state
    global carrying
    if obj in items_in[state]:
        print("You picked up: " + obj)
        carrying.append(obj)
        items_in[state].remove(obj)
    else:
        print("You cannot pick that up!")

"""Player can drop specific objects they are carrying and the object will be placed in the current room"""
def drop_cmd(obj_name):
    global carrying
    global items_in
    if obj_name in carrying:
        carrying.remove(obj_name)
        items_in[state].append(obj_name)
        print("You dropped: " + obj_name)
    elif carrying == []:
        print("Nothing to drop")
    else:
        print("Which item would you like to drop?")

"""Displays an inventory of objetcs they are currently carrying"""
def inventory_cmd():
    global carrying
    if carrying:
        print("You are currently carrying " + ", ".join(carrying))
    else:
        print("You are not carrying anything")

#########################################################
# The main loop that processes the player's input commands.
def main():
    for turn in range(20, 0, -1):
        print("")
        describe()
        cmd = input("Enter your command " + str(turn) + "> ").lower().split()
        if cmd == "quit":
            print("You gave in so easily :-(")
            break
        elif cmd[0] == "drop":
            obj_name = " ".join(cmd[1:])
            drop_cmd(obj_name)
        elif cmd[0] == "inventory":
            inventory_cmd()
        elif cmd[0] == "go":
            where = " ".join(cmd[1:])
            move_cmd(where)
            if state == "outside":
                print("You push the door open with the heavy aquarium and escape to outside!")
                break
        elif cmd[0] == "take":
            obj = " ".join(cmd[1:])
            take_cmd(obj)
        else:
            print("I do not understand '" + " ".join(cmd) + "'.  Try go/take/quit")
    print("Game over")


if __name__ == "__main__":
    main()
