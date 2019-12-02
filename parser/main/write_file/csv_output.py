from config.config_reader import Config
from util.logger_service import LoggerMixin


class CsvOutput(LoggerMixin):
    def __init__(self):
        self.csvfile = Config.outputfile

    def get_output_csv_file(self):
        self.logger.info(f'Your output will go to csv: {self.csvfile}')
        return (self.csvfile)
