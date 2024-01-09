def choice_model(gpt_model_list: list[str]) -> str:
    """
    チャットで使うモデルを選択させる
    :param gpt_model_list: GPTモデルの一覧
    :return: 選択したモデル名
    """

    default_model = "gpt-3.5-turbo"

    # モデルの一覧を表示
    print("AIとのチャットに使うモデルの番号を入力し Enter キーを押してください。")
    for num, model in enumerate(gpt_model_list):
        print(f"{num}: {model}")

    while True:
        input_number = input(f"何も入力しない場合は {default_model} を使います。: ")

        # 何も入力されなかった場合
        if not input_number:
            return default_model

        # 数字じゃなかった場合
        if not input_number.isdigit():
            print("数字を入力してください。")

        # モデル一覧の範囲外の数字だった場合
        elif not int(input_number) in range(len(gpt_model_list)):
            print("その番号は選択肢に存在しません。")

        # 正常な入力だった場合
        else:
            return gpt_model_list[int(input_number)]
