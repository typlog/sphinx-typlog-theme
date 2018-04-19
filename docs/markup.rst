Markup Styles
=============

This page is showing markup styles, they have no meanings.

Admonition
----------

.. admonition:: Debug Note

   The default admonition has no colors. It is gray.

.. attention:: Attention please!

.. caution:: Attention please!

.. danger:: This is a danger area.

.. error:: This is an error message.

.. hint:: This is hint message.

.. important:: This is an impoartant message.

.. note::
   This page is showing markup styles, they have no meanings.

   Oh. Except this message.

.. tip:: A small tip please.

.. warning:: Please don't do anything harmful to me.


Sphinx Admonition
-----------------

.. versionadded:: 2.5
   The *spam* parameter.

.. versionchanged:: 2.5
   The *spam* parameter.

.. deprecated:: 3.1
   Use :func:`spam` instead.

.. seealso::
   It is also available at https://typlog.com/

.. centered:: LICENSE AGREEMENT

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

Block Level
-----------

Code
~~~~

Here is an example on code highlight::

    @app.route('/', methods=['GET')
    def hello(name='world'):
        return 'Hello {}'.format(name)

    class API(object):
        """API docstring style"""

        def __init__(self, request):
            # comment
            self.request = request

Quote
~~~~~

Here is an example on block quote:

    | Beautiful is better than ugly.
    | Explicit is better than implicit.
    | Simple is better than complex.
    | Complex is better than complicated.
    | Flat is better than nested.
    | Sparse is better than dense.
    | Readability counts.
    | Special cases aren't special enough to break the rules.
    | Although practicality beats purity.
    | Errors should never pass silently.
    | Unless explicitly silenced.
    | In the face of ambiguity, refuse the temptation to guess.
    | There should be one-- and preferably only one --obvious way to do it.
    | Although that way may not be obvious at first unless you're Dutch.
    | Now is better than never.
    | Although never is often better than *right* now.
    | If the implementation is hard to explain, it's a bad idea.
    | If the implementation is easy to explain, it may be a good idea.
    | Namespaces are one honking great idea -- let's do more of those!

List
~~~~

* Make a list, and its items

  1. Ordered item: foo

     a. A third level item

  2. Ordered item: bar

* The second item has no items
* The third item has unordered items

  * A foo is a foo
  * A bar is a bar

Inline Style
------------

A plain text mixed with **bold** and *italic*. And we have ``code`` too.

Let's try a link https://lepture.com.

Badges
------

Let's have a preview of what badges look like:

* :badge:`done` Add badge role
* :badge:`todo` Add more badge features
* :badge:`doing` Things that in plan
* :badge-red:`remove` Some feature has been removed
* :badge-green:`√`


API References
--------------
