class Computer(object):

    def __init__(self, case, mainboard, cpu, memory, hard_drive, video_card):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive
        self.video_card = video_card

    def display(self):
        print('Custom Computer:')
        print(f'\t{"Case":>10}: {self.case}')
        print(f'\t{"Mainboard":>10}: {self.mainboard}') 
        print(f'\t{"CPU":>10}: {self.cpu}') 
        print(f'\t{"Memory":>10}: {self.memory}') 
        print(f'\t{"Hard drive":>10}: {self.hard_drive}') 
        print(f'\t{"Video card":>10}: {self.video_card}') 
