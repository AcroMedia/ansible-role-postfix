import os
import pytest
import testinfra.utils.ansible_runner
import testinfra


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


""" helper functions"""


def check_file(filepath, user, group, permission):

    assert filepath.exists
    assert filepath.user == user
    assert filepath.group == group
    assert oct(filepath.mode) == permission


# passable test for debugging baseline (get something working!)
def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


""" tasks/main.yml tests """


def test_pkg(host):
    mailx = host.package("mailx")
    mailutils = host.package('mailutils')

    assert mailx.is_installed or mailutils.is_installed


@pytest.mark.parametrize('files', [
    '/etc/aliases', '/etc/postfix/main.cf'
])
def test_alias_exists(host, files):
    test_files = [files]
    [check_file(host.file(x), 'root', 'root', '0o644') for x in test_files]
