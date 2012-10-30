# coding: utf-8
import os

from ubik_toolbelt.logger import stream_logger
from ubik_toolbelt.control import Control

from ubik_toolbelt.contrib import which

class Package(Control):
    def __init__(self):
        Control.__init__(self)
        self.name = 'spilleliste'
        self.version = '0.1.0'
        self.release = '0'
        self.requires = []
        self.arch = ''
        self.dist = ''
        self.vers = ''
        self.description = 'Spilleliste read your iTunes playlist and generate for you a simple but beautiful html page to share with your friends with all the Spotify links (Youtube fallback) you want.'

        self.cur_dir = os.getcwd()
        self.src_dir = os.path.join(os.getcwd(), 'source')
        self.pkg_dir = os.path.join(os.getcwd(), 'build')

    def build(self):
        stream_logger.info('Building...')
        
        os.makedirs('%s/bin' % self.src_dir)
        os.chdir('%s/bin' % self.src_dir)

        os.system('curl -o spilleliste https://raw.github.com/Socketubs/Spilleliste/master/spilleliste')
        os.system('chmod +x spilleliste')

    def package(self):
        stream_logger.info('Packaging...')
        os.system('cp -rp %s/* %s' % (self.src_dir, self.pkg_dir))

    def pre_install(self):
        if which('pip-2.7'):
            os.system('pip-2.7 install jinja2 requests docopt appscript')
        elif which('pip2'):
            os.system('pip2 install jinja2 requests docopt appscript')
        elif which('easy_install2'):
            os.system('easy_install install jinja2 requests docopt appscript')
        elif which('easy_install-2.7'):
            os.system('easy_install-2.7 install jinja2 requests docopt appscript')
        else:
            stream_logger.info('Error: I cant find you Python package command (pip, easy_install).')
            sys.exit(1)

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
