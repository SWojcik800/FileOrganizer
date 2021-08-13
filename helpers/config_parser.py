import configparser

def parse():
    config = configparser.ConfigParser()
    config.read("appconfig.txt")

    return config["OPTIONS"]



