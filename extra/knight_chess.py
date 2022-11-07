# Find minimum steps to reach destiny with a horse in chess
# Chessboard numeration is like below:
# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------
def min_moves_to_reach_dest(src, dest):
    # All possible movements for the knight
    ky = [2, 2, -2, -2, 1, 1, -1, -1]
    kx = [1, -1, 1, -1, 2, -2, 2, -2]
    # Generate Chessboard
    chessboard = [[i + j * 8 for i in range(8)] for j in range(8)]
    src_y, src_x = get_y_and_x(chessboard, src)
    dest_y, dest_x = get_y_and_x(chessboard, dest)
    # Save visited positions
    visited = [[False for _ in range(8)] for _ in range(8)]
    visited[src_y][src_x] = True
    # Save registry of all traces
    all_traces = [Trace(src_y, src_x), ]
    while len(all_traces) > 0:
        current_trace = all_traces[0]
        all_traces.pop(0)

        # Return fastest trace
        if current_trace.y == dest_y and current_trace.x == dest_x:
            return current_trace.moves

        # Append all possible moves to trace list
        for i in range(8):
            y = current_trace.y + ky[i]
            x = current_trace.x + kx[i]
            if is_inside(y, x) and not visited[y][x]:
                visited[y][x] = True
                all_traces.append(Trace(y, x, current_trace.moves + 1))


def get_y_and_x(chessboard, position):
    x, y = 0, 0
    for i in chessboard:
        try:
            x = i.index(position)
            y = chessboard.index(i)
        except ValueError:
            pass
    return x, y


def is_inside(y, x):
    if 0 <= y <= 7 and 0 <= x <= 7:
        return True
    return False


class Trace:
    def __init__(self, y, x, moves=0):
        self.y = y
        self.x = x
        self.moves = moves


if __name__ == '__main__':
    print(min_moves_to_reach_dest(0, 1))
    print(min_moves_to_reach_dest(19, 36))
    print(min_moves_to_reach_dest(25, 20))
    print(min_moves_to_reach_dest(0, 63))
