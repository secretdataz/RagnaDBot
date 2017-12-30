#!/usr/bin/env python3
import yaml

class MVP(yaml.YAMLObject):
    yaml_tag = u'!Monster'
    # name: mvp name
    # map_spawn: list of maps and spawn times
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.downtime = 0


