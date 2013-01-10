# coding: utf-8
import os
import shutil

from ubik_toolbelt.logger import stream_logger
from ubik_toolbelt.control import Control

from ubik_toolbelt.contrib import get_md5

class Package(Control):
    def __init__(self):
        Control.__init__(self)
        self.name = 'python3'
        self.version = '3.3.0'
        self.release = '0'
        self.requires = []
        self.arch = 'x86_64'
        self.dist = 'ubuntu'
        self.vers = '1204'
        self.description = 'Python 3 interpreter'

        self.cur_dir = os.getcwd()
        self.src_dir = os.path.join(os.getcwd(), 'source')
        self.pkg_dir = os.path.join(os.getcwd(), 'build')

        self.archive_md5 = '198a64f7a04d1d5e95ce2782d5fd8254'

        self.archive_name = 'Python-%s.tgz' % self.version
        self.dir_name = 'Python-%s' % self.version

    def build(self):
        stream_logger.info('=> Building...')
        os.chdir(self.src_dir)
        if not os.path.exists(self.archive_name):
            stream_logger.info('=> Downloading %s' % self.archive_name)
            os.system('wget http://www.python.org/ftp/python/%s/%s' % (self.version, self.archive_name))
        elif get_md5(self.archive_name) != self.archive_md5:
            stream_logger.info('!! Invalid archive md5')
            os.remove(self.archive_name)
            stream_logger.info('=> Downloading %s' % self.archive_name)
            os.system('wget http://www.python.org/ftp/python/%s/%s' % (self.version, self.archive_name))

        if os.path.exists(self.dir_name):
            stream_logger.info('=> Clean old builds')
            shutil.rmtree(self.dir_name)
        stream_logger.info('=> Extract archive')
        os.system('tar xvf %s' % self.archive_name)
        os.chdir(self.dir_name)
        os.system('./configure --prefix=/usr/local/ubik')
        os.system('make')

    def package(self):
        stream_logger.info('=> Packaging...')
        os.chdir(self.src_dir)
        os.chdir(self.dir_name)
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
