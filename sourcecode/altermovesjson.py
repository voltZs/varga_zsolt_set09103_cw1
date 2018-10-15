import json

with open("moves.json", "r") as read_file:
    moves = json.load(read_file)

new_moveslist = []

for move in range(1,152):
    move_obj = {}
    move = str(move)
    move_obj["num"] = move
    move_obj["name"] = moves[move]["name"]
    move_obj["type"] = moves[move]["type"]
    move_obj["category"] = moves[move]["category"]
    move_obj["description"] = moves[move]["description"]
    move_obj["pp"] = moves[move]["pp"]
    move_obj["accuracy"] = moves[move]["accuracy"]
    new_moveslist.append(move_obj)

with open("moves_updated.json", "w") as write_file:
    json.dump(new_moveslist, write_file)
