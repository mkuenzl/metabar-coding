import configparser


def read_config():
    config_file = configparser.ConfigParser()
    config_file.read('configuration.ini')
    return config_file


def read_config_by_path(config_path: str):
    config_file = configparser.ConfigParser()
    config_file.read(config_path)
    return config_file
