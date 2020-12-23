#!/usr/bin/python3
"""contains do_pack, do_deploy, and deploy"""
from fabric.operations import local
from datetime import datetime
from os import path


def do_pack():
    """generates .tgz archive from web_static"""
    local('mkdir -p versions')
    tgzname = "web_static_{}.tgz".format((datetime.now()).strftime(
        "%Y%m%d%H%M%S"))
    try:
        return local('tar -cvzf versions/{} web_static'.format(tgzname))
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if not path.exists(archive_path):
        return(False)


def deploy():
    fp = do_pack()
    if fp is None:
        return False
    return do_deploy(fp)
