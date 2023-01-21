import string
import random

from config import config

SHORTENED_STRING_LENGTH = config.SHORTENED_STRING_LENGTH


def generate_shortened_url(length: int = SHORTENED_STRING_LENGTH) -> str:
    """
    This function is used to generate random alias of a given length.
    Default length is taken from environment variables.
    :return: Return a randomly generated string of a given length. String will include alphanumeric symbols only.
    """
    letters = string.ascii_lowercase
    digits = string.digits
    chars = letters + digits
    result_str = ''.join(random.choice(chars) for i in range(length))
    return result_str
