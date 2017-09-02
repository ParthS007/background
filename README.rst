background: does what it says it does
=====================================

This module makes it stupidly simple to run things in the background of your
application, be it a CLI app, or a web app.

Work in progress.


Usage
-----

::

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

::

    from background import Worker

    worker = Worker(n=10, use_subprocess=True)

    @worker.task
    def work():
        import time
        time.sleep(10)

    for _ in range(100):
        work()