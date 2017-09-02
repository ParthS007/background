background: does what it says it does
=====================================

This module makes it stupidly simple to run things in the background of your
application, be it a CLI app, or a web app.


Basic Usage
-----------

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
