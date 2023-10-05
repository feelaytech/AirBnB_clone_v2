#!/usr/bin/python3
"""A Fabric script (based on the file 3-deploy_web_static.py)
   that deletes out-of-date archives.
"""
import os
from fabric.api import *

env.hosts = ["52.3.252.132", "100.26.132.178"]


def do_clean(number=0):
    """Deletes out-of-date archives.
    Args:
        number(int): The number of archives to keep.
    If number is 0 or 1, keep only the most recent archive. If
    number is 2, keep the most and second-most recent archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
