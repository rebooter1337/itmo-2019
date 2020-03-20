# -*- coding: utf-8 -*-

import argparse
import os
from datetime import datetime


def ls(dir=None):
    """Ls."""
    dir = os.getcwd() if dir is None else dir
    objects = []
    for folder_name in os.listdir(dir):
        if '.' not in folder_name:
            objects.append(folder_name)
    for file_name in os.listdir(dir):
        if '.' in file_name:
            objects.append(file_name)
    return objects


def mk(file_name):
    """Mk."""
    if os.path.isfile(file_name):
        return 'Error'
    try:
        open(file_name, 'w+').close
        return 'Success'
    except OSError:
        return 'Error'


def rm(file_name):
    """Rm."""
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        return 'Error'
    return 'Success'


def contains(file_name):
    """Contains."""
    if os.path.isfile(file_name):
        return True
    return False


def since(time, dir=None):
    """Since."""
    files = []
    if dir is None:
        dir = os.getcwd()
    try:
        date = datetime.strptime(time, '%Y-%m-%d_%H:%M:%S')
        for file_name in os.listdir(dir):
            if dir == os.getcwd():
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(file_name),
                )
            else:
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(dir / file_name),
                )
            if file_datetime > date:
                files.append(file_name)
        return files
    except ValueError:
        return 'Use mask: y-m-d-h:m:s'


def main():
    """Main."""
    commands = {
        'ls': ls,
        'mk': mk,
        'rm': rm,
        'contains': contains,
        'since': since,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'argument',
        type=str,
        nargs='*',
    )
    argument = parser.parse_args()
    command = argument.argument[0]
    parameter = None
    if command in commands:
        if len(argument.argument) > 1:
            parameter = argument.argument[1]
        programm = commands[command]
        print(programm(parameter))
    else:
        print('There is no such command')

if __name__ == '__main__':
    main()
