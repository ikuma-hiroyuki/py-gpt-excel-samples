def chat_runner() -> tuple[list[dict], str]:
    """
    チャットを開始し、チャットログとユーザーの最初のプロンプトを要約して返す。
    :returns: チャットログ, ユーザーの最初のプロンプトの要約
    """

    # チャットを開始
    # GPTモデルの一覧を取得
    gpt_list = fetch_gpt_model_list()
    # チャットで使うモデルを選択
    choice = choice_model(gpt_list)
    # チャットログを取得
    generated_log = generate_chat_log(choice)
    # ユーザーの最初のプロンプトを取得
    initial_user_prompt = get_initial_prompt(generated_log)

    initial_prompt_summary = ""
    if initial_user_prompt:
        # ユーザーの最初のプロンプトを要約
        initial_prompt_summary = generate_summary(initial_user_prompt)

    return generated_log, initial_prompt_summary
