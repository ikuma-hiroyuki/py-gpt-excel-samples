def fetch_gpt_model_list() -> list[str] | None:
    """
    GPTモデルの一覧を取得
    :return: GPTモデルの一覧
    """

    # モデルの一覧の取得
    try:
        all_model_list = client.models.list()
    except openai.InternalServerError:
        print("OpenAI側でエラーが発生しています。少し待ってから再度試してください。")
        print("サービス稼働状況は https://status.openai.com/ で確認できます。")
    except openai.AuthenticationError:
        print("APIキーが正しく設定されていません。")
    except openai.APITimeoutError:
        print("APIのタイムアウトが発生しました。しばらくしてから再度実行してください。")
    except openai.RateLimitError:
        print("APIのレート制限に達しました。")
    except openai.APIError:
        print("エラーが発生しました")
    else:
        # GPTモデルのみ抽出する
        gpt_model_list = []
        for model in all_model_list:
            if "gpt" in model.id:
                gpt_model_list.append(model.id)

        # モデル名でソート
        gpt_model_list.sort()

        return gpt_model_list
