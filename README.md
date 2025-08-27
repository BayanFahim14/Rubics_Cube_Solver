🧩 Rubik’s Cube Simulator & Solver

A Python-based Rubik’s Cube simulator and solver that allows scrambling, visualizing, and solving the cube using Kociemba’s two-phase algorithm.
The project provides:

Interactive CLI menu for scrambling and solving.

2D visual display of the cube using matplotlib.

Move engine that respects real cube mechanics.

Integration with kociemba for optimal solving sequences.

🚀 Features

✅ Create a solved cube state

✅ Apply scramble moves

✅ Visualize the cube in 2D with correct color mapping

✅ Convert cube state to Kociemba-compatible facelet string

✅ Solve scrambled cube using the kociemba algorithm

✅ Interactive keys:

S → Scramble cube

V → Solve cube

Q → Quit

📦 Requirements

Make sure you have the following Python libraries installed:

pip install kociemba matplotlib

▶️ Usage

Clone or download the project.

Run the script:

python rubiks_cube_solver.py


You’ll see a menu:

Press:
S - Scramble
V - Solve
Q - Quit


Press S → The cube scrambles (20 random moves applied).

Press V → The program finds and applies the solution using Kociemba’s algorithm.

Press Q → Exit the program.

🎨 Cube Representation

U (Up) → White

D (Down) → Yellow

F (Front) → Green

B (Back) → Blue

R (Right) → Red

L (Left) → Orange

The cube is displayed in a 2D unfolded view:

        [U]
[L] [F] [R] [B]
        [D]

⚙️ How It Works

Cube Representation

Each face is stored as a 3×3 list.

Standard Rubik’s notation: U, D, L, R, F, B.

Moves Application

Moves (U, U', U2, etc.) rotate the face and adjust adjacent edges.

Scrambling

A random sequence of 20 moves is applied.

Solving

Cube state is converted to a 54-character facelet string.

kociemba.solve(facelet_str) returns the optimal move sequence.

Solution is applied and cube is restored.

📸 Example Run
Press:
S - Scramble
V - Solve
Q - Quit
Enter your choice: S

🔀 Scramble Moves: L' U R F' D2 B U' R' L D F' U L' B' R D2 U R' L B

[Scrambled cube visualization]

Enter your choice: V

🔍 Facelet String: UUUUUUUUURRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB
✅ Solution: R U R' U R U2 R'

🛠️ Future Improvements

Add 3D interactive cube visualization with Ursina or pygame.

Add keyboard controls for manual cube manipulation.

Support for custom scramble input.

Export move animations. 
