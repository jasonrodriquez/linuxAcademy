#!/usr/bin/env python3.7

users = [{'admin': True, 'active': True, 'name': 'John'},
         {'admin': True, 'active': True, 'name': 'Jane'},
         {'admin': False, 'active': True, 'name': 'Frank'},
         {'admin': True, 'active': False, 'name': 'Jennifer'}
]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "
    print(prefix + user['name'])
    line += 1
