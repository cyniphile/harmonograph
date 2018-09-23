import main as h


def test_rotate_vector():
    start = [1, 0]
    finish = h.rotate_vector(start, 90)
    assert(round(finish[0], 3) == 0)
    assert(round(finish[1], 3) == 1)


if __name__ == "__main__":
    test_rotate_vector()

