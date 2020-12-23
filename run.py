import argparse
import requests
from random import choice
from time import sleep

parser = argparse.ArgumentParser(
    description="Supply domain and addresses to be polled")
parser.add_argument('--domain', required=True,
                    help="Domain in the form http://<domain>:<port>/")
parser.add_argument('--arguments', required=True,
                    help="Arguments to be hit on the domain, comma separated")
parser.add_argument('--delay', type=int, required=False,
                    default=0, help="Milliseconds of delay between polls")


def poller(domain, targets, delay=0):
    counter = 0
    while True:
        try:
            url = f"{domain}{choice(targets)}"
            _ = requests.get(url)
            counter += 1
            print(f'[{counter}]: Accessed {url}')
        except Exception:
            pass
        sleep(delay/1000.0)


def main():
    args = parser.parse_args()
    poller(args.domain, args.arguments.split(','), args.delay)


if __name__ == "__main__":
    main()
