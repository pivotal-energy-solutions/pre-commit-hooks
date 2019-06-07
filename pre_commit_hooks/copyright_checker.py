from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import datetime
import io
import re

now = datetime.datetime.now()

COPYRIGHT = "Copyright 2011-%s Pivotal Energy Solutions. All rights reserved." % now.strftime("%Y")


def has_author(data):
    for line in data:
        if re.match(r'^__author__\b', line):
            return True
    return '__author__ = \'<FULL_NAME>\''


def has_date(data):
    for line in data:
        if re.search(r'^__date__\b', line):
            return True
    return '__date__ = \'%s\'' % now.strftime('%m/%d/%Y %H:%M %p')


def has_copyright(data):
    for line in data:
        if re.search(r'^__copyright__\b', line):
            return True
    return '__copyright__ = \'%s\'' % COPYRIGHT


def has_credits(data):
    for line in data:
        if re.search(r'^__credits__\b', line):
            return True
    return '__credits__ = [\'<FULL_NAME>\', ]'


def main(argv=None):
    parser = argparse.ArgumentParser(description='Checker for copyright declaration.')
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        errors = []
        data = io.open(filename).readlines()
        for method in [has_author, has_date, has_copyright, has_credits]:
            valid = method(data)
            if valid is not True:
                errors.append(valid)

        if len(errors):
            retv = 1

            print("\n%s is missing the following lines (insert after imports):" % filename)
            for item in errors:
                print(" " + item)

    return retv

if __name__ == '__main__':
    exit(main())