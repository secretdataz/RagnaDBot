#!/usr/bin/env python3
import yaml
import time
import logging


logging.basicConfig(format='%(levelname)s:%(message)s',
                          level=logging.DEBUG)



class MVP(yaml.YAMLObject):
    yaml_tag = u'!Monster'
    # name: mvp name
    # map_spawn: list of maps and spawn times
    def __init__(self, name, info):
        self.name = name
        self.info = info

    def parse_maps(self):
        print('test')
        logging.debug(' '.join(['_parse_maps:', info]))
