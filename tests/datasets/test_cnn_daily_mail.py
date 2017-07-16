import pytest
import os
import neural_summarization.constants as constants


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='CHECKING THE NUMBER OF CNN URLS IS A DEV TEST ONLY')
def test_number_cnn_urls():
    NUMBER_CNN_URLS = 92579
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    assert DATA_FOLDER is not None
    URLS_FOLDER = os.path.join(DATA_FOLDER, 'cnn_dailymail', 'urls')
    cnn_train_urls_filename = os.path.join(URLS_FOLDER, 'cnn_wayback_training_urls.txt')
    cnn_test_urls_filename = os.path.join(URLS_FOLDER, 'cnn_wayback_test_urls.txt')
    cnn_validation_urls_filename = os.path.join(URLS_FOLDER, 'cnn_wayback_validation_urls.txt')
    with open(cnn_train_urls_filename) as fp:
        num_train_urls = len(fp.readlines())
    with open(cnn_test_urls_filename) as fp:
        num_test_urls = len(fp.readlines())
    with open(cnn_validation_urls_filename) as fp:
        num_validation_urls = len(fp.readlines())

    num_urls = num_train_urls + num_test_urls + num_validation_urls

    assert num_urls == NUMBER_CNN_URLS


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='CHECKING THE NUMBER OF DAILYMAIL URLS IS A DEV TEST ONLY')
def test_number_dailymail_urls():
    NUMBER_DAILYMAIL_URLS = 219506
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    assert DATA_FOLDER is not None
    URLS_FOLDER = os.path.join(DATA_FOLDER, 'cnn_dailymail', 'urls')
    dailymail_train_urls = os.path.join(URLS_FOLDER, 'dailymail_wayback_training_urls.txt')
    dailymail_test_urls = os.path.join(URLS_FOLDER, 'dailymail_wayback_test_urls.txt')
    dailymail_validation_urls = os.path.join(URLS_FOLDER, 'dailymail_wayback_validation_urls.txt')

    with open(dailymail_train_urls) as fp:
        num_train_urls = len(fp.readlines())

    with open(dailymail_test_urls) as fp:
        num_test_urls = len(fp.readlines())

    with open(dailymail_validation_urls) as fp:
        num_validation_urls = len(fp.readlines())

    num_urls = num_train_urls + num_test_urls + num_validation_urls

    assert num_urls == NUMBER_DAILYMAIL_URLS


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='CHECKING THE OVERALL LENGTH OF TRAINING URL LIST IS A DEV TEST')
def test_number_training_urls():
    CNN_NUMBER_TRAINING_URLS = 90266
    DAILYMAIL_TRAINING_URLS = 196961
    NUM_TRAINING_URLS = CNN_NUMBER_TRAINING_URLS + DAILYMAIL_TRAINING_URLS
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    assert DATA_FOLDER is not None
    URLS_FOLDER = os.path.join(DATA_FOLDER, 'cnn_dailymail', 'urls')
    cnn_train_urls_filename = os.path.join(URLS_FOLDER, 'cnn_wayback_training_urls.txt')
    dailymail_train_urls = os.path.join(URLS_FOLDER, 'dailymail_wayback_training_urls.txt')

    with open(cnn_train_urls_filename) as fp:
        num_cnn_training_urls = len(fp.readlines())

    with open(dailymail_train_urls) as fp:
        num_dailymail_training_urls = len(fp.readlines())

    num_training_urls = num_cnn_training_urls + num_dailymail_training_urls

    assert num_training_urls == NUM_TRAINING_URLS


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='CHECKING THE OVERALL LENGTH OF TESTING URLS IS A DEV TEST')
def test_number_test_urls():
    CNN_NUMBER_TEST_URLS = 1093
    DAILYMAIL_TEST_URLS = 10397
    NUM_TEST_URLS = CNN_NUMBER_TEST_URLS + DAILYMAIL_TEST_URLS
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    assert DATA_FOLDER is not None
    URLS_FOLDER = os.path.join(DATA_FOLDER, 'cnn_dailymail', 'urls')
    cnn_test_urls_filename = os.path.join(URLS_FOLDER, 'cnn_wayback_test_urls.txt')
    dailymail_test_urls = os.path.join(URLS_FOLDER, 'dailymail_wayback_test_urls.txt')

    with open(cnn_test_urls_filename) as fp:
        num_cnn_test_urls = len(fp.readlines())

    with open(dailymail_test_urls) as fp:
        num_dailymail_test_urls = len(fp.readlines())

    num_test_urls = num_cnn_test_urls + num_dailymail_test_urls

    assert num_test_urls == NUM_TEST_URLS


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='CHECKING THE OVERALL LENGTH OF VALIDATIONS URLS IS A DEV TEST')
def test_number_validation_urls():
    CNN_NUMBER_VALIDATION_URLS = 1220
    DAILYMAIL_VALIDATION_URLS = 12148
    NUM_VALIDATION_URLS = CNN_NUMBER_VALIDATION_URLS + DAILYMAIL_VALIDATION_URLS
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    assert DATA_FOLDER is not None
    URLS_FOLDER = os.path.join(DATA_FOLDER, 'cnn_dailymail', 'urls')
    cnn_validation_urls_filename = os.path.join(URLS_FOLDER, 'cnn_wayback_validation_urls.txt')
    dailymail_validation_urls = os.path.join(URLS_FOLDER, 'dailymail_wayback_validation_urls.txt')

    with open(cnn_validation_urls_filename) as fp:
        num_cnn_validation_urls = len(fp.readlines())

    with open(dailymail_validation_urls) as fp:
        num_dailymail_validation_urls = len(fp.readlines())

    num_test_urls = num_cnn_validation_urls + num_dailymail_validation_urls

    assert num_test_urls == NUM_VALIDATION_URLS


