|RTD| |License| |Issues|

.. _GETTING_STARTED:
************************************************************************
{{cookiecutter.project_name}}
************************************************************************

{{cookiecutter.short_description}}

**Author**: {{ cookiecutter.author_name }} (`{{cookiecutter.author_email}} <mailto:{{cookiecutter.author_email}}>`_)


.. contents:: **Table of Contents**
    :local:

    INSTALL
    ENVIRONMENT

.. |Issues| image:: https://img.shields.io/github/issues/{{cookiecutter.github_project}}.svg
   :target: https://github.com/{{cookiecutter.github_project}}/issues
   :alt: Open Issues

.. |RTD| image:: https://readthedocs.org/projects/{{cookiecutter.repo_name}}/badge/?version=latest
   :target: http://{{cookiecutter.repo_name}}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

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
