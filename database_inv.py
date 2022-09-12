#!/usr/bin/python

#import os
#import sys
import argparse
import mysql.connector


try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory);

    # Example inventory for testing.
    def example_inventory(self):
        
        config = {
        'user': 'autoscript',
        'password': 'autopassword',
        'host': '10.200.200.3',
        'database': 'inventory',
        'raise_on_warnings': True
         }

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(buffered=True)
        query = ('SELECT Hostname, IP_Address FROM hosts')
        cursor.execute(query)
        resp=[(str(elem[0]),str(elem[1])) for elem in cursor.fetchall()]
        cursor.close()
        cnx.close()

        return {
            resp[0][0]: {
                'hosts': [resp[0][1]],
                'vars':{}
          	        },
            resp[1][0]: {
	        'hosts': [resp[1][1]],
	        'vars':{}
 	            }
                }
    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
