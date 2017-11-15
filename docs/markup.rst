Markup Styles
=============

This page is showing markup styles, they have no meanings.

Admonition
----------

.. admonition:: Debug Note

   The default admonition has no colors. It is gray.

.. note::
   This page is showing markup styles, they have no meanings.

   Oh. Except this message.

.. warning::
   Please don't do anything harmful to me.

.. deprecated:: 3.1
   Use :func:`spam` instead.

Block Level
-----------

Code
~~~~

Here is an example on code highlight::

    def hello(name='world'):
        return 'Hello {}'.format(name)

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


API References
--------------

.. autoclass:: flask.Flask
   :members:
