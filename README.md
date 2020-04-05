cephadm-ansible
===================
**Automate deploying Ceph at scale using cephadm and Ansible**

[cephadm-ansible] is an Ansible playbook that deploys [Ceph] by
automating the use of the new [cephadm] script.  The intention is to
explore creating an alternative to [ceph-ansible] that more closely
aligns with the needs and deployment strategy employed by
[kolla-ansible].

This playbook will allow a user to deploy a standalone [Ceph] cluster
that trivializes integrating with [kolla-ansible], and follows
official [Ceph] recommended practices by default.

If you are new to [Ceph], please see the following:
* https://docs.ceph.com/docs/octopus/start/hardware-recommendations/
* https://docs.ceph.com/docs/octopus/start/os-recommendations/
* https://docs.ceph.com/docs/octopus/cephadm/


Goals
===================
* Deploying must be relatively **trivial**, with clear directions
* Deploying and Updating in the same Ceph release must be **boring**
* Purging a cluster must revert all changes, with **no side effects**
* Upgrading to a newer Ceph release must be **seemless**
* All of the above must also work **flawlessly** with [kolla-ansible]


Usage
===================
TODO: clarify this section

Installation
-------------------
TODO: clarify this section

```sh
$ virtualenv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Setup
-------------------
1. Create your inventory

    Make a copy of `inventory.sample.yml`:

    ```sh
    $ cp inventory{.sample,}.yml
    ```

    Read over the created `inventory.yml` and add your hosts as outlined
    in the comments above each defined group.

2. Define your configuration

    Make a copy of `group_vars/all.sample.yml`:

    ```sh
    $ cp group_vars/all{.sample,}.yml
    ```

    Read over the created `group_vars/all.yml` and adjust the variables
    as outlined in the comments in each section.

Deploying / Updating
-------------------
The process of deploying a [Ceph] cluster as well as updating it
within the same release are the same single-step process:

```sh
$ ansible-playbook -i inventory.yml site.deploy.yml
```

Purging
-------------------
Destroying a [Ceph] cluster requires specifying the `fsid` of the
cluster to destroy, as well as passing a tag that confirms you really
want to purge.

```sh
$ ansible-playbook -i inventory.yml site.purge.yml \
  --extra-vars "cephadm_cluster_fsid=<fsid>" \
  --tags yes-i-really-really-mean-it
```


[cephadm-ansible]: https://github.com/jcmdln/cephadm-ansible

[Ceph]: https://ceph.io/
[Ceph Orchestrator]: https://docs.ceph.com/docs/octopus/mgr/orchestrator/
[Ceph Orch]: https://docs.ceph.com/docs/octopus/mgr/orchestrator/
[cephadm]: https://docs.ceph.com/docs/octopus/cephadm/
[ceph-ansible]: https://github.com/ceph/ceph-ansible

[kolla-ansible]: https://github.com/openstack/kolla-ansible
