import pytest

import v1
import v2


@pytest.mark.parametrize("version, a, b, excepted_result", [
    (v1, "a", "aa", ""),
    (v1, "ABDDCDGDWEGNABDC", "ABC", "ABDC"),
    (v1, "ABDDDCDGDWEGNABDCCCCC", "ABC", "ABDC"),
    (v2, "a", "aa", ""),
    (v2, "ABDDCDGDWEGNABDC", "ABC", "ABDC"),
    (v2, "ABDDDCDGDWEGNABDCCCCC", "ABC", "ABDC"),
    (v2, "qwer", "qwer", "qwer"),
])
def test_minimum_window_substring(version, a, b, excepted_result):
    sol = version.Solution()
    assert sol.minWindow(a, b) == excepted_result
