#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Judit Acs <judit@sch.bme.hu>
#
# Distributed under terms of the MIT license.

from typing import Any, Union, Optional, Sequence


def foo(value: float) -> None:
    print(value, value + 1)


def bar(value: float) -> int:
    foo(value)
    return 0


def happy_birthday(name: str, age: Union[int, str]) -> str:
    return f"Happy {age}th birthday, {name}"


def print_all(elements: Sequence, prefix: Optional[str] = None) -> None:
    for e in elements:
        if prefix:
            print(f"{prefix}: {e}")
        else:
            print(e)


def main():
    print(happy_birthday("John", 25))
    print_all([1, "abc", "def"])


if __name__ == '__main__':
    main()
