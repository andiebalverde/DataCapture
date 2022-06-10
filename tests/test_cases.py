from stats.data_capture import DataCapture

def test_greater_small_set():
    capture = DataCapture()
    capture.add(3)
    capture.add(980)
    capture.add(3)
    capture.add(4)
    capture.add(771)
    stats = capture.build_stats()
    assert stats.greater(4) == 2


def test_greater_big_set():
    capture = DataCapture()
    capture.add(3)
    capture.add(100)
    capture.add(3)
    capture.add(4)
    capture.add(12)
    capture.add(1000)
    capture.add(999)
    capture.add(872)
    capture.add(42)
    stats = capture.build_stats()
    assert stats.greater(4) == 6


def test_less_small_set():
    capture = DataCapture()
    capture.add(1)
    capture.add(100)
    capture.add(3)
    capture.add(4)
    capture.add(90)
    stats = capture.build_stats()
    assert stats.less(4) == 2


def test_less_big_set():
    capture = DataCapture()
    capture.add(3)
    capture.add(122)
    capture.add(3)
    capture.add(4)
    capture.add(87)
    capture.add(1)
    capture.add(1)
    capture.add(1)
    capture.add(0)
    stats = capture.build_stats()
    assert stats.less(4) == 6


def test_between_small_set():
    capture = DataCapture()
    capture.add(3)
    capture.add(12)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.between(3, 6) == 4


def test_between_big_set():
    capture = DataCapture()
    capture.add(3)
    capture.add(4)
    capture.add(2)
    capture.add(4)
    capture.add(3)
    capture.add(1)
    capture.add(1)
    capture.add(1)
    capture.add(0)
    stats = capture.build_stats()
    assert stats.between(0, 1) == 4
