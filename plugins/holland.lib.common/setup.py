import sys
from setuptools import setup, find_packages

version = "1.1.18"
if sys.version_info[0] == 2:
    install_requires = (["subprocess32"],)
else:
    install_requires = ([""],)

setup(
    name="holland.lib.common",
    version=version,
    description="Common modules used by Holland plugins",
    long_description="""\
""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="holland lib common",
    author="Rackspace",
    author_email="holland-devel@googlegroups.com",
    url="http://www.hollandbackup.org/",
    license="GPLv2",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
    entry_points="""
      # -*- Entry points: -*-
      """,
    namespace_packages=["holland", "holland.lib"],
)
