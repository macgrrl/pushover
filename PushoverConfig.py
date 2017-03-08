"""
PushoverConfig.py

reads and writes the pushover configuration file

Author: Kirschen Seah

Copyright (c) 2017
"""

import os
from ConfigParser import RawConfigParser

class PushoverConfig:

# global

    default_config_filename = '~/.pushover_config'
    user_section = 'user'
    app_key_option = 'app_key'
    user_key_option = 'user_key'


    def __init__(self, filename=default_config_filename):
        self.app_key = ''
        self.user_key = ''
        self.config_filename = filename


    def read(self):
        rcp = RawConfigParser()
        if rcp.read(os.path.expanduser(self.config_filename)) != []:
            self.app_key = rcp.get(PushoverConfig.user_section, PushoverConfig.app_key_option)
            self.user_key = rcp.get(PushoverConfig.user_section, PushoverConfig.user_key_option)
        else:
            print self.config_filename + ' not found'


    def write(self):
        rcp = RawConfigParser()
        rcp.add_section(PushoverConfig.user_section)
        rcp.set(PushoverConfig.user_section, PushoverConfig.app_key_option, self.app_key)
        rcp.set(PushoverConfig.user_section, PushoverConfig.user_key_option, self.user_key)
        f = open(os.path.expanduser(self.config_filename), 'w')
        rcp.write(f)
        f.close()


if __name__ == "__main__":
    import sys
    pc = PushoverConfig()
    if len(sys.argv) >= 3:
        # app key and user key arguments
        pc.app_key = sys.argv[1]
        pc.user_key = sys.argv[2]
        pc.write()
    else:
        # no arguments - show current
        pc.read()
        print 'app key:' + pc.app_key
        print 'user key:' + pc.user_key
