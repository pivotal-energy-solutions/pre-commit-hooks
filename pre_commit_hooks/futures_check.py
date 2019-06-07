from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import io
import re


def has_future_import(import_name, data):
    for line in data:
        if re.match(r'^from __future__ import %s' % import_name, line):
            return True
    return 'from __future__ import %s' % import_name


def main(argv=None):
    parser = argparse.ArgumentParser(description='Checker for copyright declaration.')
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        errors = []
        data = io.open(filename).readlines()
        for future_import in ['absolute_import', 'print_function', 'unicode_literals']:
            valid = has_future_import(future_import, data)
            if valid is not True:
                errors.append(valid)

        if len(errors):
            retv = 1

            print("\n%s is missing the following future lines (insert at top):" % filename)
            for item in errors:
                print(" " + item)

    return retv


if __name__ == '__main__':
    exit(main())