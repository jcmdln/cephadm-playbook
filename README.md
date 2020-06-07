cephadm-ansible
===================
**Automate deploying Ceph at scale using cephadm and Ansible**

**NOTE**: This has basically reached the point of gross scaffolding
that kind of works.  Don't run this and expect anything positive to
happen, especially not in a production environment.

[cephadm-ansible] is an Ansible playbook that deploys [Ceph] by
automating the use of the new [cephadm] script.  The intention is to
explore creating an alternative to [ceph-ansible] that more closely
aligns with the needs and deployment strategy employed by
[kolla-ansible].  This playbook will allow a user to deploy a
standalone [Ceph] cluster that trivializes integrating with
[kolla-ansible], and follows official [Ceph] recommended practices by
default.

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
This section covers how to use this process, outlining how to setup,
configure, deploy/update, and

Setup
-------------------

```sh
$ git clone https://github.com/jcmdln/cephadm-ansible
$ cd cephadm-ansible
$ virtualenv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Configure
-------------------
1. Create your inventory

    Make a copy of `inventory.sample.yml`:

    ```sh
    $ cp {sample.,}inventory.yml
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
within the same release are the same process.

1. (Optional) Fetch the latest commits from the current branch

    ```sh
    $ git pull origin master
    ```

2. Run the playbook

    ```sh
    $ ansible-playbook -i inventory.yml site.yml
    ```

Currently this process is not foolproof because a baseline of stability
from which to automate changes has not yet been defined.  Consider the
above to probably work, and expect to roll up your sleeves and have to
do some work.

Purging
-------------------
Destroying a [Ceph] cluster requires using `cephadm rm-cluster` and is
not handled automatically by this playbook.  The mentioned command does
simplify the process and handles everything, so there's no real need
for additional logic to be added to this playbook.

[cephadm-ansible]: https://github.com/jcmdln/cephadm-ansible

[Ceph]: https://ceph.io/
[Ceph Orchestrator]: https://docs.ceph.com/docs/octopus/mgr/orchestrator/
[Ceph Orch]: https://docs.ceph.com/docs/octopus/mgr/orchestrator/
[cephadm]: https://docs.ceph.com/docs/octopus/cephadm/
[ceph-ansible]: https://github.com/ceph/ceph-ansible

[kolla-ansible]: https://github.com/openstack/kolla-ansible
