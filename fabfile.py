from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.utils import puts

base_path = os.path.abspath(os.path.dirname(__file__))

env.forward_agent = True
env.user = 'ubuntu'
env.host_string = 'cf3.ijs.si:22'

@task
def deploy():
    with cd('/home/ubuntu/cf3/'):
        run('git pull')

        puts(magenta("[Updating containers]"))
        run('docker-compose pull')
        run('docker-compose up -d --build --scale worker=4')
