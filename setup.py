from setuptools import setup
from embarcaderomindmachine import __version__

setup(  name='embarcaderomindmachine',
        version=__version__,
        description='The extensible framework for running Github bot flocks.',
        url='https://pages.charlesreid1.com/embarcadero-mind-machine',
        author='charlesreid1',
        author_email='charles@charlesreid1.com',
        test_suite='nose.collector',
        tests_require=['nose'],
        license='MIT',
        packages=['embarcaderomindmachine'],
        install_requires=['PyGithub>=1.39'],
        zip_safe=False)

