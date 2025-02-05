from setuptools import setup, find_packages

setup(
    name='midi-drums-converter',
    version='0.1.0',
    author='Diogo Guimaraes',
    author_email='diogo.m.guimaraes.92@gmail.com',
    description='A MIDI file converter for EZ Drummer 3 to PV edition.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'mido',
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)