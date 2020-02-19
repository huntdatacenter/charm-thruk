# Thruk

![GitHub Action CI badge](https://github.com/huntdatacenter/charm-thruk/workflows/ci/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This subordinate charm deploys [Thruk][thruk] alongside Nagios deployed with the [`nagios`][nagios-charm] charm.
The charm installs Thruk from the [Consol Labs Repository][consol-labs] from [Consol][consol].

## Usage

Here is an example to get going:

```
juju deploy cs:~huntdatacenter/thruk
juju deploy nagios
juju add-relation nagios:juju-info thruk:juju-info
```

## Development

Here are some helpful commands to get started with development and testing:

```
$ make help
lint                 Run linter
build                Build charm
deploy               Deploy charm
upgrade              Upgrade charm
force-upgrade        Force upgrade charm
test-xenial-bundle   Test Xenial bundle
test-bionic-bundle   Test Bionic bundle
push                 Push charm to stable channel
clean                Clean .tox and build
help                 Show this help
```

## Further information

### Links

- [Thruk project][thruk]
- [Thruk documentation][thruk-docs]
- [Consol Labs repository][consol-labs]
- [ConSol Consulting & Solutions Software GmbH][consol]

[thruk]: https://www.thruk.org
[thruk-docs]: https://www.thruk.org/documentation/
[consol]: https://consol.de/
[consol-labs]: https://labs.consol.de/
[nagios-charm]: https://jaas.ai/nagios
