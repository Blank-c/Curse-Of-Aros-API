from setuptools import setup, find_packages

setup(
   name='curseofaros',
   version='0.0.1',
   author='Blank-c',
   packages=find_packages(),
   url='https://github.com/Blank-c/Curse-Of-Aros-API',
   description='A python wrapper for Curse Of Aros game leaderboards.',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   install_requires=['aiohttp'],
   keywords='curseofaros'
)