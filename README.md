ceph-playbook
==============================

This Ansible Playbook uses the new Ceph Orchestrator SSH module to
provision a Ceph cluster.

* https://docs.ceph.com/docs/nautilus/start/
* https://docs.ceph.com/docs/nautilus/mgr/orchestrator_cli/


Why?
==============================

[ceph-ansible] is alright, but:
* The documentation is imprecise
* Requires a disjointed mix of Ansible and in-situ CLI to manage things
* Doesn't follow upstream Ceph recommendations

[ceph-deploy] is closer, but:
* Is a bit too manual

What can we do to improve deploying Ceph clusters?

[ceph-ansible]: https://github.com/ceph/ceph-ansible
[ceph-deploy]: https://github.com/ceph/ceph-deploy


Goals
==============================
* Follow Ceph recommendations
* Use Ansible to deploy, CLI to manage
* Documentation per-file and formal usage information
* Use [systemd-nspawn] to control resources


Usage
==============================

TBD

```sh
$ wew lad
```
