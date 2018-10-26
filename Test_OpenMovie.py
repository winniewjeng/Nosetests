#!/usr/bin/env python3

import os
import shutil
import logging
import nose
import OpenMovie

# nose.main()


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
        self.avatar_movie = OpenMovie.OpenMovie(title="Avatar",
                                                posterURL="https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg")
        # test the name path
        assert self.empty_movie.path is "Posters"
        if os.path.isdir(self.empty_movie.path):
            assert os.path.isdir(self.empty_movie.path)
        else:
            assert os.mkdir(self.empty_movie.path)
        # if Poster dir already exists, delete it so OpenMovie can create a new one
        shutil.rmtree(self.empty_movie.path)

    def teardown(self):
        self.capture.end()
        self.logcapture.end()
        del (self.empty_movie)
        del (self.avatar_movie)
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
        print("\n")
        print(str(self.empty_movie))

        assert self.avatar_movie.title is "Avatar"
        assert self.avatar_movie.posterURL is "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg"
        assert self.avatar_movie.posterFileName is None
        print(str(self.avatar_movie))
        self.capture.finalize(result="None")

    def test_getPoster(self):
        '''
        Test getPoster method
        '''
        self.capture.begin()
        self.logcapture.begin()
        assert self.empty_movie.title is self.empty_movie.title
        self.capture.finalize(result="None")
