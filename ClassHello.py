#!/usr/bin/env python3

import subprocess


class Hello:
    def __init__(self, some_name):
        self.some_name = some_name

    def say_hello(self):
        sysinfo = subprocess.check_output(['uname', '-a'])
        print(f'Hello, {self.some_name}!\nI am {sysinfo.decode("utf-8")}')

        with open('log.txt', 'a') as file:
            file.write(self.some_name + '\n' + sysinfo.decode("utf-8"))

        input('Press Enter to exit...')
