#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents
   of the web_static folder of your AirBnB Clone repo.
"""
from os import path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Creates a tar gzipped(.tgz) archive of the directory `web_static`."""
    dt = datetime.utcnow()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                            dt.month,
                                                            dt.day,
                                                            dt.hour,
                                                            dt.minute,
                                                            dt.second)
    if path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive)).failed is True:
        return None
    return archive
