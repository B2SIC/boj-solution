import matplotlib.pyplot as plt
from xlrd import open_workbook


class Elevator:
    def __init__(self, file_list):
        self.file_list = file_list
        self.altitude = []
        self.times = []

    @staticmethod
    def is_number(get_number):
        try:
            float(get_number)
            return True
        except ValueError:
            return False

    def draw_graph(self):
        for idx in range(len(self.file_list)):
            self.altitude = []
            self.times = []

            # Open .xls files
            xl = open_workbook(self.file_list[idx])
            xl_sheet = xl.sheet_by_index(0)

            # get Time Values
            for elem in xl_sheet.col_values(0):
                if self.is_number(elem):
                    elem = float(elem)
                    self.times.append(elem)

            # get Altitude Values
            for elem in xl_sheet.col_values(5):
                if self.is_number(elem):
                    elem = float(elem)
                    self.altitude.append(elem)

            # Print Output(Average Velocity)
            print("파일명:", self.file_list[idx])
            print("평균속도:", abs(self.altitude[0] - self.altitude[-1]) / abs(self.times[0] - self.times[-1]))
            print()

            # Draw Graph
            plt.figure(idx + 1)
            plt.plot(self.times, self.altitude, 'r-')
            plt.xlabel("Time(Second)")
            plt.ylabel("Altitude(Meter)")
            plt.grid()
            plt.show()


if __name__ == "__main__":
    e1 = Elevator(['el_Down-1.xls', 'el_Up-1.xls', 'el_Down-2.xls', 'el_Up-2.xls'])
    e1.draw_graph()
