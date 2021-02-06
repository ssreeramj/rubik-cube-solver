INSTRUCTION = 'Place the cube in the box'

FACE_LEN = 90
CELL_LEN = FACE_LEN // 3

CIRCLES = [
    (102, 134), (165, 134), (226, 134),
    (102, 196), (165, 196), (226, 196),
    (102, 262), (165, 262), (226, 262),
]

COLORS = {
    'RED': [255, 0, 0],
    'BLUE': [0, 0, 255],
    'ORANGE': [255, 128, 0],
    'GREEN': [0, 255, 0],
    'WHITE': [255, 255, 255],
    'YELLOW': [255, 255, 0],
    'BLACK': [0, 0, 0]
}

CUBE_LOC = [(20 + i * FACE_LEN + 10, 360) for i in range(6)]

INPUT_MAP = {
    "RED": 'F',
    "BLUE": 'R',
    "ORANGE": 'B',
    "GREEN": 'L',
    "WHITE": 'U',
    "YELLOW": 'D'
}