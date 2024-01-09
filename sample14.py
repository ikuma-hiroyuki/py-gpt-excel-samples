def trim_invalid_chars(title: str) -> str:
    """
    シート名に使えない文字を除去する
    :param title: シート名
    :return: 除去後のシート名
    """

    invalid_chars = ["/", "\\", "?", "*", "[", "]"]
    for char in invalid_chars:
        title = title.replace(char, "")
    return title
