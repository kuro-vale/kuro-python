# https://www.codewars.com/kata/5bb904724c47249b10000131/python

def points(games):
    team_points = 0
    for i in range(len(games)):
        match = games[i].split(':')
        if match[0] > match[1]:
            team_points += 3
        elif match[0] == match[1]:
            team_points += 1
    return team_points
