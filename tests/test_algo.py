from exp4 import exp4


def test_smoke():
    player = exp4()
    advice = [
        [1/3, 1/3, 1/3],
        [2/3, 1/3, 0],
    ]
    arm = player.send((None, advice))
    assert arm in range(3)

    advice = [
        [0, 0, 1],
        [0, 0, 1],
    ]
    arm = player.send((0.2, advice))
    assert arm == 2

    advice = [
        [1/3, 0, 1/3],
        [1, 0, 0],
    ]
    arm = player.send((0.1, advice))
    assert arm != 1
