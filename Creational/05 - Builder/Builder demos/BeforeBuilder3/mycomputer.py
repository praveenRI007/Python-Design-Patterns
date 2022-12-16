from computer import Computer

class MyComputer(object):

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = 'Coolermaster'
        computer.mainboard = 'MSI'
        computer.cpu = 'Intel Core i9'
        computer.memory = '2 x 16GB'
        computer.hard_drive = 'SSD 2TB'
        computer.video_card = 'GeForce'
