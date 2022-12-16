class Computer(object):
    case: str
    mainboard: str
    cpu: str
    memory: str
    hard_drive: str
    video_card: str

    def display(self):
        print('Custom Computer:')
        print(f'\t{"Case":>10}: {self.case}')
        print(f'\t{"Mainboard":>10}: {self.mainboard}') 
        print(f'\t{"CPU":>10}: {self.cpu}') 
        print(f'\t{"Memory":>10}: {self.memory}') 
        print(f'\t{"Hard drive":>10}: {self.hard_drive}') 
        print(f'\t{"Video card":>10}: {self.video_card}') 
