import argparse
import json
import sys
from concurrent.futures import thread
from core import runchecks
from utils import formatoutput

def main():
    parser = argparse.ArgumentParser(description='axogint - email osint tool')
    parser.add_argument('email', help='target email address')
    parser.add_argument('--threads', type=int, default=20, help='number of threads')
    parser.add_argument('--timeout', type=int, default=10, help='request timeout')
    parser.add_argument('--output', choices=['json','table'], default='table', help='output format')
    parser.add_argument('--modules', nargs='+', help='limit to specific modules')
    args = parser.parse_args()

    results = runchecks(args.email, args.threads, args.timeout, args.modules)
    formatoutput(results, args.output)

if __name__ == '__main__':
    main()
