import pytest
import thoudecimal

testcases = [
    ('天', 1),
    ('地', 2),
    ('宇宙', 5006),
    ('天地人', 1002079),
    ('二千五百', 415503151613)
]

@pytest.mark.parametrize('input, expect', testcases)
def test_1000decimaldecode(input, expect):
    assert thoudecimal.to_decimal(input) == expect
