#!/usr/bin/python
'''
Example custom dynamic inventory script for Ansible, in Python.
'''

#import os
import sys
import argparse

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
        with open('/tmp/argv_log','a') as f:
            f.write(json.dumps(sys.argv)+'\n')
        return {
            'white': {
                'hosts': ['10.200.200.3'],
                'vars':{}
          	        },
            'black': {
	        'hosts': ['10.200.200.2'],
	        'vars':{}
 	            },
            'network': {
	        'hosts': ['10.200.200.101'],
	        'vars':{}
			},
            '_meta': {
                'hostvars': {
                    '10.200.200.101': {
                        'ansible_connection': 'network_cli',
                        'ansible_network_os': 'ios',
                        'ansible_user':'ansible',
                        'ansible_password':'1234QWer'
                                     }
                            }
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
