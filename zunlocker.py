#!/usr/bin/python3

import zipfile; import sys; import argparse; import os; import time;
from pwn import *

parser = argparse.ArgumentParser()
parser.add_argument("-zf", "--zipfile", required=True)
parser.add_argument("-w", "--wordlist", required=True)
parser.add_argument("-oN", "--oN")
args = parser.parse_args()

zfile = zipfile.ZipFile(args.zipfile)
wordlist = args.wordlist
zlocation = args.oN

p1 = log.progress("Decrypting zip")
p2 = log.progress("Password")

def main():
    with open(wordlist, "r") as wfile:
        for word in wfile:
            word = word.strip()
            try:
                zfile.extractall(pwd=word.encode())
            except:
                p2.status(word)
                pass
            else:
                p1.success("Completed")
                p2.success(word)
                if bool(zlocation):
                    with open(zlocation, "w") as zpassword:
                        zpassword.write(f"{word}")
                else:
                    pass
                sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
