import kociemba
from collections import Counter

# cube_state = 'BUBBUBRLL BDDDRRBBF FUUFFLUFU LFDLDRRLB DRURLDRFL LBRDBUDUF'
cube_state = 'RLFBULBDBUDDRRLLDLRBLFFURBFBUUUDFLDBFRURLUDLDRBUFBFDRF'

print(Counter(cube_state))

sol = kociemba.solve(cube_state)

print(sol)