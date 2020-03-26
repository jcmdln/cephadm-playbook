cephadm-ansible
===================
**Automate deploying Ceph using cephadm and docker at scale**

About
===================
[cephadm-ansible] exists to utilize the upstream [Ceph Orchestrator]
and its SSH module wrapped in an Ansible playbook that deploys and
isolates services using [docker]. The intention is to explore creating
an alternative to [ceph-ansible] that more closely aligns with the
needs and deployment strategy employed by [kolla-ansible].

This playbook will allow a user to deploy a standalone [Ceph] cluster
that trivializes integrating with [kolla-ansible], and follows
official [Ceph] recommended practices by default.

Goals
===================
* Deploying must be relatively trivial, with clear directions
* Purging a cluster must revert _all_ changes, with _no_ side effects
* Updating must be seemless, regardless of minor/patch version changes
* Upgrading must be seemless, regardless of major version changes
* All of the above must also work **flawlessly** with [kolla-ansible]

Platform Support
==============================
| Operating System   | Quality |
| ------------------ | ------- |
| CentOS 8.x         | None, planned
| Ubuntu 18.04 LTS   | None, planned

Usage
===================

Setup
-------------------
```sh
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ curl -L -o venv/bin/cephadm \
    https://raw.githubusercontent.com/jcmdln/ceph/octopus/src/cephadm/cephadm
(venv) $ chmod +x venv/bin/cephadm
```

Quick Start
-------------------

1. Deploy this playbook

  ```sh
  $ ansible-playbook site.deploy.yml
  ```

5. Purge the deployment and its configuration

  ```sh
  $ ansible-playbook site.purge.yml
  ```

Methodology
==============================
A loose, un-ordered series of notes about how things are designed.

* All variables are prefixed with `ceph_*`, hopefully allowing this
  playbook to be imported into others without much hassle.
* There's no point in making gratuitous re-declarations of BlueStore
  defaults.  If Ceph has default settings, **use them**.
* If anything can be calculated reliably, do some math rather than
  providing a list or range of options.
* Before deploying, users must feel safe that our `check.yml` play
  caught any potential issues.

[ceph]: ceph.com
[ceph orchestrator]: https://docs.ceph.com/docs/master/mgr/orchestrator_cli/
[ceph-ansible]: https://github.com/ceph/ceph-ansible
[cephadm]: https://docs.ceph.com/docs/master/bootstrap
[cephadm-ansible]: https://github.com/jcmdln/cephadm-ansible
[kolla-ansible]: https://github.com/openstack/kolla-ansible
