import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:
    README = ''
    CHANGES = ''

setup(
    name='Flask-DebugToolbar-LineProfilerPanel',
    description="Panel for the Flask Debug toolbar to capture and view line-by-line profiling stats",
    version='1.0.1',
    url='https://github.com/phleet/flask_debugtoolbar_lineprofilerpanel',

    author='Jamie Wong',
    author_email='jamie.lf.wong@gmail.com',
    long_description=README + '\n\n' + CHANGES,
    license='MIT',

    packages=(
        'flask_debugtoolbar_lineprofilerpanel',
    ),
    include_package_data=True,
    install_requires=[
        'Flask-DebugToolbar',
        'line-profiler>=1.0b3'
    ]
)
