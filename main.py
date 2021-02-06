import cv2
import matplotlib.pyplot as plt
import numpy as np

from constants import CIRCLES, CUBE_LOC, FACE_LEN, INSTRUCTION
from helper import (classify_color, draw_cube_face, get_solution,
                    prepare_cube_state)

instruct = INSTRUCTION
cap = cv2.VideoCapture(0)
FONT = cv2.FONT_HERSHEY_SIMPLEX


faces = 0
done = False
color = { k: { i:'' for i in range(9) } for k in range(7) }

while not done:
    # Capture frame-by-frame
    _, frame = cap.read()
    
    if faces == 7:
        cube_state = prepare_cube_state(face_dict=color)
        solution = get_solution(cube_state).strip()
        # print(solution)

        # get boundary of this text
        textsize = cv2.getTextSize(solution, FONT, 1, 2)[0]
        # print(textsize, frame.shape)

        # get coords based on boundary
        x_pos = (frame.shape[1] - textsize[0] // 2) // 2
        # print(x_pos)


        while True:
            _, frame = cap.read()
            cv2.putText(frame, "HERE'S YOUR SOLUTION!", (105, 50), FONT, fontScale=1.2, color=(255, 0, 0), thickness=3)
            cv2.putText(frame, solution, (x_pos, 100), FONT, fontScale=0.5, color=(0, 0, 255), thickness=2)
            cv2.imshow("Rubik's Cube Solver", frame)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                done = True
                break

    # if not input_taken:
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame, (65, 100), (263, 300), (10, 10, 10), 2)
    cv2.putText(frame, instruct, (200, 20), FONT, fontScale=0.7, color=(10, 10, 10), thickness=2)

    for i, (x, y) in enumerate(CIRCLES):
        cv2.rectangle(frame, (x-10, y-10), (x+10, y+10), (10, 10, 10), )  
        # cv2.imshow(f'{i}', frame[y-9:y+9, x-9: x+9])  


    k = cv2.waitKey(1) & 0xFF
    if k == ord(' '):
        for i, (x, y) in enumerate(CIRCLES):
            # print(hsv_frame[y, x], classify_color(hsv_frame[y, x], faces, i))
            color[faces][i] = classify_color(hsv_frame[y, x], faces, i)
        
        faces += 1
        # print(color)
    
    for i in range(min(faces, 6)):
        x, y = CUBE_LOC[i]
        x += 5 * i
        frame[y:y+FACE_LEN, x:x+FACE_LEN] = draw_cube_face(color[i])

    cv2.imshow("Rubik's Cube Solver", frame)

    if k == ord('n'):
        faces -= 1    

    if k == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
