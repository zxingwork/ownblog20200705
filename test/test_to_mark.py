#!/usr/bin/python3
# author:zxing
# -*- coding:utf-8 -*-
# @time     : 11:43 上午
# @site     :
# @File     :test_to_mark.py
# @software :PyCharm
import pytest

print(pytest.__version__)


def test_func1():
    assert 1 == 1


@pytest.mark.skip(reason='out of data')
def test_func2():
    assert 1 != 1


@pytest.mark.skipif(pytest.__version__ < '5.4.4',
                    reason='the pytest version is too low')
def test_api1():
    assert 1 == 1


@pytest.mark.xfail(pytest.__version__ > '5.4.2',
                   reason='not support until v5.4.6')
def test_api2():
    assert 1 != 1


@pytest.mark.parametrize('passwd',
                         ['12345689797',
                          'asdfghjkl',
                          'as12343454tgt5'])
def test_passwd_length(passwd):
    assert len(passwd) >= 8


@pytest.mark.parametrize('user,passwd',
                         [('jack', 'adndefrfrg'),
                          ('tom', '12jfirfjirgnt')])
def test_passwd_md5(user, passwd):
    db = {
        'jack': ''
    }