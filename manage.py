#!/usr/bin/env python

import os
import sys

abspath = os.path.abspath(r'./app1')
sys.path.insert(0, abspath)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
