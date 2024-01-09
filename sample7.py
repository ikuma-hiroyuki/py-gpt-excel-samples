def get_initial_prompt(chat_log: list[dict]) -> str | None:
    """
    チャットの履歴からユーザーの最初のプロンプトを取得する。
    :param chat_log:チャットの履歴
    :return: ユーザーの最初のプロンプト
    """

    # ユーザーの最初のプロンプトを取得
    for log in chat_log:
        if log["role"] == "user":
            initial_prompt = log["content"]
            return initial_prompt
