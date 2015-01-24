# scale_proxy_server

This Python script provides a JSON-RPC interface to a USB mail scale. It uses SSL and Basic HTTP authentication. It is designed for use with [scale_proxy](https://github.com/ryepdx/scale_proxy).

## Usage:

    $ python app.py

## Spoofing weight:

    $ python app.py --weight "1.94 kg"

## Adding users

    $ python
    
    >>> from app import add_user
    >>> add_user("user", "password")
    >>> exit()

## Removing users

    $ python
    
    >>> from app import delete_user
    >>> delete_user("user")
    >>> exit()

## Accessing the user database directly

    $ sqlite3 users.db
    
    sqlite> select * from users;

    user|494c884325be4798032547ee6525d03d8bf96977d623a2ebafa0095bf5b194dd|4f1a6f06-c8fd-4526-a375-986fa298c36b

    sqlite> .q


