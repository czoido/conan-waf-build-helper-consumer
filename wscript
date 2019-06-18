#! /usr/bin/env python
# encoding: utf-8


VERSION = '0.0.1'
APPNAME = 'cxx_test'

top = '.'
out = 'build'


def options(opt):
    opt.load('compiler_cxx')


def configure(conf):
    conf.load('compiler_cxx')
    conf.load('waf_conan_libs_info', tooldir='.')
    conf.load('waf_conan_toolchain', tooldir='.')
    if conf.env.DEST_OS == 'win32' and conf.env.CC_NAME == 'msvc':
        conf.check_cc(lib='user32', mandatory=True)
        conf.check_cc(lib='comctl32', mandatory=True)
        conf.check_cc(lib='kernel32', mandatory=True)
        conf.check_cc(lib='ws2_32', mandatory=True)
        conf.check_cc(lib='gdi32', mandatory=True)
        conf.check_cc(lib='Advapi32', mandatory=True)
        conf.check_cc(lib='Comdlg32', mandatory=True)
        conf.env.CONAN_LIBS.extend(['USER32', 'COMCTL32', 'KERNEL32',
                                    'WS2_32', 'GDI32', 'ADVAPI32', 'COMDLG32'])


def build(bld):
    bld.program(source='example.cpp', target='app', use=bld.env.CONAN_LIBS)
