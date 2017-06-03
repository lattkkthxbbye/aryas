import json
import sqlite3
import sys
from collections import defaultdict


def main(argv):
    """
    Will create a love table, and a json file
    :param argv:    the args
        -> None: will use stdin
        -> discord_token: the discord token that will be put in the json file
    """
    arg_dict = build_arg_list(argv)

    if 'discord_token' in arg_dict:
        # args
        cred = arg_dict['discord_token'][0]
    else:
        # stdin
        cred = input('Type the cred: ')

    create_love_table()
    create_secret_json(cred)


def build_arg_list(argv):
    """
    Takes a list of system arguments and transforms them into a dictionary.
    :param argv: ie. sys.argv[1:]
    :return d:  The argument dictionary
    """
    d = defaultdict(list)
    for k, v in ((k.lstrip('-'), v) for k, v in (a.split('=') for a in argv)):
        d[k].append(v)

    return dict(d)


def create_secret_json(token):
    """
        Create secrets.json file.
        :param token: the token of the bot to add in the json
    """
    json_data = json.dumps({
        'discord': {
            'token': token
        }
    }, sort_keys=True, indent=2, separators=(',', ': '))

    # Write json_data to the secrets.json file.
    with open('secrets.json', 'w') as outfile:
        outfile.write(json_data)


def create_love_table():
    """
    Creates a love table on a SQLite DB
    """
    # Create a SQLite DB and connect to it.
    conn = sqlite3.connect('aryas.db')
    c = conn.cursor()
    # Create love table
    c.execute("""CREATE TABLE IF NOT EXISTS love
                  (giver CHAR(18), receiver CHAR(18), channel CHAR(18), server CHAR(18), amount INTEGER)""")


if __name__ == '__main__':
    main(sys.argv[1:])
