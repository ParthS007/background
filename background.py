#!/usr/bin/env python

import multiprocessing
import concurrent.futures

from decorator import decorator


class Worker(object):
    """A Background Worker."""

    def __init__(self, n=None, use_subprocess=False):
        self.n = n
        self.use_subprocess = use_subprocess

        self.configure_n()

        if self.uses_subprocess:
            self.pool = concurrent.futures.ProcessPoolExecutor(max_workers=self.n)
        else:
            self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=self.n)

    @property
    def uses_threads(self):
        return not self.uses_subprocess

    @property
    def uses_subprocess(self):
        return self.use_subprocess

    def configure_n(self):
        if self.n is None:
            self.n = multiprocessing.cpu_count()

    # @decorator
    def run(self, f, *args, **kwargs):
        self.pool.submit(f, *args, **kwargs)


default_worker = Worker()


@decorator
def task(f, *args, **kwargs):
    return default_worker.run(f)

