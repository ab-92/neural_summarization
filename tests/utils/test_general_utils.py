from neural_summarization.utils.general_utils import *


def test_form_hash_return_type():
    string_ = 'This is a test'
    hashed_string = form_hash(string_)
    assert type(hashed_string) == str
