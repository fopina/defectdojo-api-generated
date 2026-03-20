import unittest


def skip_if_fail(test_dependency, *args, **kwargs):
    try:
        return test_dependency(*args, **kwargs)
    except Exception as e:
        raise unittest.SkipTest(f'dependency failed ({str(e)})')
