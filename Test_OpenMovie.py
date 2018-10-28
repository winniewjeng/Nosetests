#!/usr/bin/env python3

import os
import shutil
import logging
import nose
import OpenMovie
import urllib.request
import traceback
import json
import sys
import re



class Test_OpenMovie:
    """
        Test OpenMovie.py to demonstrate nosetests
    """

    def __init__(self):
        self.capture = nose.plugins.capture.Capture()
        self.logcapture = nose.plugins.logcapture.LogCapture()
        self.logcapture.start()
        logging.basicConfig(filename="testlog.log",
                            level=logging.info,
                            format='%(asctime)s,%(levelname)s,%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        pass

    def setup(self):
        self.capture.begin()
        self.logcapture.begin()
        self.empty_movie = OpenMovie.OpenMovie()
        # self.avatar_movie = OpenMovie.OpenMovie(title="Avatar",
        #                                         posterURL="https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg")
        # assert that the name of the path is Posters
        assert self.empty_movie.path is "Posters"

        # if Posters directory already exists, delete it
        if os.path.isdir(self.empty_movie.path):
            shutil.rmtree(self.empty_movie.path)
        else:
            pass

    def teardown(self):
        self.capture.end()
        self.logcapture.end()
        del (self.empty_movie)
        # del (self.gladiator_movie)
        print("capture: %s" % (self.capture.buffer))
        print("logcapture: %s " % (self.logcapture.formatLogRecords()))

    def test_ctor(self):
        '''
        Test constructor method
        '''
        self.capture.begin()
        self.logcapture.begin()
        assert self.empty_movie.title is None
        assert self.empty_movie.posterURL is None
        assert self.empty_movie.posterFileName is None
        assert self.empty_movie.path is 'Posters'
        # if Posters directory already exists
        if os.path.isdir(self.empty_movie.path):
            # assert its existence
            assert os.path.isdir(self.empty_movie.path)
        # if Posters directory does not exists and is being made
        else:
            # assert its new existence
            os.mkdir(self.empty_movie.path)
            assert os.path.isdir(self.empty_movie.path)
            # assert the logging
            # assert logging.INFO
        print("\n")
        print(str(self.empty_movie))

        self.capture.finalize(result="None")

    def test_getPoster(self):
        '''
        Test getPoster method
        '''
        self.capture.begin()
        self.logcapture.begin()

        try:
            json.load(open('movies.json', 'r'))
        except:
            assert IOError, "Cannot open file!"

        self.gladiator_movie = OpenMovie.OpenMovie("Gladiator", "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg")
        self.gladiator_movie.getPoster()

        self.faulty_movie = OpenMovie.OpenMovie("Dummy", "https://images.jpg")
        self.faulty_movie.getPoster()
        # assert self.gladiator_movie.getPoster() is traceback.TracebackException
        # if self.gladiator_movie.getPoster() is True:
        #     assert urllib.request.urlretrieve(self.empty_movie.posterURL, self.empty_movie.posterFileName)
        # assert re.sub(r"[^a-zA-Z0-9]", "_", self.gladiator_movie.title)
        # assert self.gladiator_movie.title is "Gladiator"
        # assert self.gladiator_movie.posterURL is "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg"


        exc_type, exc_value, exc_traceback = sys.exc_info()
        # assert sys.exc_info is (None, None, None)
        # assert exc_type and exc_value and exc_traceback
        # assert traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
        # assert self.gladiator_movie.getPoster() is True
        # assert self.empty_movie.getPoster() is False
        # assert self.test_getPoster() is True
        # urllib.request.urlretrieve("https://images-na.ssl-images-amazon.com", self.gladiator_movie.posterFileName)
        #     pass
        #     assert self.test_getPoster() is False
        self.capture.finalize(result="None")
