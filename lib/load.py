#!/usr/bin/env python3
import yaml
import logging


def load_settings(path):
    with open(path) as f:
        document = f.read()
        document = yaml.load(document)
        logging.debug(document)
    return document


def parse_mvp_list(path):
    with open(path) as f:
        mvp_list = f.read()
        mvp_list = list(yaml.load_all(mvp_list))
        logging.debug(mvp_list)
        logging.debug(", ".join(str([mvp.name, mvp.info]) for mvp in mvp_list))
    return mvp_list


