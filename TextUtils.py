

def to_camel_case(text: str) -> str:
    """
    Convert an underscore separated string to camelCase.

    :param text: The string to convert
    :rtype: str
    :return: The converted string in camelCase
    """
    split_text = [word.title() for word in text.split('_')]
    return ''.join([split_text[0].lower()] + split_text[1:])
