#!/usr/bin/env python

from charmhelpers.contrib.ansible import apply_playbook
from charmhelpers.core.hookenv import status_set
from charms.reactive.decorators import hook
from charms.reactive.decorators import when
from charms.reactive.decorators import when_not
from charms.reactive.flags import clear_flag
from charms.reactive.flags import register_trigger
from charms.reactive.flags import set_flag

register_trigger(when='config.changed',
                 clear_flag='thruk.configured')


@when_not('thruk.installed')
def install_thruk():
    status_set('maintenance', 'installing thruk')
    apply_playbook(playbook='ansible/playbook.yaml')
    status_set('active', 'ready')
    set_flag('thruk.configured')
    set_flag('thruk.installed')


@when('thruk.installed')
@when_not('thruk.configured')
def configure_thruk():
    status_set('maintenance', 'configuring thruk')
    apply_playbook(playbook='ansible/playbook.yaml', tags=['config'])
    status_set('active', 'ready')
    set_flag('thruk.configured')


# Hooks
@hook('stop')
def cleanup():
    apply_playbook(playbook='ansible/playbook.yaml', tags=['uninstall'])


@hook('upgrade-charm')
def upgrade_charm():
    clear_flag('thruk.version')
    clear_flag('thruk.installed')
