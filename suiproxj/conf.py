#! /usr/bin/python
# -*- coding: utf-8 -*-


def get_server_url():
    return 'https://simpleui.72wo.com'


def get_device_id():
    return _get_serial_number()


def _get_serial_number():
    return "穷得很以后再补票"


if __name__ == '__main__':
    print(_get_serial_number())
