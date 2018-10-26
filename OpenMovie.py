#!/usr/bin/env python3

import logging
import os
import re
import sys
import traceback
import urllib.request


class OpenMovie:
    """
    Simple OpenMovie class to demonstrate testing
    """

    # constructor:
    def __init__(self, title=None, posterURL=None):
        '''
        constructor
        '''
        self.title = title
        self.posterURL = posterURL
        self.posterFileName = None
        self.path = "Posters"
        if os.path.isdir(self.path):
            pass
        else:
            os.mkdir(self.path)
            logging.info(" Successfully created the directory %s " % self.path)

    def getPoster(self):
        # log the event of calling getPoster() method
        logging.info(" getPoster() method is called")
        logging.info(" Poster's name: %s" % self.title)
        logging.info(" Poster's URL %s" % self.posterURL)

        # substitute every symbol and spaces in title with underline
        self.title = re.sub(r"[^a-zA-Z0-9]", "_", self.title)
        self.title = "Posters/%s" % self.title

        # use urlretrieve to download the file from posterURL, store it in posterFileName, return True
        try:
            self.posterFileName = urllib.request.urlretrieve(self.posterURL, self.title)
            return True
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            # print("*** tb_lineno:", exc_traceback.tb_lineno)
            logging.error("*** tb_lineno:", exc_traceback.tb_lineno)
            return False
