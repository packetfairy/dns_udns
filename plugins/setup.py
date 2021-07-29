from setuptools import setup

setup(
    name='dns_udns',
    package='dns_udns.py',
    install_requires=[
        'certbot',
        'zope.interface',
    ],
    entry_points={
        'certbot.plugins': [
            'dns_udns = dns_udns:Authenticator',
        ],
    },
)
