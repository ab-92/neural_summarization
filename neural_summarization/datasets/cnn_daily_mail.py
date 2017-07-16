from neural_summarization.utils.general_utils import print_block


def read_story_file():
    pass


def process_url_list(urllist, type):
    """
    Args:
        urllist (list): the combined urllist for cnn and dailymail
        (str): One of 'train', 'test', 'validation'
    """
    print_block("PROCESSING CNN/DAILYMAIL %s URLLIST" % (type, ))
    for url in urllist:
        print url


if __name__ == '__main__':
    pass
