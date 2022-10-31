# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/python

def warn_the_sheep(queue):
    queue.reverse()
    if queue[0] == "wolf":
        return "Pls go away and stop eating my sheep"
    for i in range(len(queue)):
        if queue[i] == "wolf":
            return f"Oi! Sheep number {i}! You are about to be eaten by a wolf!"
