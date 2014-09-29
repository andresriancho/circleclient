# -*- coding: utf-8 -*-

"""
circleclient.cli
~~~~~~~~~~~~~~~~

This module provides the CLI interface to cicleclient.
"""


import argparse
import circleclient


def main():
    """Entry point for the application scipt."""
    parser = argparse.ArgumentParser(prog="ccl")
    subparsers = parser.add_subparsers(help="todo help")

    parser_user = subparsers.add_parser(
        'user', help='List information about the user.')

    parser_projects = subparsers.add_parser(
        'projects', help='List all projects.')

    parser_cache = subparsers.add_parser(
        'cache', help='Clear cache for given project')
    parser_cache.add_argument('username', type=str, help='Username')



if __name__ == "__main__":
    main()
