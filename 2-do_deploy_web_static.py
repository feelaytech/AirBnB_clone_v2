#!/usr/bin/python3
"""A Fabric script (based on the file 1-pack_web_static.py)
   that distributes an archive to my web servers.
"""
from os import path
from fabric.api import env, put, run

env.hosts = ["52.3.252.132", "100.26.132.178"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.
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
