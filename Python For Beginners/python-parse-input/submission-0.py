from typing import List

def read_integers() -> List[int]:
    user = input()
    my_list = [int(x) for x in user.split(",")]
    return my_list
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
