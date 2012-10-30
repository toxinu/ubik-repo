# coding: utf-8
import os

from ubik_toolbelt.logger import stream_logger
from ubik_toolbelt.control import Control

from ubik.core import conf

class Package(Control):
    def __init__(self):
        Control.__init__(self)
        self.name = 'wget'
        self.version = '1.14'
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

        os.system('wget http://ftp.gnu.org/gnu/wget/wget-%s.tar.gz' % self.version)
        os.system('tar xvf wget-%s.tar.gz' % self.version)
        os.system('rm wget-%s.tar.gz' % self.version)
        os.chdir('wget-%s' % self.version)
        os.system('./configure --prefix=%s' % conf.get('settings', 'packages'))
        os.system('make')

    def package(self):
        stream_logger.info('Packaging...')
        os.chdir(self.src_dir)
        os.chdir('wget-%s' % self.version)

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
