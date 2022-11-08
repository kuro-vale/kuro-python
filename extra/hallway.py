# This program count the number of greetings in a hallway.
# A hallway is represented like "--->---<"
# - are empty spaces
# > is an employee walking to the right
# < is an employee walking to the left
# Each employee salute each other in front of him
def count_greetings(s):
    greetings = 0
    for i in range(len(s)):
        if s[i] == ">":
            for j in range(i + 1, len(s)):
                if s[j] == "<":
                    greetings += 1
        if s[i] == "<":
            for j in range(i):
                if s[j] == ">":
                    greetings += 1

    return greetings


if __name__ == '__main__':
    print(count_greetings(">->-<"))  # 4
    print(count_greetings("><><"))  # 6
    print(count_greetings("><><><"))  # 12
    print(count_greetings(">><><"))  # 10
    print(count_greetings(">><><><"))  # 18
