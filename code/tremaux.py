import API
import sys

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def is_valid(x, y):
    if x < 0 or y < 0 or x >= API.mazeWidth() or y >= API.mazeHeight():
        return False
    if API.wallFront():
        return False
    cell_type = API.cell(x, y)
    if cell_type != "U":
        return False
    return True

def find_unvisited_neighbors(x, y):
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            neighbors.append((nx, ny))
    return neighbors

def find_next_move(x, y):
    neighbors = find_unvisited_neighbors(x, y)
    if not neighbors:
        # Backtrack
        API.turnLeft()
        API.turnLeft()
        API.moveForward()
        API.setColor(x, y, "B")
        return
    # Choose the first neighbor in the list
    nx, ny = neighbors[0]
    if nx > x:
        API.turnRight()
    elif nx < x:
        API.turnLeft()
    elif ny > y:
        API.moveForward()
    else:
        API.turnLeft()
        API.turnLeft()
        API.moveForward()
    API.setColor(nx, ny, "V")
    find_next_move(nx, ny)

def main():
    # Initialiser la couleur et le texte de la première cellule
    API.setColor(0, 0, "V")
    API.setText(0, 0, "abc")

    # Trouver le prochain mouvement
    find_next_move(0, 0)

if __name__ == "__main__":
    main()
