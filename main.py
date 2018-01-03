#!/usr/bin/env python3
import yaml
import logging
import sys
import discord
import asyncio
import getopt
from lib import load

# Some ascii art
_welcome = """
 __  ____      _______    _______             _ version 0.1
|  \/  \ \    / /  __ \  |__   __|           | |
| \  / |\ \  / /| |__) |    | |_ __ __ _  ___| | _____ _ __
| |\/| | \ \/ / |  ___/     | | '__/ _` |/ __| |/ / _ \ '__|
| |  | |  \  /  | |         | | | | (_| | (__|   <  __/ |
|_|  |_|   \/   |_|         |_|_|  \__,_|\___|_|\_\___|_|
By Normynator                           for Ragnarok Online"""

# Config
_log_level = logging.DEBUG
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=_log_level)
logging.info(" ".join(["Config logging is enabled and set to:",
                       str(_log_level)]))
# Path to the config file
_config = "config.yml"
_client = discord.Client()
_settings = load.load_settings(_config)
_mvp_list = load.parse_mvp_list(_settings['mvp_list'])
_channel = discord.Object(id=_settings['channel_id'])
_debug_core = False


async def _job(time_):
    await asyncio.sleep(int(time_))
    logging.debug('_job: sleep over')
    await send_message(time_)


def parse_input(content):
    try:
        cmd, name, time_ = content.split(' ', 3)
    except():
        logging.warning("Parsing failed")
    logging.debug(' '.join(['parse_input:', 'cmd:', cmd,
                            '| name:', name, '| time:', time_]))


def parse_mvp_list(path):
    with open(path) as f:
        mvp_list = f.read()
        mvp_list = list(yaml.load_all(mvp_list))
        logging.debug(mvp_list)
        logging.debug(", ".join(str([mvp.name, mvp.info]) for mvp in mvp_list))
        for mvp in mvp_list:
            mvp.parse_maps()
    return mvp_list


def parse_args(args):
    opts, args = getopt.getopt(args[1:], "hl:t:")
    for opt, arg in opts:
        if opt == '-h':
            print("MVP Tracker: -h [shows this message], -l <debug, info, "
                  "warning> [sets the log level]")
            sys.exit(2)
        elif opt == '-l':
            log_type = logging.WARNING
            if arg == 'debug':
                log_type = logging.DEBUG
            elif arg == 'info':
                log_type = logging.INFO
            elif arg == 'warning':
                log_type = logging.WARNING
            logging.basicConfig(format='%(levelname)s:%(message)s',
                                level=log_type)


def get_mvps():
    return ", ".join(str(mvp.name) for mvp in _mvp_list)


@_client.event
async def on_ready():
    logging.debug(" ".join(['Logged in as', _client.user.name,
                            str(_client.user.id)]))


@_client.event
async def on_message(message):
    if message.content.startswith('!list'):
        await _client.send_message(_channel, get_mvps())
    elif message.content.startswith('!dead'):
        con = str(message.content)
        # temp disabled
        # parse_input(con)

        # working do NOT remove, needed later
        _mvp_list[1].set_task(asyncio.ensure_future(_job(con.split(' ')[1])))
        logging.debug('init timer')


async def send_message(message):
    await _client.send_message(_channel, message)


def main():
    print(_welcome)
    parse_args(sys.argv)
    if not _debug_core:
        _client.run(_settings['token'])

    # testing
    print(_mvp_list[1].info.name)
    print(_mvp_list[1].test())


if __name__ == "__main__":
    main()
