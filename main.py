import ctypes
def RightClick(x, y):
    ctypes.windll.user32.SetCursorPos(x, y), ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(10, 0, 0, 0, 0)
def LeftClick(x, y):
    ctypes.windll.user32.SetCursorPos(x, y), ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)