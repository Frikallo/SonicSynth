from setuptools import setup
from sonicsynth import __version__

setup(
    name='sonicsynth',
    version=__version__,
    description='An audio synthesis library for sound generation and manipulation',
    author='Noah Kay',
    author_email='noahkay13@gmail.com',
    url='https://github.com/Frikallo/sonicsynth',
    packages=['sonicsynth'],
    install_requires=[
        'numpy',
        'scipy',
        'pydub',
    ],
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Multimedia :: Sound/Audio',
    ],
)