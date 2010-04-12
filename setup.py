from setuptools import setup, find_packages
import os

version = '1.0a8'

setup(name='plone.app.dexterity',
      version=version,
      description="Integrates the Dexterity content type system into Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone ttw dexterity schema interface',
      author='Martin Aspeli, David Glick, et al',
      author_email='dexterity-development@googlegroups.com',
      url='http://plone.org/products/dexterity',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone','plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.monkeypatcher',
          'five.localsitemanager>=1.1',
          # ^^ required to fix a bug that affects content with __parent__ pointers set
          'plone.app.content',
          'plone.app.jquerytools',
          'plone.app.relationfield',
          'plone.app.textfield',
          'plone.app.z3cform>=0.4.6',
          'plone.behavior>=1.0b5',
          'plone.contentrules',
          'plone.dexterity',
          'plone.directives.form>=1.0b3',
          'plone.directives.dexterity',
          'plone.formwidget.autocomplete',
          'plone.formwidget.contenttree',
          'plone.formwidget.namedfile',
          'plone.portlets',
          'plone.scale >=2.0a2',
          'plone.schemaeditor >=1.0a4dev-r35539',
          'plone.supermodel>=1.0b2',
          'plone.z3cform>=0.5.5',
          'Products.CMFCore',
          'setuptools',
          # Zope 2
          'zope.interface',
          'zope.component',
          'zope.schema',
          'zope.publisher',
          'z3c.form',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
