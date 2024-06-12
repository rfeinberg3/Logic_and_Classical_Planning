#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))

