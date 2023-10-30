#!/usr/bin/env python3

import ClassHello


def main():
    name = input('Your name: ')
    object_hello = ClassHello.Hello(name)
    object_hello.say_hello()


if __name__ == '__main__':
    main()
