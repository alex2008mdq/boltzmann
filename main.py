# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Particula:
    def __init__(self, masa, x, y, z, vx, vy, vz):
        Particula.masa = masa
        Particula.x = x
        Particula.y = y
        Particula.z = z
        Particula.vx = vx
        Particula.vy = vy
        Particula.vz = vz

class Ensemble:
    def __init__(self):