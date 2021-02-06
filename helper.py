import cv2
import kociemba
import numpy as np

from constants import CELL_LEN, COLORS, FACE_LEN, INPUT_MAP


def classify_color(img, face_num, idx):
    h, s, v = img
    # print(h, s, v)

    if idx == 4:
        items = list(COLORS.items())
        return items[face_num][0]

    else:
        if s < 100:
            return "WHITE"
        elif h < 15:
            return "ORANGE"
        elif h < 45:
            return "YELLOW"
        elif h < 72:
            return "GREEN"
        elif h < 120:
            return "BLUE"
        elif h > 150:
            return "RED"
        else:
            return "BLACK"


def draw_cube_face(color_dict):
    arr = np.zeros((FACE_LEN, FACE_LEN, 3), dtype=int)
    
    for i in range(3):
        row = np.zeros((CELL_LEN, FACE_LEN, 3), dtype=int)
        x = CELL_LEN * i
        for j in range(3):
            y = CELL_LEN * j
            color = color_dict[3 * i + j]
            row[:, y:y+CELL_LEN, :] = COLORS[color]

        arr[x:x+CELL_LEN, :, :] = row
            
    # drawing borders
    arr[0] = COLORS['BLACK']
    arr[-1] = COLORS['BLACK']
    arr[:, 0, :] = COLORS['BLACK']
    arr[:, -1, :] = COLORS['BLACK']
    arr[CELL_LEN, :, :] = COLORS['BLACK']
    arr[2*CELL_LEN, :, :] = COLORS['BLACK']
    arr[:, CELL_LEN, :] = COLORS['BLACK']
    arr[:, 2*CELL_LEN, :] = COLORS['BLACK']
    
    return arr[:, :, ::-1]


def prepare_cube_state(face_dict):

    order = [4, 1, 0, 5, 3, 2]
    state = ''
    for f in order:
        face = face_dict[f]
        for i in range(9):
            state += INPUT_MAP[face[i]]

    # print(state)
    return state


def get_solution(state):
    soln = kociemba.solve(state)
    return soln
