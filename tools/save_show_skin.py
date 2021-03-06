import sys
import numpy as np
import cv2
import time
ts = int(time.time())
import find_skin as skin

filename = sys.argv[1]
original = cv2.imread(sys.argv[1])
#cv2.imwrite(f"grab_cut_tests/{ts}.{filename[8:]}.0.original.png", original)
show_skin_img = skin.show_skin(sys.argv[1])

find_skin_img =  skin.find_skin(sys.argv[1])

cv2.imwrite(f"grab_cut_tests/{ts}.{filename[8:]}.0.find_skin.png", find_skin_img)
cv2.imwrite(f"grab_cut_tests/{ts}.{filename[8:]}.0.show_skin.png", show_skin_img)
