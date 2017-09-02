#!/usr/bin/env python

import multiprocessing
import concurrent.futures


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


def task(f, *args, **kwargs):
    def do_task():
        result = run(f, *args, **kwargs)
        results.append(result)

        for cb in callbacks:
            result.add_done_callback(cb)

        return result
    return do_task


def callback(f):
    callbacks.append(f)

    def register_callback():
        f()

    return register_callback
