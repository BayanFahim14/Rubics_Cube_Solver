import copy
import kociemba
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# --- Face Rotation ---
def rotate_face_cw(face):
    return [list(reversed(col)) for col in zip(*face)]

def rotate_face_ccw(face):
    return [list(col) for col in zip(*face)][::-1]

# --- Physical Cube Rotation ---
def _apply_base_move(cube, move):
    cube = copy.deepcopy(cube)
    if move == 'U':
        cube['U'] = rotate_face_cw(cube['U'])
        temp = cube['F'][0][:]
        cube['F'][0] = cube['R'][0]
        cube['R'][0] = cube['B'][0]
        cube['B'][0] = cube['L'][0]
        cube['L'][0] = temp
    elif move == 'D':
        cube['D'] = rotate_face_cw(cube['D'])
        temp = cube['F'][2][:]
        cube['F'][2] = cube['L'][2]
        cube['L'][2] = cube['B'][2]
        cube['B'][2] = cube['R'][2]
        cube['R'][2] = temp
    elif move == 'L':
        cube['L'] = rotate_face_cw(cube['L'])
        temp = [cube['U'][i][0] for i in range(3)]
        for i in range(3):
            cube['U'][i][0] = cube['B'][2 - i][2]
            cube['B'][2 - i][2] = cube['D'][i][0]
            cube['D'][i][0] = cube['F'][i][0]
            cube['F'][i][0] = temp[i]
    elif move == 'R':
        cube['R'] = rotate_face_cw(cube['R'])
        temp = [cube['U'][i][2] for i in range(3)]
        for i in range(3):
            cube['U'][i][2] = cube['F'][i][2]
            cube['F'][i][2] = cube['D'][i][2]
            cube['D'][i][2] = cube['B'][2 - i][0]
            cube['B'][2 - i][0] = temp[i]
    elif move == 'F':
        cube['F'] = rotate_face_cw(cube['F'])
        temp = cube['U'][2][:]
        for i in range(3):
            cube['U'][2][i] = cube['L'][2 - i][2]
            cube['L'][2 - i][2] = cube['D'][0][2 - i]
            cube['D'][0][2 - i] = cube['R'][i][0]
            cube['R'][i][0] = temp[i]
    elif move == 'B':
        cube['B'] = rotate_face_cw(cube['B'])
        temp = cube['U'][0][:]
        for i in range(3):
            cube['U'][0][i] = cube['R'][i][2]
            cube['R'][i][2] = cube['D'][2][2 - i]
            cube['D'][2][2 - i] = cube['L'][2 - i][0]
            cube['L'][2 - i][0] = temp[i]
    return cube

# --- Apply Modifier Moves ---
def apply_move(cube, move):
    base, mod = move[0], move[1:] if len(move) > 1 else ''
    turns = {'': 1, '2': 2, "'": 3}
    for _ in range(turns.get(mod, 1)):
        cube = _apply_base_move(cube, base)
    return cube

# --- Cube to Facelet String ---
def cube_to_facelet(cube):
    face_order = ['U', 'R', 'F', 'D', 'L', 'B']
    color_to_face = {
        cube['U'][1][1]: 'U',
        cube['R'][1][1]: 'R',
        cube['F'][1][1]: 'F',
        cube['D'][1][1]: 'D',
        cube['L'][1][1]: 'L',
        cube['B'][1][1]: 'B',
    }
    facelet_string = ''
    for face in face_order:
        for row in cube[face]:
            for color in row:
                facelet_string += color_to_face[color]
    return facelet_string

# --- Scrambled Cube ---
def create_solved_cube():
    return {
        'U': [['W'] * 3 for _ in range(3)],
        'R': [['R'] * 3 for _ in range(3)],
        'F': [['G'] * 3 for _ in range(3)],
        'D': [['Y'] * 3 for _ in range(3)],
        'L': [['O'] * 3 for _ in range(3)],
        'B': [['B'] * 3 for _ in range(3)],
    }

# --- Apply Moves ---
def apply_moves(cube, moves):
    for move in moves.split():
        cube = apply_move(cube, move)
    return cube

# --- 2D Visual Display ---
def draw_2d_colored_cube(cube, title):
    color_map = {
        'W': 'white', 'Y': 'yellow', 'G': 'green',
        'B': 'blue', 'R': 'red', 'O': 'orange'
    }
    face_positions = {
        'U': (3, 6), 'L': (0, 3), 'F': (3, 3),
        'R': (6, 3), 'B': (9, 3), 'D': (3, 0)
    }
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.axis('off')
    for face, (x_offset, y_offset) in face_positions.items():
        for i in range(3):
            for j in range(3):
                color = color_map[cube[face][2 - i][j]]
                rect = patches.Rectangle((x_offset + j, y_offset + i), 1, 1, facecolor=color, edgecolor='black')
                ax.add_patch(rect)
    plt.xlim(0, 12)
    plt.ylim(0, 9)
    plt.show()

# --- Main Execution with Interactive Keys ---
if __name__ == '__main__':
    cube = create_solved_cube()

    while True:
        print("\nPress:")
        print("S - Scramble")
        print("V - Solve")
        print("Q - Quit")
        choice = input("Enter your choice: ").upper()

        if choice == 'S':
            moves_list = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "L", "L'", "R", "R'"]
            scramble_moves = ' '.join(random.choices(moves_list, k=20))
            cube = create_solved_cube()
            cube = apply_moves(cube, scramble_moves)
            print("\n🔀 Scramble Moves:", scramble_moves)
            draw_2d_colored_cube(cube, "Scrambled Cube")

        elif choice == 'V':
            facelet_str = cube_to_facelet(cube)
            print("🔍 Facelet String:", facelet_str)
            try:
                solution = kociemba.solve(facelet_str)
                print("✅ Solution:", solution)
                cube = apply_moves(cube, solution)
                draw_2d_colored_cube(cube, "Solved Cube")
            except Exception as e:
                print("❌ Invalid cube or scramble string:", str(e))

        elif choice == 'Q':
            print("👋 Exiting.")
            break

        else:
            print("❗ Invalid input. Please try again.")
