import neural_summarization.constants as constants
import os
import pytest


def test_root_not_empty():
    ROOT = constants.ROOT
    ROOT = ROOT.strip()
    assert bool(ROOT) is True


def test_dirpaths_dict():
    DIRPATHS = constants.DIRPATHS
    assert type(DIRPATHS) == dict


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='THIS IS A DEV TEST ONLY')
def test_data_folder_exist():
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    assert DATA_FOLDER is not None
    assert os.path.isdir(DATA_FOLDER) is True


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='THIS IS A DEV TEST ONLY')
def test_cnndailymail_folder_exists():
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    os.path.isdir(os.path.join(DATA_FOLDER, 'cnn_dailymail')) is True


@pytest.mark.skipif(os.environ['DEV'] != 'TRUE',
                    reason='THIS IS A DEV TEST ONLY')
def test_url_files_exist():
    DIRPATHS = constants.DIRPATHS
    DATA_FOLDER = DIRPATHS.get('DATA', None)
    URLS_FOLDER = os.path.join(DATA_FOLDER, 'cnn_dailymail', 'urls')
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'cnn_wayback_training_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'cnn_wayback_validation_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'cnn_wayback_test_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'dailymail_wayback_training_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'dailymail_wayback_validation_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'dailymail_wayback_test_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'training_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'validation_urls.txt')) is True
    assert os.path.isfile(os.path.join(URLS_FOLDER, 'test_urls.txt')) is True


