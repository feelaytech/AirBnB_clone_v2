#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents
   of the web_static folder of your AirBnB Clone repo and distributes it
   to my web servers.
"""
from os import path
from datetime import datetime
from fabric.api import local, env, put, run

env.hosts = ["52.3.252.132", "100.26.132.178"]


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


def do_deploy(archive_path):
    """Distributes an archive to my web servers.
    Args:
        archive_path(str): The path of the archive to distribute.
    Returns:
        True OR,
        If the file doesn't exist at archive_path or an error occurs - False.
    """
    if path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Creates and distributes an archive to my web servers."""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
