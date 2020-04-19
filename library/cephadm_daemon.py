#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Johnathan C. Maudlin <jcmdln@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import
from ansible.module_utils.basic import AnsibleModule

import json


def deploy(r, m):
    """
    Deploy a daemon.
    """

    r["command"] = "%s deploy %s %s" % (
        r["command"],
        m.params["fsid"],
        m.params["name"],
    )

    if m.params["name"] == "osd":
        r["command"] = "%s --osd-fsid %s" % (r["command"], m.params["osd_fsid"])

    if m.params["config"]:
        r["command"] = "%s --config %s" % (r["command"], m.params["config"])

    if m.params["config_json"]:
        r["command"] = "%s --config-json %s" % (r["command"], m.params["config_json"])

    if m.params["key"]:
        r["command"] = "%s --key %s" % (r["command"], m.params["key"])

    if m.params["keyring"]:
        r["command"] = "%s --keyring %s" % (r["command"], m.params["keyring"])

    if m.params["allow_ptrace"]:
        r["command"] = "%s --allow-ptrace" % r["command"]

    if m.params["reconfig"]:
        r["command"] = "%s --reconfig" % r["command"]

    if m.params["skip_firewalld"]:
        r["command"] = "%s --skip-firewalld" % r["command"]

    r["rc"], r["stdout"], r["stderr"] = m.run_command(r["command"], check_rc=False)

    if r["rc"] > 0:
        r["changed"] = True
        r["msg"] = "received a non-zero exit code"

    return r


def rm_daemon(r, m):
    """
    Remove a daemon.
    """

    r["command"] = "%s rm-daemon %s %s" % (
        r["command"],
        m.params["fsid"],
        m.params["name"],
    )

    if m.params["force"]:
        r["command"] = "%s --force" % r["command"]

    if m.params["force_delete_data"]:
        r["command"] = "%s --force-delete-data" % r["command"]

    r["rc"], r["stdout"], r["stderr"] = m.run_command(r["command"], check_rc=False)

    if r["rc"] > 0:
        r["changed"] = True
        r["msg"] = "received a non-zero exit code"

    return r


def main():
    module = AnsibleModule(
        argument_spec={
            "allow_ptrace": {"type": "bool", "default": False},
            "config": {"type": "str", "default": ""},
            "config_json": {"type": "mapping", "default": ""},
            "force": {"type": "bool", "default": False},
            "force_delete_data": {"type": "bool", "default": False},
            "fsid": {"type": "str", "required": True},
            "key": {"type": "str", "default": ""},
            "keyring": {"type": "str", "default": ""},
            "name": {
                "type": "str",
                "choices": [
                    "alertmanager",
                    "crash",
                    "grafana",
                    "iscsi",
                    "mgr",
                    "mon",
                    "nfs",
                    "node-exporter",
                    "osd",
                    "prometheus",
                    "rbd-mirror",
                    "rgw",
                ],
                "required": True,
            },
            "osd_fsid": {"type": "str", "default": ""},
            "reconfig": {"type": "bool", "default": False},
            "skip_firewalld": {"type": "bool", "default": False},
            "state": {
                "type": "str",
                "choices": ["absent", "present"],
                "required": True,
            },
        },
        mutually_exclusive=[
            ["allow_ptrace", "force"],
            ["allow_ptrace", "force_delete_data"],
        ],
    )

    result = {
        "changed": False,
        "command": "cephadm",
        "msg": "no action performed",
        "rc": 0,
        "stderr": "",
        "stdout": "",
    }

    if module.params["state"] == "absent":
        result = rm_daemon(result, module)
    else:
        result = deploy(result, module)

    if result["rc"] > 0:
        module.fail_json(**result)
    else:
        module.exit_json(**result)


if __name__ == "__main__":
    main()
