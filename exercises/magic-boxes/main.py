NR_BOXES = 42
# If the first is ALICE,  The second is BOB and alice just takes and bob gives
# {
#     "ALICE": "takes",
#     "BOB": "gives"
# }
# constrains only 2 keys and only two unique values(actions) "takes" and "gives"
ACTIONS = ["takes", "gives"]
ACTORS = dict()  # {}
BOX = dict()
FILE_PATH = "actions-fail_carl.txt"

# {

# }



def check_actions(file_path):
    line_nr = 0  # line number
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip() 
            if not line:
                continue
            print(f"Line {line_nr}: --> {line}")
            actor, action, _, object = line.split(" ")
            if action not in ACTIONS:
                print(f"Error: {action} is not a valid action on line {line_nr}")
                return False

            actor_action = ACTORS.get(actor)  #  ACTORS dict firstly is empty
            if actor_action is None and len(ACTORS.keys()) < 2:
                stored_action = ACTORS.values()
                if action in stored_action:
                    print(f"Error: {actor} is not a valid actor on line {line_nr}")
                    return False
                ACTORS[actor] = action
                actor_action = action
            if actor_action is None and len(ACTORS.keys()) >= 2:
                print(f"Error: {actor} is not a valid actor on line {line_nr}")
                return False

            if actor_action is not None and actor_action != action:
                print(f"Error: {actor} is not a valid actor on line {line_nr}")
                return False

            box_length = len(BOX.keys())
            if actor_action == "gives":
                object_stored_nr = BOX.get(
                    object
                )  # BOX[object]   throws an error if object is not in the dictionary but BOX.get(object) returns None
                if object_stored_nr is None and box_length < NR_BOXES:
                    BOX[object] = 1

                if object_stored_nr is None and box_length >= NR_BOXES:
                    # print(BOX)
                    # print(box_length)
                    # print(f"Error: No more space in the box for {object} on line {line_nr}") 
                    return False

                if object_stored_nr is not None:
                    BOX[object] += 1
            if actor_action == "takes":
                object_stored_nr = BOX.get(object)
                if object_stored_nr is None:
                    print(f"Error: {object} does not exist in boxes on {line_nr}")
                    return False
                BOX[object] -= 1
                if BOX[object] == 0:
                    del BOX[object]

            line_nr += 1
    return True


def main():
    isOk = check_actions(FILE_PATH)
    if isOk:
        print("All actions are valid")
    else:
        print("Actions are not valid")  
    pass


"""
Before ACTORS dict is empty and BOX dict is empty  like ACTORS={} and BOX={}    

Bob gives a APPLE   -> actor = Bob, action = gives, object = APPLE   check if action is in ACTIONS list and
does bob have an action in ACTORS dict?  Does the ACTORS dict length is less than 2?   
Bob gives a BANANA
Bob gives a APPLE
Carl takes a BANANA
Bob gives a CHERR  
    
"""


if __name__ == "__main__":
    main()
