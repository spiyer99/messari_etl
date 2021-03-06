from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='messari_etl',
    url='https://github.com/spiyer99/messari_etl',
    author='Neel Iyer',
    author_email='neel.r.iyer@gmail.com',
    # Needed to actually package something
    packages=['messari_etl'],
    # Needed for dependencies
    install_requires=['pandas', 'requests'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Unofficial Python Wrapper for Messari data',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)