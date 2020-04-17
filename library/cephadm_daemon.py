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

    r["command"] = "%s deploy" % r["command"]

    r["rc"], r["stdout"], r["stderr"] = m.run_command(r["command"], check_rc=False)

    if r["rc"] > 0:
        r["changed"] = True
        r["msg"] = "received a non-zero exit code"

    return r


def ls(r, m):
    """
    List daemon(s).
    """

    r["command"] = "%s ls" % r["command"]

    if m.params["no_detail"]:
        r["command"] = "%s --no-detail" % r["command"]

    r["rc"], r["stdout"], r["stderr"] = m.run_command(r["command"], check_rc=False)

    if r["rc"] > 0:
        r["changed"] = True
        r["msg"] = "received a non-zero exit code"

    return r


def rm_daemon(r, m):
    """
    Remove a daemon.
    """

    r["command"] = "%s rm-daemon" % r["command"]

    r["rc"], r["stdout"], r["stderr"] = m.run_command(r["command"], check_rc=False)

    if r["rc"] > 0:
        r["changed"] = True
        r["msg"] = "received a non-zero exit code"

    return r


def rm_cluster(r, m):
    """
    Remove all daemons.
    """

    r["command"] = "%s rm-cluster" % r["command"]

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
            "fsid": {"type": "str", "default": ""},
            "key": {"type": "str", "default": ""},
            "keyring": {"type": "str", "default": ""},
            "list": {"type": "bool", "default": False},
            "name": {
                "type": "str",
                "choices": ["*", "grafana", "mgr", "mon", "osd", "prometheus"],
            },
            "no_detail": {"type": "bool", "default": False},
            "osd_fsid": {"type": "str", "default": ""},
            "reconfig": {"type": "bool", "default": False},
            "skip_firewalld": {"type": "bool", "default": False},
            "state": {"type": "str", "choices": ["absent", "present"],},
        },
        mutually_exclusive=[
            ["allow_ptrace", "force"],
            ["allow_ptrace", "force_delete_data"],
            ["allow_ptrace", "force"],
            ["allow_ptrace", "force_delete_data"],
            ["allow_ptrace", "list", "fsid"],
            ["allow_ptrace", "list", "name"],
            ["allow_ptrace", "list", "reconfig"],
            ["allow_ptrace", "list", "skip_firewalld"],
            ["allow_ptrace", "list", "state"],
            ["allow_ptrace", "no_detail", "fsid"],
            ["allow_ptrace", "no_detail", "name"],
            ["allow_ptrace", "no_detail", "reconfig"],
            ["allow_ptrace", "no_detail", "skip_firewalld"],
            ["allow_ptrace", "no_detail", "state"],
        ],
        required_if=[["state", "absent", ["fsid"]], ["state", "present", ["fsid"]]],
        required_one_of=[["list", "state"]],
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
        if module.params["name"] == "*":
            result = rm_cluster(result, module)
        else:
            result = rm_daemon(result, module)

    if module.params["state"] == "present":
        result = deploy(result, module)

    if module.params["list"]:
        result = ls(result, module)

    if result["rc"] > 0:
        module.fail_json(**result)
    else:
        module.exit_json(**result)


if __name__ == "__main__":
    main()
