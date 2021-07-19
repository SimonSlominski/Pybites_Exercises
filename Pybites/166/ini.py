"""Bite 166. Complete a tox ini file parser class"""


import configparser
import re


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = self._read_config(ini_file)

    def _read_config(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file)
        return config

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        enviroment = sorted([i.lstrip() for i in re.split(r'\n| ,|,', self.config['tox']['envlist']) if i])
        return enviroment

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        # return [basepython
        #         for basepython in self.config.get("testenv", "basepython")]
        basepython = []
        for c in self.config.sections():
            try:
                if self.config[c]['basepython'] not in basepython:
                    basepython.append(self.config[c]['basepython'])
            except KeyError:
                pass
        return basepython
