from hw import count_vowels

def test_count_vowels():
    assert count_vowels('привет') == 2
    assert count_vowels('пртвнк') == 0
    assert count_vowels('здрАвствУй') == 2
    assert count_vowels('аеёиоуыэюя') == 10