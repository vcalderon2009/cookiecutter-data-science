{% if cookiecutter.use_read_the_docs == "RTD" %}
|RTD| |License| |Issues|
{% endif %}

.. _commands_sec:

Commands
========

The Makefile contains the central entry points for common tasks related to this project.

This section is dedicated towards the functions used through the analysis.

.. |Issues| image:: https://img.shields.io/github/issues/{{cookiecutter.github_project}}.svg
    :target: https://github.com/{{cookiecutter.github_project}}/issues
    :alt: Open Issues

.. |RTD| image:: https://readthedocs.org/projects/{{cookiecutter.repo_name|lower|replace(' ', '-')|replace('_', '-')}}/badge/?version=latest
   :target: https://{{cookiecutter.repo_name|lower|replace(' ', '-')|replace('_', '-')}}.rtfd.io/en/latest/
   :alt: Documentation Status







.. ----------------------------------------------------------------------------

Project based on the `modified <https://github.com/vcalderon2009/cookiecutter-data-science-vc>`_  version of
`cookiecutter data science project template <https://drivendata.github.io/cookiecutter-data-science/>`_ 

{% if cookiecutter.open_source_license == "BSD 3-Clause" %}
.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :target: https://github.com/{{cookiecutter.github_project}}/blob/master/LICENSE.rst
    :alt: Project License
{% endif %}

{% if cookiecutter.open_source_license == "GNU GPL v3+" %}
.. |License| image:: https://img.shields.io/badge/license-GNU%20GPL%20v3%2B-blue.svg
    :target: https://github.com/{{cookiecutter.github_project}}/blob/master/LICENSE.rst
    :alt: Project License
{% endif %}

{% if cookiecutter.open_source_license == "Apache Software Licence 2.0" %}
.. |License| image:: https://img.shields.io/badge/license-Apache%20Software%20Licence%202.0-blue.svg
    :target: https://github.com/{{cookiecutter.github_project}}/blob/master/LICENSE.rst
    :alt: Project License
{% endif %}

{% if cookiecutter.open_source_license == "BSD 2-Clause" %}
.. |License| image:: https://img.shields.io/badge/license-BSD%202--Clause-blue.svg
    :target: https://github.com/{{cookiecutter.github_project}}/blob/master/LICENSE.rst
    :alt: Project License
{% endif %}

{% if cookiecutter.open_source_license == "MIT" %}
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/{{cookiecutter.github_project}}/blob/master/LICENSE.rst
   :alt: Project License
{% endif %}