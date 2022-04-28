#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
