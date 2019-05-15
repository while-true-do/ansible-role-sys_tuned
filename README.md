<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_tuned.svg)](https://github.com/while-true-do/ansible-role-sys_tuned/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_tuned.svg)](https://github.com/while-true-do/ansible-role-sys_tuned/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_tuned.svg)](https://github.com/while-true-do/ansible-role-sys_tuned/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_tuned.svg)](https://github.com/while-true-do/ansible-role-sys_tuned/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_tuned.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_tuned)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_tuned%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_tuned)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_tuned%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_tuned)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_tuned%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_tuned)

# Ansible Role: sys_tuned

An Ansible Role to install and configure [tuned](https://tuned-project.org/).

## Motivation

Tuned is a very powerful tool to configure kernel parameters and Linux Systems.

## Description

This role installs tuned and set a proper profile for the system.

## Requirements

Used Modules:

-   [Ansible Module Package](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Module Service](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Module Shell](https://docs.ansible.com/ansible/latest/modules/shell_module.html)
-   [Ansible Module Command](https://docs.ansible.com/ansible/latest/modules/command_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_tuned)
```
ansible-galaxy install while_true_do.sys_tuned
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_tuned)
```
git clone https://github.com/while-true-do/ansible-role-sys_tuned.git while_true_do.sys_tuned
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.sys_tuned

# Additional profile packages are possible
wtd_sys_tuned_packages:
  - tuned
  - tuned-profiles-cpu-partitioning
# State can be present|latest|absent
wtd_sys_tuned_packages_state: "present"

wtd_sys_tuned_service: "tuned"
# State can be started|stopped|restarted
wtd_sys_tuned_service_state: "started"
wtd_sys_tuned_service_enabled: true

# Which profile to use
# auto|balanced|virt-guest|powersave|hpc-compute|desktop|etc...
# check with "tuned-adm list"
wtd_sys_tuned_profile: "auto"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_tuned
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_tuned/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_tuned/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
