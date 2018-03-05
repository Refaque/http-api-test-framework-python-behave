#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import parse
from behave import *


@parse.with_pattern(r'\d+')
def parse_number(text):
    return int(text)

register_type(Number=parse_number)