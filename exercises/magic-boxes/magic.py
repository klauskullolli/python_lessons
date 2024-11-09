# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

# from pprint import pprint

NUM_MAGIC_BOXES = 42
# ACTION_FILENAME = 'actions.txt'
ACTION_FILENAME = "actions-simple.txt"
# ACTION_FILENAME = 'actions-fail_bob.txt'
# ACTION_FILENAME = 'actions-fail_carl.txt'
BOB = "Bob"
CARL = "Carl"

# declared boxes like an array[m][m] 
#  m = 42   
#  boxes = [[],[], [], [], ...., []]    

def find_box(boxes, obj):
    for index, box in enumerate(boxes):
        if obj in box:
            return index
    for index, box in enumerate(boxes):
        if not box:
            return index
    return None


def add_object(boxes, obj):
    bi = find_box(boxes, obj)
    if bi is None:
        return False
    else:
        boxes[bi].append(obj)
        return True


def remove_object(boxes, obj):
    bi = find_box(boxes, obj)
    if bi is None or not boxes[bi]:
        return False
    else:
        boxes[bi].pop()
        return True


def main():
    magic_boxes = [list() for _ in range(NUM_MAGIC_BOXES)]
    with open(ACTION_FILENAME) as action_file:
        for action in action_file:
            actor, _, _, object = action.split()
            if actor == BOB:
                feedback = add_object(magic_boxes, object)
                if not feedback:    
                    print(f"Alice cannot store a {object}!")
                    break
            elif actor == CARL:
                if not remove_object(magic_boxes, object):
                    print(f"Alice cannot give a {object}!")
                    break
            else:
                assert actor in [BOB, CARL], f"Unknown actor: {actor}"
            # pprint(magic_boxes)
        else:
            print("All ok")


if __name__ == "__main__":
    main()
    # a  = ["Alice", "gives", "a", "APPLE"]   
    # for e in a:
    #     print(e)

    # #  for index and element in a using enumerate keyword
    # for i , e in enumerate(a):
    #     print(i, e) 

    a = [] 

    if not a:  # means if is empty 
        print("Empty")  