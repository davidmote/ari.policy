from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(
    name='ari.policy',
    version=version,
    description='The collection of products required for the ARI website',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/ari.policy',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['ari'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'PIL',
        'plone.app.caching',
        'plone.app.ldap',
        'collective.uploadify',
        'collective.indexing',
        'jyu.z3cform.datepicker',
        'Products.PloneFormGen',

        'avrc.ari.theme',
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
