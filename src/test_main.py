from .main import get_text_length


def test_get_text_length():
    res = get_text_length("Hello React")
    assert res == 11
