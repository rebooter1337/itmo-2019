# -*- coding: utf-8 -*-

"""Fw for running tests."""
import glob
import importlib
import inspect
import os
import sys
import traceback

PATTERN = '/test_*.py'


def select_path(path):
    """Returns collected test files."""
    if not path:
        path = os.getcwd()
        tests = glob.glob(path + PATTERN)
        return tests
    sys.path.append(path)
    tests = glob.glob(path + PATTERN)

    if not tests:
        print('no tests here')  # noqa: T001
    return tests


def find_tests(tests):  # noqa: WPS210
    """Returns collected array with modules and array with tests."""
    to_import = []
    my_tests = []

    for module in tests:
        method = inspect.getmodulename(module)
        to_import.append(importlib.import_module(method))
    import_list = list(set(to_import))
    for fu in import_list:
        methodes = [pm[0] for pm in inspect.getmembers(fu, inspect.isfunction)]
        for methode in methodes:
            if 'test_' in methode:
                my_tests.append(methode)
    return to_import, my_tests


def run_tests(to_import='', my_tests=''):
    """Runs tests."""
    for test in my_tests:
        for module in to_import:
            check_test = hasattr(module, test)  # noqa: WPS421
            if check_test:
                func = getattr(module, test)
                try:  # noqa: WPS229
                    func()
                    path = inspect.getfile(module)
                    print('{0} {1} {2}'.format(  # noqa: T001
                        test,
                        path,
                        ' - ok\n',
                        ),
                    )
                except AssertionError:
                    path = inspect.getfile(module)
                    print('{0} {1} {2} {3}'.format(test, path, ' - fail\n', traceback.format_exc()))  # noqa: T001, E501


if __name__ == '__main__':
    path = input('Enter your path: ')  # noqa: S322, WPS421
    if os.path.exists(path) or not path:
        tests = select_path(path)
    else:
        print('no such dir')  # noqa: T001
        sys.exit()
    to_import, my_tests = find_tests(tests)
    run_tests(to_import, my_tests)
