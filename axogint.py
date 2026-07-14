import argparse
import json
import sys
from core import runchecks
from utils import formatoutput

def main():
    parser = argparse.ArgumentParser(description='axogint - email osint tool')
    parser.add_argument('email', help='target email address')
    parser.add_argument('--threads', type=int, default=20, help='number of threads')
    parser.add_argument('--timeout', type=int, default=10, help='request timeout')
    parser.add_argument('--output', choices=['json','table'], default='table', help='output format')
    parser.add_argument('--modules', nargs='+', help='limit to specific modules')
    parser.add_argument('--proxy', help='proxy url e.g. socks5://127.0.0.1:9050')
    parser.add_argument('--tor', action='store_true', help='use tor default proxy (127.0.0.1:9050)')
    parser.add_argument('--dns', action='store_true', help='perform dns/mx check before modules')
    parser.add_argument('--rate-limit', type=float, default=0, help='global delay between requests (seconds)')
    parser.add_argument('--color', action='store_true', help='enable colored output')
    parser.add_argument('--verbose', action='store_true', help='show detailed error messages')
    args = parser.parse_args()

    results = runchecks(args.email, args.threads, args.timeout, args.modules,
                        args.proxy, args.tor, args.dns, args.rate_limit, args.verbose)
    formatoutput(results, args.output, args.color)

if __name__ == '__main__':
    main()
