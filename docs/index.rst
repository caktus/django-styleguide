

Welcome to django-styleguide documentation!
===========================================

An app to manage a live style guide in your Django project.

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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

