def input_user_prompt() -> str:
    """
    ユーザーからの入力を受け付ける
    :return: ユーザーのプロンプト
    """

    user_prompt = ""
    while not user_prompt:
        user_prompt = input("\nあなた: ")
        if not user_prompt:
            print("プロンプトを入力してください。")

    return user_prompt


def generate_chat_log(gpt_model: str) -> list[dict]:
    """チャットを開始"""

    # チャットのログを保存するリスト
    chat_log: list[dict] = []

    # 役割がある場合はチャットログに追加
    system_role = give_role_to_system()
    if system_role:
        chat_log.append({"role": "system", "content": system_role})

    while True:
        prompt = input_user_prompt()
        if prompt == EXIT_COMMAND:
            break

        # チャットログにユーザーの入力を追加
        chat_log.append({"role": "user", "content": prompt})

        # AIの応答を取得
        response = client.chat.completions.create(model=gpt_model,
                                                  messages=chat_log,
                                                  stream=True)

        # ストリーミングでAIの応答を取得
        role, content = stream_and_concatenate_response(response)

        # チャットログにAIの応答を追加
        chat_log.append({"role": role, "content": content})

    return chat_log
