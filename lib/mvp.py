#!/usr/bin/env python3
import yaml
import logging


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)

def _parse_yaml_obj(yaml_obj):
        name = yaml_obj.name
        map_list = {}
        for map_ in yaml_obj.info:
            map_list[map_[0]] = (Map(map_[0], map_[1], map_[2]))
        return (name, map_list)

class Map:
    def __init__(self, map_name, min_, max_):
        self.min_ = min_
        self.max_ = max_
        self.map_name = map_name
        self._task = None

    def set_task(self, task_):
        if self._task is not None:
            self._task.cancel()
        self._task = task_


class MVP:

    def __init__(self, yaml_mvp):
        self.name, self.maps = _parse_yaml_obj(yaml_mvp)

    async def set_task(self, time_):
        

class yaml_MVP(yaml.YAMLObject):
    yaml_tag = u'!Monster'
    # name: mvp name
    # map_spawn: list of maps and spawn times

    def __init__(self, name, info):
        self.name = name
        self.info = info
