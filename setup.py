# ua2nx
# See full license in LICENSE

from setuptools import setup

# provide a long description using reStructuredText
long_description = """
ua2nx is a module that converts UrbanAccess graph into NetworkX MultiDiGraph.
"""

with open('requirements.txt') as f:
    requirements_lines = f.readlines()
install_requires = [r.strip() for r in requirements_lines]

# now call setup
setup(name='ua2nx',
      version='0.0.1',
      description='Converts UrbanAccess graph into NetworkX MultiDiGraph',
      long_description=long_description,
      url='https://github.com/htenkanen/ua2nx',
      author='Henrikki Tenkanen',
      author_email='henrikki@mapple.fi',
      license='MIT',
      platforms='any',
      packages=['ua2nx'],
      install_requires=install_requires,
      include_package_data=True
      )
