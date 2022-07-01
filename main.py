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
            a_writer.write('\n'+Data)
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

