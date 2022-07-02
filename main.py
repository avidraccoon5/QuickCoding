import ctypes, pynput, time
class Mouse:
    def RightClick(x, y):
        ctypes.windll.user32.SetCursorPos(x, y), ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(10, 0, 0, 0, 0)
    def LeftClick(x, y):
        ctypes.windll.user32.SetCursorPos(x, y), ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    def MoveMouse(x, y):
        mouse = pynput.mouse.Controller
        mouse.position(x,y)
    def MouseClick(self):
        mouse = pynput.mouse.Controller
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
        mouse = pynput.mouse.Controller
        def on_move(dx, dy):
            global x, y
            x = dx
            y = dy
        with mouse.Listener(on_move=on_move) as listener:
            listener.join()
        global x, y
        return [x, y]
class DataSystem:
    file = []
    def GetData(Line):
        file = []
        with open('data', 'r') as reader:
            line = reader.readline()
            while line != '':
                test = ''
                for i in range(len(line)):
                    test+=line[i]
                file.append(test)
                line = reader.readline()
        print(file)
        return file[Line-1]
    def SaveData(Line, Data):
        with open('data', 'r', encoding='utf-8') as file:
            data = file.readlines()
        data[Line-1] = Data+"\n"
        with open('data', 'w', encoding='utf-8') as file:
            file.writelines(data)
    def CreateData(Data):
        file = []
        with open('data', 'r') as reader:
            line = reader.readline()
            while line != '':
                test = ''
                for i in range(len(line)-2):
                    test+=line[i-1]
                file.append(test)
                line = reader.readline()
        with open('data', 'a') as a_writer:
            if len(file) == 0:
                Line = 0
                data = Data + "\n"
                with open('data', 'w', encoding='utf-8') as file:
                    file.writelines(data)
                return 1
            else:
                a_writer.write(Data+"\n")
                return len(file)
    def Clear(self):
        with open('data', 'r', encoding='utf-8') as file:
            data = file.readlines()
        with open('data', 'r') as reader:
            line = reader.readline()
            while line != '':
                test = ''
                for i in range(len(line)-2):
                    test+=line[i-1]
                self.file.append(test)
                line = reader.readline()
        length = len(self.file)
        data = []
        for i in range(length):
            data.append('')
        with open('data', 'w', encoding='utf-8') as file:
            file.writelines(data)
class KeyBoard:
    def PressKey(key):
        Control = pynput.keyboard.Controller()
        if key == "space":
            key = " "
        Control.press(key)
        Control.release(key)
    def TypeInput(Data):
        Control = pynput.keyboard.Controller()
        Control.type(Data)
