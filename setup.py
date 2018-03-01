from setuptools import setup, find_packages

setup(
    name='django-styleguide',
    version='1.2.4',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(exclude=['sample_project']),
    include_package_data=True,
    url='http://github.com/caktus/django-styleguide/',
    license='BSD',
    description='Styleguide helper for projects that work with design teams',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'bs4',
        "markdown",
    ],
    #long_description=open('README.rst').read(),
    zip_safe=False, # because we're including media that Django needs
)
