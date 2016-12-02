#!/usr/bin/env python2
from fabric.api import abort, task, puts, roles, run, env


@task
def test():
    """
    Our test is so simple
    """
    print('Bobbalob')
