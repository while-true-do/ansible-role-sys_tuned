import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tuned_package(host):
    pkg = host.package("tuned")

    assert pkg.is_installed


def test_tuned_service(host):
    srv = host.service("tuned")

    assert srv.is_running
    assert srv.is_enabled
