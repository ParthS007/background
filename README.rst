Background: run stuff in the backround
======================================

    "An elegant decorator-based abstraction around Python 3's concurrent.futures ThreadPoolExecutor class" 

    — Simon Wilson

This module makes it stupidly simple to run things in the background of your
application, be it a CLI app, or a web app.

.. image:: https://farm5.staticflickr.com/4296/36137232912_7276365f2e_k_d.jpg

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


    import background

    # Use 40 background threads.
    background.n = 40


    @background.task
    def work():
        import time
        time.sleep(10)

    @background.callback
    def work_callback(future):
        print(future)


    for _ in range(100):
        work()

Installation
------------

::

    $ pipenv install backround
    ✨🍰✨
