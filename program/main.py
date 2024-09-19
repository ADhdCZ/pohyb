import pyautogui
import time
import math
import itertools
import random
import os
import threading

pyautogui.FAILSAFE = False

def move_mouse_in_circle(radius, center_x, center_y, steps=66):
    for i in range(steps):
        angle = (2 * math.pi * i) / steps
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        pyautogui.moveTo(x, y, duration=0.01)

def move_mouse_and_press_key():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    radius = min(center_x, center_y) // 3

    while True:
        move_mouse_in_circle(radius, center_x, center_y)
        pyautogui.press('shift')
        time.sleep(5)

messages = [
    "System initializing...",
    "User authenticated.",
    "Loading modules...",
    "Connecting to mainframe...",
    "Decrypting data...",
    "Transmission received.",
    "Hacking the mainframe...",
    "Encrypting data...",
    "Posun running...",
    "Rebooting system..."
]

message_cycle = itertools.cycle(messages)

def generate_matrix_line():
    length = random.randint(10, 100)
    line = ''.join(random.choice('01') for _ in range(length))
    return line

def display_matrix():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            for _ in range(20):
                print(generate_matrix_line())
            print("\n")
            print(next(message_cycle))
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Script was stopped by the user.")

if __name__ == "__main__":
    # Spustí pohyb myši a stisk klávesy ve zvláštním vlákně
    mouse_thread = threading.Thread(target=move_mouse_and_press_key)
    mouse_thread.daemon = True  # Zajištění, že se vlákno ukončí s hlavním programem
    mouse_thread.start()
    pyautogui.hotkey('f11')
    # Spustí zobrazení Matrixu v hlavním vlákně
    display_matrix()
