#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Johnathan C. Maudlin <jcmdln@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import)
from ansible.module_utils.basic import AnsibleModule


def main():
    module_args = {
        'config': {},
        'fsid': {},
        'dashboard': {
            'type': 'bool',
            'default': False,
        },
        'dashboard_user': {
            'type': 'str',
            'default': ''
        },
        'dashboard_password': {
            'type': 'str',
            'default': ''
        },
        'skip_ping_check': {},
        'skip_pull': {},
    }

    module = AnsibleModule(
        argument_spec=module_args,
    )

    result = {
        'changed': False,
        'command': '',
        'msg': 'no action performed',
        'rc': 0,
        'stderr': '',
        'stdout': '',
    }


if __name__ == '__main__':
    main()
