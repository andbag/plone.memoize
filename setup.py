from setuptools import setup, find_packages

version = '1.1'

setup(name='plone.memoize',
      version=version,
      description="Decorators for caching the values of functions and methods",
      long_description=open("README.txt").read() + '\n' + \
                       open("docs/HISTORY.txt").read(),
      classifiers=[],
      keywords='plone memoize decorator cache',
      author='Martin Aspeli, David "Whit" Morriss and Daniel Nouri',
      author_email='optilude@gmx.net',
      url='http://svn.plone.org/svn/plone/plone.memoize',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'zope.annotation',
        'zope.component',
        'zope.configuration',
        'zope.interface',
        'zope.publisher',
        'zope.testing',
        'zope.app.cache',
        'zope.app.component',
        'zope.app.testing',
        # 'Zope2',
      ],
      )
