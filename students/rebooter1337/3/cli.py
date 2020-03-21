# -*- coding: utf-8 -*-

import argparse
import os
from datetime import datetime


def ls(directory=None):
    """Ls."""
    directory = os.getcwd() if directory is None else directory
    ls_staff = []
    for folder_name in os.listdir(directory):
        if '.' not in folder_name:
            ls_staff.append(folder_name)
    for file_name in os.listdir(directory):
        if '.' in file_name:
            ls_staff.append(file_name)
    return ls_staff


def mk(file_name):
    """Mk."""
    if os.path.isfile(file_name):
        return 'Error'
    try:  # noqa: WPS229
        current_file = open(file_name, 'w+').close
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


def since(time, directory=None):  # noqa C901
    """Since."""
    files = []
    if directory is None:
        directory = os.getcwd()
    try:  # noqa: WPS229
        date = datetime.strptime(time, '%Y-%m-%d_%H:%M:%S')
        for file_name in os.listdir(directory):
            if directory == os.getcwd():
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(file_name),
                )
            else:
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(directory / file_name),
                )
            if file_datetime > date:
                files.append(file_name)
        return files
    except ValueError:
        return 'Use mask: y-m-d-h:m:s'


def main():  # noqa: WPS210
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
        print(programm(parameter))  # noqa: T001
    else:
        print('There is no such command')  # noqa: T001

if __name__ == '__main__':
    main()
