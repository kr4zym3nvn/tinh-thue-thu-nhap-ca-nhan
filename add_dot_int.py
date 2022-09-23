def reformat_text(text):
    # add "." every 3 digits
    text = str(text)
    text = text[::-1]
    text = ".".join(text[i:i + 3] for i in range(0, len(text), 3))
    text = text[::-1]
    return text