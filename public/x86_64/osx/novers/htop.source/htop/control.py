# coding: utf-8
import os

from ubik_toolbelt.logger import stream_logger
from ubik_toolbelt.control import Control

from ubik_toolbelt.contrib import which

from ubik.core import conf

class Package(Control):
    def __init__(self):
        Control.__init__(self)
        self.name = 'htop'
        self.version = '0.8.2.1'
        self.release = '0'
        self.requires = []
        self.arch = ''
        self.dist = ''
        self.vers = ''
        self.description = ''

        self.cur_dir = os.getcwd()
        self.src_dir = os.path.join(os.getcwd(), 'source')
        self.pkg_dir = os.path.join(os.getcwd(), 'build')

    def build(self):
        stream_logger.info('Building...')
        os.chdir(self.src_dir)

        os.system('curl -k -L https://github.com/max-horvath/htop-osx/tarball/%s-2012-04-18 | tar zx' % self.version)
        os.chdir('max-horvath-htop-osx-d92a7d4')
        os.system('./autogen.sh')
        os.system('./configure --disable-dependency-tracking --prefix=%s' % conf.get('settings', 'packages'))
        os.system('make')

    def package(self):
        stream_logger.info('Packaging...')
        os.chdir(self.src_dir)
        os.chdir('max-horvath-htop-osx-d92a7d4')

        os.system('make prefix=%s install' % self.pkg_dir)

    def pre_install(self):
        pass

    def post_install(self):
        pass

    def pre_upgrade(self):
        pass

    def post_upgrade(self):
        pass

    def pre_remove(self):
        pass

    def post_remove(self):
        pass