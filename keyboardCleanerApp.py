import tkinter as tk
import threading
from pynput import keyboard

keyboard_locked = False

def lock_keyboard():
    global keyboard_locked
    if keyboard_locked:
        return

    keyboard_locked = True
    label.config(text="Keyboard is LOCKED.\nPress ⌘ + ⇧ + K to unlock.")
    
    def block_keys():
        while keyboard_locked:
            pass  
    threading.Thread(target=block_keys, daemon=True).start()

def unlock_keyboard():
    global keyboard_locked
    keyboard_locked = False
    label.config(text="Keyboard is UNLOCKED.\nYou can now clean safely.")

def on_press(key):
    try:
        if key == keyboard.Key.f9:  
            unlock_keyboard()
    except AttributeError:
        pass

root = tk.Tk()
root.title("Keyboard Cleaner")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Click below to lock the keyboard.", font=("Helvetica", 14), wraplength=350)
label.pack(pady=30)

lock_button = tk.Button(root, text="🔒 Lock Keyboard", command=lock_keyboard, font=("Helvetica", 12))
lock_button.pack()

listener = keyboard.Listener(on_press=on_press)
listener.start()

root.mainloop()