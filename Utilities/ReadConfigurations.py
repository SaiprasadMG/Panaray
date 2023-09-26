from configparser import ConfigParser


def get_config(category,Key):
    config = ConfigParser()
    config.read("C:\\Users\\sgondkar\\PycharmProjects\\PanarayRegressionSuite\\Configurations\\config.ini")
    return config.get(category,Key)

