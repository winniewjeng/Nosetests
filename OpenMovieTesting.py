#!/usr/bin/env python3

import logging
import nose  # changed from from nose import * to import nose


class OpenMovieTesting:
    def __init__(self, title=None, posterURL=None):
        self.title = title
        self.posterURL = posterURL
        self.posterFileName = None
        # log.WARNING("im here!")


    # def get_poster(self):
    #     # logging.INFO("im in get poster!")



class Test_OpenMovieTesting:
    def __init__(self):
        self.capture = nose.plugins.capture.Capture()
        self.logcapture = nose.plugins.logcapture.LogCapture()
        self.logcapture.start()
        logging.basicConfig(filename="testlog.log",
                            level=logging.INFO,
                            format='%(asctime)s,%(levelname)s,%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        pass

    def setup(self):
        self.logcapture.begin()
        self.empty_movie = OpenMovieTesting()

    def teardown(self):
        self.logcapture.end()
        del(self.empty_movie)
        print("capture: %s" % (self.capture.buffer))
        print("logcapture: %s " % (self.logcapture.formatLogRecords()))

    def test_ctor(self):
        self.logcapture.begin()
        assert self.empty_movie.title is None
        assert self.empty_movie.posterURL is None
        assert self.empty_movie.posterFileName is None

    # def test_getPoster(self):
    #     self.logcapture.begin()


