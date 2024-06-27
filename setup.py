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
      version='0.0.5',
      description='Converts UrbanAccess graph into NetworkX MultiDiGraph',
      long_description=long_description,
      url='https://github.com/htenkanen/ua2nx',
      download_url='https://github.com/htenkanen/ua2nx/archive/v_04.tar.gz',
      author='Henrikki Tenkanen',
      author_email='henrikki@mapple.fi',
      license='MIT',
      platforms='any',
      packages=['ua2nx'],
      install_requires=install_requires,
      include_package_data=True,

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6'
        ],
      )
