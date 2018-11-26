#!usr/bin/python3
# -*- coding: utf-8; -*-
# LICENSE: see Araneus/LICENSE
import configparser
from shutil import copy2
from Araneus.helpers import *

config = configparser.ConfigParser()


class Configurations:
    """
    Contains all methods for manipulate settings
    """
    conf_dir = ''
    conf_file_path = ''
    std_conf_file_path = ''

    def __init__(self):
        """
        - Checking os platform first
        - Setting file paths
        """
        self.declare()
        self.create_config_file()

    def declare(self):
        try:
            self.conf_dir = str(os.path.expanduser("~")) + "/.config/Araneus/"
            self.conf_file_path = self.conf_dir + "conf.ini"
            self.std_conf_file_path = os.path.dirname(os.getcwd()) + "/Araneus/configurations/default-conf.ini"
            return True
        except ValueError:
            print(ValueError)

    def create_config_dir(self):
        """
        Creates Application's directory
        :return: Bool
        """
        if not os.path.exists(self.conf_dir):
            try:
                os.mkdir(self.conf_dir)
                return True
            except ValueError:
                return ValueError
        return True

    def create_config_file(self):
        """
        Creates configurations file
        :return: Bool
        """
        if os.path.isfile(self.conf_file_path):
            return True
        try:
            self.create_config_dir()
            copy2(self.std_conf_file_path, self.conf_file_path)
            return True
        except ValueError:
            return ValueError

    def reset(self):
        """
        Resets preferences by copying the original configurations file over the old one
        :return: None
        """
        try:
            self.create_config_file()
            copy2(self.std_conf_file_path, self.conf_file_path)
            return True
        except ValueError:
            return ValueError

    def validate(self):
        """
        Validate the config file
        :return: bool
        """
        try:
            config.read(self.std_conf_file_path)
            nconfig = configparser.ConfigParser()
            nconfig.read(self.conf_file_path)
            for section in config.sections():
                for (key, val) in config.items(section):
                    if not nconfig.has_option(section, key):
                        self.reset()
            return True
        except Exception:
            return False

    def get_option(self, section, option, method='str'):
        """
        Read configurations file
        :return: String
        """
        try:
            self.validate()
            config.read(self.conf_file_path)
            if method == 'int':
                return config.getint(section, option)
            elif method == 'bool':
                return config.getboolean(section, option)
            else:
                return config.get(section, option)
        except ValueError:
            return ValueError("Error occurred while getting the required option value")

    def set_option(self, section, option, value):

        try:
            self.validate()
            config.read(self.conf_file_path)
            config[section][option] = str(value)
            with open(self.conf_file_path, 'w') as f:
                config.write(f)
            return self.get_option(section, option)
        except ValueError:
            raise ValueError("Error occurred while changing preferences")

#
# test = Configurations()
# test.reset()
# print(type(test.get_option('GENERAL', 'Language', 'str')))
# print(test.get_option('GENERAL', 'Language', 'str'))
