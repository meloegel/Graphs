from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

def turnAround(dir):
    if dir == 'n':
        return 's'
    if dir == 's':
        return 'n'
    if dir == 'w':
        return 'e'
    if dir == 'e':
        return 'w'

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

s = Stack()

while len(visited_rooms) < len(world.rooms):
    exits = player.current_room.get_exits()
    moveOptions = []
    for x in exits:
        if x is not None and player.current_room.get_room_in_direction(x) not in visited_rooms:
            moveOptions.append(x)
    visited_rooms.add(player.current_room)
    if len(moveOptions) > 0:
        move = random.randint(0, len(moveOptions) - 1)
        s.push(moveOptions[move])
        player.travel(moveOptions[move])
        traversal_path.append(moveOptions[move])
    else:
        last_move = s.pop()
        player.travel(turnAround(last_move))
        traversal_path.append(turnAround(last_move))



for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
