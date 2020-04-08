import tempfile
import os
from Sort import Sorting


class Large_file_sort(object):
    __temp_arr = []
    __number_of_lines = 10
    __name_of_files = []
    __count = 1
    __sort = Sorting()

    def sort(self, file_name):
        self.__read_file(file_name)
        self.__sort_files()
        self.__create_res_file()

    def __read_file(self, f_name):
        with open(f_name, 'r') as file:
            for line in file:
                self.__temp_arr.append(int(line))
                self.__count += 1
                if self.__count > self.__number_of_lines:
                    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp:
                        arr = self.__sort.merge_sort(self.__temp_arr)
                        temp.writelines(f'{i}\n' for i in arr)
                        self.__name_of_files.append(temp)
                    self.__temp_arr.clear()
                    self.__count = 1

    def __sort_files(self):
        while len(self.__name_of_files) > 1:
            with open(self.__name_of_files[0].name, 'r') as f0, open(self.__name_of_files[1].name, 'r') as f1:
                with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp:
                    self.__sort_lines(temp, [f0, f1])
                    self.__name_of_files.append(temp)
            self.__del_files(f0)
            self.__del_files(f1)

    def __sort_lines(self, temp, files):
        line_f = files[0].readline()
        line_s = files[1].readline()
        while line_s and line_f:
            if int(line_f) > int(line_s):
                temp.writelines(line_s)
                line_s = files[1].readline()
            else:
                temp.writelines(line_f)
                line_f = files[0].readline()
        if line_f:
            self.__cont_fill(temp, files[0], line_f)
        else:
            self.__cont_fill(temp, files[1], line_s)

    def __cont_fill(self, temp, file, line):
        while line:
            temp.writelines(f'{line}')
            line = file.readline()

    def __del_files(self, file):
        if os.path.exists(file.name):
            self.__name_of_files.pop(0)
            os.remove(file.name)

    def __create_res_file(self):
        temp_file = self.__name_of_files[0]
        with open('res_numbers.txt', 'w') as f, open(temp_file.name, 'r') as temp:
            for i in temp:
                f.writelines(i)
        self.__del_files(temp_file)


import random
with open('numbers.txt', 'w') as f:
    f.writelines('{}\n'.format(random.randint(-100, 100)) for _ in range(50))

a= Large_file_sort()
a.sort("numbers.txt")