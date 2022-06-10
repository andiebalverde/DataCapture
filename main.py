from stats.data_capture import DataCapture

if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.add(1)
    capture.add(1)
    capture.add(1)
    capture.add(0)
    stats = capture.build_stats()
    print(f"stats.less(4): {stats.less(4)}")
    print(f"stats.between(1, 4): {stats.between(1, 4)}")
    print(f"stats.greater(8): {stats.greater(8)}")