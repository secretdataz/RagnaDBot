#!/usr/bin/env python3
import yaml
import logging


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)


class MVP:
    def __init__(self, yaml_mvp):
        self._task = None
        self.info = yaml_mvp
        self.death = False

    def set_task(self, task_):
        if self._task is not None:
            self._task.cancel()
        self._task = task_


class yaml_MVP(yaml.YAMLObject):
    yaml_tag = u'!Monster'
    # name: mvp name
    # map_spawn: list of maps and spawn times

    def __init__(self, name, info):
        self.name = name
        self.info = info
