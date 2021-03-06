from setuptools import setup

setup(name='socialblade',
      version='1.0.5.1',
      description='Object oriented SocialBlade API wrapper',
      long_description=open('README.rst', 'r').read() ,
      author='sl4v',
      author_email='iamsl4v@gmail.com',
      url='https://github.com/sl4vkek/python-socialblade',
      packages=['socialblade'],
      install_requires=['cloudscraper', 'dateparser'],
      license="UNLICENSE"
     )
