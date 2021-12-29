# input('What is your name?')
# from getpass import getpass
# getpass('What is your pass?')

# import sys

# print(sys.argv)
# print(len(sys.argv))

# if len(sys.argv) == 2:
#     print(f'Knock, knock, {sys.argv[1]}')
# else:
#     sys.stderr.write(f'Usage: {sys.argv[0]} <name>\n')
#     sys.exit(1)
# # echo $?

from argparse import ArgumentParser

ap = ArgumentParser(description='Greet user')
ap.add_argument('name', nargs='?')

args = ap.parse_args()
print(args.name)
