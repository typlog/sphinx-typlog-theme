How To Use
==========

Guide on how to use **sphinx typlog theme**.

Installation
------------

Installing **sphinx typlog theme** is easy with pip::

    $ pip install sphinx-typlog-theme

You can also add ``sphinx-typlog-theme`` into your **requirements.txt**.

How to Use
----------

To use **sphinx typlog theme** in your documentation, configure it in
``conf.py``::

    html_theme = 'sphinx_typlog_theme'

If you are using Sphinx < 1.7, you can add it into ``html_theme_path``::

    import sphinx_typlog_theme
    html_theme_path = [sphinx_typlog_theme.get_path()]

Other Options
-------------

In ``conf.py``, there are lots of :ref:`options` to be configured.
