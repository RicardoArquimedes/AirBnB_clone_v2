#!/usr/bin/python3
""" Write a Fabric script """
from fabric.api import local, env, run, put
from datetime import datetime
from os.path import exists

env.hosts = ['35.190.136.16', '35.231.20.58']


def do_pack():
    """ function that packs archives """
    local('mkdir -p versions')
    date = datetime.now()
    t_file = local('tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz web_static'
                   .format(date.year, date.month, date.day,
                           date.hour, date.minute, date.second), capture=True)
    if t_file.succeeded:
        return t_file
    return None


def do_deploy(archive_path):
    """[summary]"""
    if exists(archive_path):
        file_path = archive_path.split("/")[1]
        serv_path = "/data/web_static/releases/{}".format(
            file_path.replace(".tgz", ""))
        put('{}'.format(archive_path), '/tmp/')
        run('mkdir -p {}'.format(serv_path))
        run('tar -xzf /tmp/{} -C {}/'.format(
            file_path,
            serv_path))
        run('rm /tmp/{}'.format(file_path))
        run('mv -f {}/web_static/* {}/'.format(serv_path, serv_path))
        run('rm -rf {}/web_static'.format(
            serv_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(
            serv_path))
        return True
    else:
        return False


def deploy():
    """ Summary """
    archive = do_pack()
    if archive is None:
        return False
    else:
        value = archive.__dict__["command"].split(" ")[-2]
        print(value)
        return do_deploy(value)
