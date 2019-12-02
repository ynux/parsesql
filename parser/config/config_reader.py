# MIT License

# Copyright (c) 2019 Sebastian Daum

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os
from pathlib import Path
from util.logger_service import LoggerMixin


class Configuration(LoggerMixin):
    def __init__(self, filename:str):
        self.abspath = os.path.dirname(os.path.abspath(__file__))
        self.filename = filename
        self.configfilepath = os.path.join(self.abspath, self.filename)
        self.data = self.read()
        self.sqldir = self.get_sql_directory()
        self.outputfile = self.get_output_file()
        self.file_extension = self.data['file_extension']

    def read(self):
        try:
            with open(self.configfilepath) as json_data_file:
                return json.load(json_data_file)
        except Exception as e:
            self.logger.info(f"Cannot open file {self.filename}. See this error: {e}")

    def get_sql_directory(self):
        """
        Use Pathlib as it is transforming the path correctly to the given os
        """
        if self.data['sqldirectory'] == "":
            path_parent = os.path.dirname(self.abspath)
            sd = os.path.join(path_parent, 'exampleSql')
        else:
            sd = self.data['sqldirectory']
        return Path(sd)

    def get_output_file(self):
        if self.data['output_file'] == "":
            base_parent = os.path.dirname(self.abspath)
            of = os.path.join(base_parent, 'prod_viewdependencies.csv')
        else:
            of = self.data['output_file']
        return Path(of)

Config = Configuration(filename='configuration.json')
