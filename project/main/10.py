# -*- coding utf-8 -*-
from project.main.base import Base
from project.utils.inputparser.parser import StringParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path)

    def main(self):
        self.factory.set_type(StringParser)
        string_parser = self.factory.create(self.path)
        input_values = string_parser.parse_data_as_single_value()
        
        for i in range(len(input_values)//2):
            s = input_values[2*i]
            p = input_values[2*i + 1]
            print(self.sol.isMatch(s, p))
