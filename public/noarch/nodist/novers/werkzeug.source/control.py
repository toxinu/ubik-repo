# coding: utf-8
import os

from ubik.core import conf

from ubik_toolbelt.logger import stream_logger
from ubik_toolbelt.control import Control

from ubik_toolbelt.contrib import get_md5

from shutil import copy2 as copy
from shutil import rmtree

class Package(Control):
    def __init__(self):
        Control.__init__(self)
        self.name = 'werkzeug'
        self.version = '0.8.3'
        self.release = '0'
        self.requires = []
        self.arch = ''
        self.dist = ''
        self.vers = ''
        self.description = 'Environment runtime detection (Python,Linux,Distribution,etc...)'

        self.cur_dir = os.getcwd()
        self.src_dir = os.path.join(os.getcwd(), 'source')
        self.pkg_dir = os.path.join(os.getcwd(), 'build')

        self.archive_name = "Werkzeug-%s.tar.gz" % self.version
        self.dir_name = "Werkzeug-%s" % self.version

        self.url = "http://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-%s.tar.gz#md5=12aa03e302ce49da98703938f257347a" % self.version
        self.md5 = self.url.split('#md5=')[-1]

    def build(self):
        stream_logger.info('Building...')
        if not os.path.exists(os.path.join(self.src_dir, self.archive_name)):
            os.system('wget %s' % self.url)
        else:
            if get_md5(os.path.join(self.src_dir, self.archive_name)) != self.md5:
                os.system('wget %s' % self.url)
        rmtree(self.dir_name)
        os.system('tar xvf %s' % self.archive_name)

    def package(self):
        stream_logger.info('Packaging...')
        if not os.path.exists(os.path.join(self.pkg_dir, 'tmp', 'ubik')):
            os.makedirs(os.path.join(self.pkg_dir, 'tmp', 'ubik'))
        copy(os.path.join(self.src_dir, self.archive_name), os.path.join(self.pkg_dir, 'tmp', 'ubik'))

    def pre_install(self):
        pass

    def post_install(self):
        # Go to tmp and extract pacakge
        os.chdir(os.path.join(conf.get('settings', 'packages'), 'tmp', 'ubik'))
        os.system('tar xvf %s' % self.archive_name)
        # Go into package and install it
        os.chdir(self.dir_name)
        os.system('python setup.py install --no-compile --prefix=%s' % conf.get('settings', 'packages'))
        # Clean package dir and archive
        os.chdir(os.path.join(conf.get('settings', 'packages'), 'tmp', 'ubik'))
        rmtree(self.dir_name)
        os.remove(self.archive_name)

    def pre_upgrade(self):
        pass

    def post_upgrade(self):
        # Go to tmp and extract pacakge
        os.chdir(os.path.join(conf.get('settings', 'packages'), 'tmp', 'ubik'))
        os.system('tar xvf %s' % self.archive_name)
        # Go into package and install it
        os.chdir(self.dir_name)
        os.system('python setup.py install --upgrade --no-compile --prefix=%s' % conf.get('settings', 'packages'))
        # Clean package dir and archive
        os.chdir(os.path.join(conf.get('settings', 'packages'), 'tmp', 'ubik'))
        rmtree(self.dir_name)
        os.remove(self.archive_name)

    def pre_remove(self):
        pass

    def post_remove(self):
        pass
