#!/usr/bin/python

# Base imports for all integrations, only remove these at your own risk!
import json
import sys
import os
import time
from collections import OrderedDict
import requests
from copy import deepcopy
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
from IPython.core.display import HTML
from IPython.display import display_html, display, Markdown, Javascript, FileLink, FileLinks, Image
import pandas as pd
# Widgets
from ipywidgets import GridspecLayout, widgets


from addon_core import Addon

@magics_class
class Helloworld(Addon):
    # Static Variables

    magic_name = "helloworld"
    name_str = "helloworld"
    custom_evars = []

    custom_allowed_set_opts = []


    myopts = {}
#    myopts['profile_max_rows_full'] = [10000, "Row threshold for doing full analysis. Over there and we default to minimal analysis with a warning"]


    def __init__(self, shell, debug=False,  *args, **kwargs):
        super(Helloworld, self).__init__(shell, debug=debug)
        self.debug = debug

        #Add local variables to opts dict
        for k in self.myopts.keys():
            self.opts[k] = self.myopts[k]
        self.load_env(self.custom_evars)
        shell.user_ns['helloworld_var'] = self.creation_name


    def listIntsAdsMD(self):
        myout = ""
        myout += "\n"
        myout += "Additional help for each integration and addon can be found by running the magic string for each integration or addon\n"
        myout += "\n"
        myout += "### Installed Integrations:\n"
        myout += "---------------\n"
        myout += "| %s | %s |\n" % ("Integration", "Integration Loaded")
        myout += "| ------ | ------ |\n"
        for integration in self.ipy.user_ns['jupyter_loaded_integrations']:
            m = "%" + integration
            myout += "| %s | %s |\n" % (m, str(True))
        myout += "\n"

        myout += "### Installed Addons:\n"
        myout += "---------------\n"
        myout += "| %s | %s |\n" % ("Addon", "Addon Loaded")
        myout += "| ------ | ------ |\n"
        for addon in self.ipy.user_ns['jupyter_loaded_addons']:
            m = "%" + addon
            myout += "| %s | %s |\n" % (m, str(True))
        myout += "\n"
        return myout

    def customHelp(self, curout):
        n = self.name_str
        m = "%" + self.name_str
        mq = "%" + m

        table_header = "| Magic | Description |\n"
        table_header += "| -------- | ----- |\n"

        out = curout
        out += "\n"
        out += self.listIntsAdsMD()

        return out

    def retCustomDesc(self):
        out = "This is the starting point for all addons and integrations in the Jupyter Integrations package"
        return out

    # This is the magic name.
    @line_cell_magic
    def helloworld(self, line, cell=None):
        if self.debug:
           print("line: %s" % line)
           print("cell: %s" % cell)
        #line = line.replace("\r", "")
        if cell is None:
            line_handled = self.handleLine(line)
            if not line_handled: # We based on this we can do custom things for integrations.
                print("I am sorry, I don't know what you want to do with your line magic, try just %" + self.name_str + " for help options")
        else: # This is run is the cell is not none, thus it's a cell to process  - For us, that means a query
            print("No Cell Magic for %s" % self.name_str)
