#!/usr/bin/env python
import os, sys
from pathlib import Path

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_counter_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Is it installed?") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
