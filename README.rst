

django-styleguide
========================

Welcome to the documentation for django-styleguide!

**Vision**

* Develop an evolving foundation of base HTML/CSS patterns
* They can be styled and extended to meet the needs of specific projects
* The result, a live style guide, is embedded in the Django project and uses the project CSS
* A complementary tool to django-comps, which is for building full pages

**Goals**

* Installed via a pluggable Django app
    * Possible to add to existing projects
* Accessible on staging server to show clients (e.g. /style-guide/)
    * Bundled into the django-project-template
    * Enabled automatically within the template
* Uses project styles
    * All simple Django templates
    * Uses project CSS files directly so style guide and project run on same code
* Easily extensible when adding new project patterns/widgets
    * No URLs/views
    * Just drop a new HTML/CSS template into a specific directory
    * Style guide menu is auto generated from file structure and adds new menu items
* Show how to use widgets
    * Copy/pasteable code snippets with syntax highlighting


Documentation
-----------------------------------

Documentation on using django-styleguide is available on 
`Read The Docs <http://readthedocs.org/docs/django-styleguide/>`_.


Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py


License
--------------------------------------

django-styleguide is released under the BSD License. See the 
`LICENSE <https://github.com/caktus/django-styleguide/blob/master/LICENSE>`_ file for more details.


Contributing
--------------------------------------

If you think you've found a bug or are interested in contributing to this project
check out `django-styleguide on Github <https://github.com/caktus/django-styleguide>`_.

Development sponsored by `Caktus Consulting Group, LLC
<http://www.caktusgroup.com>`_.
