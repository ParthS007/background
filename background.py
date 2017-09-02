#!/usr/bin/env python

import multiprocessing
import concurrent.futures

from decorator import decorator

def default_n():
    return multiprocessing.cpu_count()

n = default_n()
pool = concurrent.futures.ThreadPoolExecutor(max_workers=n)
callbacks = []
results = []

def run(f, *args, **kwargs):

    pool._max_workers = n
    pool._adjust_thread_count()

    f = pool.submit(f, *args, **kwargs)
    results.append(f)

    return f

@decorator
def task(f, *args, **kwargs):
    result = run(f, *args, **kwargs)
    results.append(result)

    for cb in callbacks:
        result.add_done_callback(cb)

    return result

def callback(f):
    callbacks.append(f)
    def register_callback():
        f()
    return register_callback
