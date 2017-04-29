# -*- coding: utf-8 -*-
from project.main.base import Base
from project.utils.inputparser.parser import IntegerParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path)

    def main(self):
        self.factory.set_type(IntegerParser)
        int_parser = self.factory.create(self.path)
        input_list = int_parser.parse_data_as_list()

        for i in range(len(input_list)//2):
            arr1 = input_list[2*i]
            arr2 = input_list[2*i + 1]
            print(self.sol.findMedianSortedArrays(arr1, arr2))
