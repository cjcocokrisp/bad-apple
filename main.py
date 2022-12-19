import cv2
import os
import pygame
import colorama

FRAME_SKIP = 9

os.system('clear')
colorama.init()

print("\033[39mDumping frames... This may take a moment...")

frame_dump = []
cap = cv2.VideoCapture('badapple.mp4')
dumped_frames = 0

if (cap.isOpened() == False):
    print("\033[31mbadapple.mp4 does not exist!")

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Progress: {} out of {} dumped.".format(dumped_frames, total_frames))

while(cap.isOpened()):

    dump = []

    for i in range(FRAME_SKIP):
        ret, frame = cap.read()
    try:
        rows, columns, channels = frame.shape
    except:
        break

    for x in range(rows):
        line = ""
        for y in range(columns):
            if frame[x, y, 0] > 245:
                line += ("\033[39m")
            elif frame[x, y, 0] < 10:
                line += ("\033[30m")
            line += "#"
        dump.append(line)
    frame_dump.append(dump)
    dumped_frames += FRAME_SKIP
    print("\033[AProgress: {} out of {} dumped.".format(dumped_frames, total_frames))

os.system('clear')

for i in range(72):
    for j in range(96):
        print("#", end="")
    print("")

for i in range(72):
    print("\033[A", end="")

pygame.mixer.init()
try:
    pygame.mixer.music.load("badapple.mp3")
except:
    print("\033[31mbadapple.mp3 does not exist!")
pygame.mixer.music.play()

for i in range(len(frame_dump)):
    for j in range(len(frame_dump[i])):
        print("{}".format(frame_dump[i][j]))
    for i in range(72):
        print("\033[A", end="")

os.system('clear')