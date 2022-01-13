#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import fabric.api as fabric_api
import os


fabric_api.env.hosts = ["34.73.0.174", "34.75.208.81"]
"""The list of host server IP addresses."""


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        fabric_api.put(archive_path, "/tmp/{}".format(file_name))
        fabric_api.run("mkdir -p {}".format(folder_path))
        fabric_api.run(
            "tar -xzf /tmp/{} -C {}".format(file_name, folder_path)
        )
        fabric_api.run("rm /tmp/{}".format(file_name))
        fabric_api.run(
            "mv {}web_static/* {}".format(folder_path, folder_path)
        )
        fabric_api.run("rm -rf {}web_static".format(folder_path))
        fabric_api.run("rm -rf /data/web_static/current")
        fabric_api.run(
            "ln -s {} /data/web_static/current".format(folder_path)
        )
        success = True
    except Exception:
        success = False
    return success
