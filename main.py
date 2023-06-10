import configparser
from helpers.postgres_data_fetching import PostgresClient



class Main:
    def __init__(self) -> None:
        """
        Constructor
        """

    def trigger(self):
        self.read()
        self.connect()
        self.extract()

    def read(self):
        config = configparser.ConfigParser()
        config.read("config.ini") #path_to_config

        self.creds = config['creds']

    def connect(self):

        #passing key value pair from config
        self.pg = PostgresClient(**self.creds)

    def extract(self):
        try:
            data = self.pg.extract_data()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    e = Main()
    e.trigger()