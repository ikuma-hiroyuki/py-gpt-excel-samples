def give_role_to_system() -> str:
    """
    AIアシスタントに与える役割を入力させる
    :return: AIアシスタントに与える役割
    """

    # はじめの説明を表示
    print("\nAIアシスタントとチャットを始めます。チャットを終了させる場合は exit() と入力してください。\n")

    # AIアシスタントに与える役割を入力
    system_role = input("AIアシスタントに与える役割がある場合は入力してください。\n"
                        "ない場合はそのままEnterキーを押してください。: ")
    return system_role