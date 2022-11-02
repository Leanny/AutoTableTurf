import os
import unittest

from capture import FileLoader
from tableturf.manager import detection

path = os.path.join(os.path.realpath(__file__), '..', '..', '..', '..', 'temp')


@unittest.skipIf(not os.path.exists(path), 'images not existed')
class TestUI(unittest.TestCase):
    def test_deck_cursor(self):
        capture = FileLoader(path=os.path.join(path, 'deck'))
        for _ in range(10):
            detection.deck_cursor(capture.capture(), True)

    def test_hands_cursor(self):
        capture = FileLoader(path=os.path.join(path, 'stage2'))
        for _ in range(10):
            detection.hands_cursor(capture.capture(), True)

    def test_redraw_cursor(self):
        capture = FileLoader(path=os.path.join(path, 'redraw'))
        for _ in range(10):
            detection.redraw_cursor(capture.capture(), True)

    def test_special_on(self):
        capture = FileLoader(path=os.path.join(path, 'stage4'))
        for _ in range(20):
            detection.special_on(capture.capture(), True)