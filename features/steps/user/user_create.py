#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from behave import *
from hamcrest import *
from libs.database import delete_user
from libs.header import Header
from libs.request import Request
from libs.const import *
from features.steps.parse_number import *


@given(u'user {user} not exists')
def user_not_exists(context, user):
    delete_user(user)


@when(u'create user {user} age {age}')
def create_user(context, user, age):
    header = Header()
    header.set_content_json()
    header.set_accept_json()
    body = {"name": user, "age": age}
    req = Request(POST, api_server_host, api_server_port, '/user', header.headers, body)
    context.resp = req.send()


@then(u'the response status code is {code:Number}')
def verify_response_status_code(context, code):
    assert_that(context.resp.status_code, equal_to(code))

