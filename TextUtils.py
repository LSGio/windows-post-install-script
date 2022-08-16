
def to_camel_case(text: str) -> str:
    split_text = [word.title() for word in text.split('_')]
    return ''.join([split_text[0].lower()] + split_text[1:])
