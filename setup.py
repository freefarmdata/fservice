from setuptools import setup
from fservice import __version__

setup(
    name='fservice',
    version=__version__,    
    description='Stateful service management system',
    url='https://github.com/freefarmdata/fservice',
    author='Jack Mead',
    author_email='jackmead515@gmail.com',
    license='BSD 2-clause',
    packages=['fservice'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)