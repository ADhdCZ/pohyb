import pyautogui
import time
import math

pyautogui.FAILSAFE = False

def move_mouse_in_circle(radius, center_x, center_y, steps=66):
    for i in range(steps):
        # Výpočet úhlu (ve stupních) a převod na radiány
        angle = (2 * math.pi * i) / steps
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        
        # Pohyb myši na vypočítané souřadnice
        pyautogui.moveTo(x, y, duration=0.01)

def move_mouse_and_press_key():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    radius = min(center_x, center_y) // 3  # Poloměr kružnice

    while True:
        move_mouse_in_circle(radius, center_x, center_y)
        
        # Simulace stisknutí klávesy
        pyautogui.press('shift')  # Stiskne klávesu Shift
        
        time.sleep(5)  # Pauza mezi akcemi

if __name__ == "__main__":
    move_mouse_and_press_key()
