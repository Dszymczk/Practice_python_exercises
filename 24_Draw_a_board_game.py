def draw_a_board(x, y):
    print(" " + y * "--- ")
    if x == 0 or y == 0:
        return " X and Y can not be 0"
    for i in range(x):
        print("|" + y * "   |")
        print(" " + y * "--- ")


if __name__ == "__main__":
    draw_a_board(4, 4)
