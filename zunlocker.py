#!/usr/bin/python3

import zipfile; import sys; import argparse; import os; import time;

#Colours
redColour = "\033[31m"
greenColour = "\033[32m"
yellowColour = "\033[33m"
blueColour = "\033[34m"
resetColour = "\033[0m"

parser = argparse.ArgumentParser()
parser.add_argument("-zf", "--zipfile", required=True)
parser.add_argument("-w", "--wordlist", required=True)
parser.add_argument("-oN", "--oN")
args = parser.parse_args()

zfile = zipfile.ZipFile(args.zipfile)
wordlist = args.wordlist
zlocation = args.oN

def main():
    with open(wordlist, "r") as wfile:
        for word in wfile:
            word = word.strip()
            try:
                zfile.extractall(pwd=word.encode())
            except:
                time.sleep(0.01)
                os.system("clear")
                print(f"Testing passwords: {redColour}{word}{resetColour}")
                pass
            else:
                os.system("clear")
                print(f"PASSWORD FOUND! {greenColour}{word}{resetColour}")
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
