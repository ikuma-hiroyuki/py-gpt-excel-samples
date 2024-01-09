def generate_summary(initial_prompt: str, summary_length: int = 10) -> str:
    """
    ユーザーの最初のプロンプトを要約する。
    :param initial_prompt:  ユーザーの最初のプロンプト
    :param summary_length:  要約する文字数の上限
    :return:  要約されたプロンプト
    """

    summary_request = {"role": "system",
                       "content": "あなたはユーザーの依頼を要約する役割を担います。"
                                  f"以下のユーザーの依頼を必ず{summary_length}文字以内で要約してください。"}

    # GPTによる要約を取得
    messages = [summary_request, {"role": "user", "content": initial_prompt}]
    response = client.chat.completions.create(model=DEFAULT_MODEL, messages=messages, max_tokens=summary_length)
    summary = response.choices[0].message.content

    adjustment_summary = summary[:summary_length]
    return adjustment_summary
