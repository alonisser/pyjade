from setuptools import setup,find_packages

setup(name='pyjade',
      version='4.0.0',
      download_url='git@github.com:syrusakbary/pyjade.git',
      packages=find_packages(),
      author='Syrus Akbary',
      author_email='me@syrusakbary.com',
      description='Jade syntax template adapter for Django, Jinja2, Mako and '
                  'Tornado templates',
      long_description=open('README.rst').read(),
      keywords='jade template converter',
      url='http://github.com/syrusakbary/pyjade',
      license='MIT',
      entry_points={
          'console_scripts' : ['pyjade = pyjade.convert:convert_file',]
      },
      install_requires=['six'],
      tests_require=[
            'nose',
            'django',
            'jinja2',
            'tornado',
            'pyramid >= 1.4, <= 1.4.99',
            'mako',
      ])
