import ctypes, pynput, time
mouse = pynput.mouse.Controller
def RightClick(x, y):
    ctypes.windll.user32.SetCursorPos(x, y), ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(10, 0, 0, 0, 0)
def LeftClick(x, y):
    ctypes.windll.user32.SetCursorPos(x, y), ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
def MoveMouse(x, y):
    global mouse
    mouse.position(x,y)
class Events:
    def MouseClick(self):
        def on_click(dx, dy, side, pressed):
            global x, y, button
            x = dx
            y = dy
            button = side
            if pressed:
                return False
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        global x, y, button
        return [x, y, button]

    def MouseMoved(self):
        def on_move(dx, dy):
            global x, y
            x = dx
            y = dy
        with mouse.Listener(on_move=on_move) as listener:
            listener.join()
        global x, y
        return [x, y]
