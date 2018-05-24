import copy


class McCluskey:
    def __init__(self, var, minterm_list):
        self.var = var
        self.minterm = minterm_list
        self.binary_list = []
        self.generations = [[], [], [], [], [], [], []]
        self.pi = []
        self.epi_set = set()
        self.nepi_set = set()

    def divide_generation(self, bit):
        bit_list = bit[0]
        count = 0
        for i in bit_list:
            if i == '1':
                count += 1
        return count

    def assign_generations(self):
        for i in self.binary_list:
            self.generations[self.divide_generation(i)].append(i)

    def get_highest_generation(self):
        max_generation = 0

        for i in range(len(self.generations)):
            if len(self.generations[i]) > 0:
                max_generation = i
        return max_generation

    def pos_combine(self, bit1, bit2):
        number_of_same = 0

        for i in range(self.var):
            if bit1[0][i] == bit2[0][i]:
                number_of_same += 1

        if number_of_same == self.var - 1:
            return True

        return False

    def combine(self, bit1, bit2):
        re_str = ["", []]

        for i in range(self.var):
            if bit1[0][i] == bit2[0][i]:
                re_str[0] += bit1[0][i]
            else:
                re_str[0] += "2"

        re_str[1] = copy.deepcopy(bit1[1])

        for i in bit2[1]:
            if i not in bit1[1]:
                re_str[1].append(i)
        re_str[1].sort()
        return re_str

    def convert_binary(self):
        for num in self.minterm:
            bin_tmp = bin(num)[2:]

            if len(bin_tmp) != self.var:
                self.binary_list.append(['0' * (self.var - len(bin_tmp)) + bin_tmp, [num]])
            else:
                self.binary_list.append([bin_tmp, [num]])

    def compare(self, str, str2):
        re_str = ""

        for i in range(len(str)):
            if str[i] == str2[i]:
                re_str += str[i]
            else:
                re_str += '-'

        return re_str

    def get_epi_or_nepi(self):
        dic_pi = {}

        for elem in range(len(self.pi)):
            for comb in self.pi[elem][1]:
                dic_pi[comb] = dic_pi.get(comb, 0) + 1

        for key, value in dic_pi.items():
            if value == 1:
                for elem in range(len(self.pi)):
                    for comb in self.pi[elem][1]:
                        if comb == key:
                            self.epi_set.add(self.pi[elem][0])

        for elem in range(len(self.pi)):
            if self.pi[elem][0] not in self.epi_set:
                self.nepi_set.add(self.pi[elem][0])

    def print_output(self):
        return_string = ""
        return_string += "EPI "

        if len(self.epi_set) != 0:
            asc_list = sorted(self.epi_set)

            for elem in asc_list:
                for char in elem:
                    if char == '2':
                        return_string += '-'
                    else:
                        return_string += char
                return_string += ' '

        return_string += "NEPI "
        if len(self.nepi_set) != 0:
            asc_list = sorted(self.nepi_set)

            for elem in asc_list:
                for char in elem:
                    if char == '2':
                        return_string += '-'
                    else:
                        return_string += char
                return_string += ' '

        return return_string

    def get_pi(self):
        self.convert_binary()
        self.assign_generations()

        while self.get_highest_generation() != 0:
            temp = [[], [], [], [], [], [], []]
            for i in range(self.get_highest_generation()):
                for a in self.generations[i]:
                    judge = 0

                    for b in self.generations[i + 1]:
                        if self.pos_combine(a, b):
                            judge = 1
                            if self.combine(a, b) not in temp[i]:
                                temp[i].append(self.combine(a, b))
                    if judge == 0:
                        if i != 0:
                            for b in self.generations[i - 1]:
                                if self.pos_combine(a, b):
                                    judge = 1

                        if judge == 0:
                            if a not in self.pi:
                                self.pi.append(a)

            i = self.get_highest_generation()
            for a in self.generations[i]:
                judge = 0

                for b in self.generations[i - 1]:

                    if self.pos_combine(a, b):
                        judge = 1

                if judge == 0:
                    self.pi.append(a)
            self.generations = temp
        for i in self.generations[0]:
            self.pi.append(i)


def solution(res):
    input_list = list(map(int, res.split()))

    number_of_var = input_list[0]
    minterm_list = []

    for i in range(2, 2 + input_list[1]):
        minterm_list.append(input_list[i])

    mc = McCluskey(number_of_var, minterm_list)
    mc.get_pi()
    mc.get_epi_or_nepi()
    return mc.print_output()


if __name__ == "__main__":
    input_string = "3 6 0 1 2 5 6 7"
    print(solution(input_string))
