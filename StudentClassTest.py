#!/usr/bin/env python3

import logging
import nose  # changed from from nose import * to import nose


class Student:

    """
    Simple Student class to demonstrate testing
    """

    def __init__(self, name=None, course=None):
        '''
        constructor
        '''
        self.name = name
        self.course = course
        self.list_of_grades = []
        self.gradeValue = 0
        logging.info("Student: %s\t%s" % (self.name, self.course))
        return

    def addGrade(self, grade=None):
        '''
        Add a grade value to the list of grades
        '''
        if grade is not None:
            self.list_of_grades.append(grade)
        return

    def calculateGrade(self):
        '''
        calculate the student letter grade based on
        the sum of the list_of_grades divided by the length
        of list_of_grades
        '''
        if len(self.list_of_grades):
            sum = 0
            for x in self.list_of_grades:
                sum = sum + x
            self.gradeValue = sum / len(self.list_of_grades)
        else:
            self.gradeValue = 0
        return

    def __str__(self):
        '''
        Nice printing of this class
        '''
        str = "{0}\t{1}\t{2}".format(self.name, self.course, self.gradeValue)
        return str


class Test_Student:

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
        self.empty_student = Student()
        self.phil_student = Student(name="Phil", course="Python")

    def teardown(self):
        self.logcapture.end()
        del(self.empty_student)
        del(self.phil_student)
        print("capture: %s" % (self.capture.buffer))
        print("logcapture: %s " % (self.logcapture.formatLogRecords()))

    def test_ctor(self):
        '''
        Test constructor method
        '''
        self.capture.begin()
        assert self.empty_student.name == None
        assert self.empty_student.course == None
        assert self.empty_student.gradeValue == 0
        assert self.empty_student.list_of_grades == []
        print("\n")
        print(str(self.empty_student))

        assert self.phil_student.name == "Phil"
        assert self.phil_student.course == "Python"
        assert self.phil_student.gradeValue == 0
        assert self.phil_student.list_of_grades == []
        print(str(self.phil_student))
        self.capture.finalize(result="None")

    def test_calculateGrade(self):
        '''
        Test grade calculation method
        '''
        self.capture.begin()
        self.phil_student.calculateGrade()
        assert self.phil_student.gradeValue == 0

        self.phil_student.addGrade(90)
        self.phil_student.calculateGrade()
        assert self.phil_student.gradeValue == 90

        self.phil_student.addGrade(80)
        self.phil_student.addGrade(70)
        self.phil_student.addGrade(65)
        self.phil_student.addGrade(100)
        self.phil_student.calculateGrade()

        nose.tools.eq_(self.phil_student.gradeValue, 81, msg="ERROR!")
        print("\n")
        print(str(self.phil_student))

        #nose.tools.eq_(self.phil_student.gradeValue, 100, msg="ERROR!")

        self.capture.finalize(result="None")

    def test_addGrade(self):
        '''
        Test adding a grade in
        '''
        self.phil_student.addGrade(90)
        assert self.phil_student.gradeValue == 0
        assert len(self.phil_student.list_of_grades) == 1
        self.phil_student.addGrade(95)
        assert self.phil_student.gradeValue == 0
        assert len(self.phil_student.list_of_grades) == 2
        self.phil_student.addGrade()
        assert self.phil_student.gradeValue == 0
        assert len(self.phil_student.list_of_grades) == 2