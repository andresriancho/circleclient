# -*- coding: utf-8 -*-

"""
circleclient.cli
~~~~~~~~~~~~~~~~

This module provides the CLI interface to cicleclient.

"""

import os
import argparse
from circleclient import circleclient


def main():
    """Entry point for the application scipt."""
    parser = argparse.ArgumentParser(prog="ccl")
    subparsers = parser.add_subparsers()

    parser_user = subparsers.add_parser(
        'user', help='List information about the user.')
    parser_user.add_argument('--info', '-i', action='store_true',
        default=False)

    parser_projects = subparsers.add_parser(
        'projects', help='List all projects.')

    parser_build = subparsers.add_parser(
        'build', help='Build operations')
    parser_build.add_argument(
        'trigger', action='store', help="Trigger new build")
    parser_build.add_argument(
        '--username', '-u', action='store', help='Username')
    parser_build.add_argument(
        '--branch', '-b', action='store', help="Branch name")

    args = parser.parse_args()

    client = circleclient.CircleClient(os.environ['API_TOKEN'])

    if args.info:
        print(client.user.info())

