import csv, os
from config.config_reader import Config
from util.logger_service import LoggerMixin

class PrettyOutput(LoggerMixin):
    def __init__(self):
        self.input_csv = Config.outputfile
        self.output_csv = os.path.join(os.path.dirname(os.path.abspath(Config.outputfile)), "pretty.csv")
        self.failed_csv = os.path.join(os.path.dirname(os.path.abspath(Config.outputfile)), "failed.csv")

    def writing_pretty(self):
            self.logger.info(f'Reading from: {self.input_csv}')
            self.logger.info(f'Writing to: {self.output_csv}')
            header = ['schema_name', 'object_name', 'referenced_schema_name', 'referenced_object_name']
            # assuming input line like
            # ['SCHEMA_1.VIEW_1', 'SCHEMA_1.VIEW_1.sql', 'SCHEMA_2.TABLE_2', 'very-technical-uuid']
            with open(self.input_csv, "r") as inputfile:
                with open(self.output_csv, "w") as outputfile:
                    with open(self.failed_csv, "w") as failurefile:
                        csv_reader = csv.reader(inputfile)
                        csv_writer = csv.writer(outputfile)
                        csv_fails = csv.writer(failurefile)
                        for row in csv_reader:
                            try:
                                split_row = [row[0].split('.')[0], row[0].split('.')[1], row[2].split('.')[0], row[2].split('.')[1]]
                                pretty_row = [v.strip(" \"'[]") for v in split_row]
                                csv_writer.writerow(pretty_row)
                            except IndexError:
                                csv_fails.writerow(row)






