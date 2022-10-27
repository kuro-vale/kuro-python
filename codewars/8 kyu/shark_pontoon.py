# https://www.codewars.com/kata/57e921d8b36340f1fd000059

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    for _ in range(pontoon_distance + 1):
        shark_distance -= shark_speed
        pontoon_distance -= you_speed
        if shark_distance <= 0:
            return "Shark Bait!"
        if pontoon_distance <= 0:
            return "Alive!"
          
