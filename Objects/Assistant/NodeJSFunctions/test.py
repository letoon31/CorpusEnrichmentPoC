# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:46:50 2018

@author: ElieAZERAF
"""

from Naked.toolshed.shell import muterun_js
import sys

response = muterun_js('call_list_workspace.js ' + "eee" + ' ' + "eee")

if response.exitcode == 0:
  print(response.stdout)
else:
  sys.stderr.write(str(response.stderr))