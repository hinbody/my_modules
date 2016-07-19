#! /usr/bin/env python3
#this is for me to remember how to get the current date/time as a string

import datetime

def get_time():
  """Returns current time in iso format
  """
  t = datetime.datetime.now().isoformat()
  return t
