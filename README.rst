.. image:: https://img.shields.io/pypi/pyversions/background.svg
   :target: https://pypi.org/pypi/background

.. image:: https://github.com/ParthS007/background/workflows/CI/badge.svg
   :target: https://github.com/ParthS007/background/actions

Background
=======================================

It runs stuff in the background.

    "An elegant decorator-based abstraction around Python 3's concurrent.futures ThreadPoolExecutor class" 

    — Simon Willison

This module makes it stupidly simple to run things in the background of your
application, be it a CLI app, or a web app.

Basic Usage
-----------

.. code:: python


    import time

    import background


    @background.task
    def work():
        # Do something expensive here.
        time.sleep(10)


    for _ in range(100):
        work()


Advanced Usage
--------------

.. code:: python

    import time

    import background

    # Use 40 background threads.
    background.n = 40
    

    @background.task
    def work():
        time.sleep(10)
        return "Done!"

    @background.callback
    def work_callback(future):
        print(future.result())


    for _ in range(100):
        work()

Installation
------------

::

    $ pipenv install background
    ✨🍰✨
