from src.pre_built.counter import count_ocurrences


def test_counter():
    expected_count_word_python = 1639
    expected_count_word_javascript = 122
    count_word_python = count_ocurrences('data/jobs.csv', 'Python')
    count_word_javascript = count_ocurrences('data/jobs.csv', 'JavaScript')
    assert count_word_python == expected_count_word_python
    assert count_word_javascript == expected_count_word_javascript
