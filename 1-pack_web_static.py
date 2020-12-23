#!/usr/bin/python3
"""contains do_pack"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """generates .tgz archive from web_static"""
    local('mkdir -p versions')
    tgzname = "web_static_{}.tgz".format((datetime.now()).strftime("%Y%m%d%H%M%S"))
    try:
        return local('tar -cvzf versions/{} web_static'.format(tgzname))
    except Exception:
        return None
