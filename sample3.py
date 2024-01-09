def fetch_gpt_model_list() -> list[str]:
    """
    GPTモデルの一覧を取得
    :return: GPTモデルの一覧
    """

    # モデルの一覧の取得
    all_model_list = client.models.list()

    # GPTモデルのみ抽出する
    gpt_model_list = []
    for model in all_model_list:
        if "gpt" in model.id:
            gpt_model_list.append(model.id)

    # モデル名でソート
    gpt_model_list.sort()

    return gpt_model_list
