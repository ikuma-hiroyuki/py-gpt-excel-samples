import os

from dotenv import load_dotenv
from openai import OpenAI


def chat_runner():
    """チャットを開始"""

    # チャットのログを保存するリスト
    chat_log: list[dict] = []

    # はじめの説明を表示
    print("AIアシスタントとチャットを始めます。チャットを終了させる場合は exit() と入力してください。\n")

    # AIアシスタントに与える役割を入力
    system_role = input("AIアシスタントに与える役割がある場合は入力してください。\n"
                        "ない場合はそのままEnterキーを押してください。: ")

    # 役割がある場合はチャットログに追加
    if system_role:
        chat_log.append({"role": "system", "content": system_role})

    while True:
        prompt = input("\nあなた: ")
        if prompt == "exit()":
            break

        # チャットログにユーザーの入力を追加
        chat_log.append({"role": "user", "content": prompt})

        # AIの応答を取得
        # todo モデルを選択できる関数を実装
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=chat_log,
                                                  stream=True)

        # ストリーミングでAIの応答を取得
        role, content = stream_and_concatenate_response(response)

        # チャットログにAIの応答を追加
        chat_log.append({"role": role, "content": content})


def stream_and_concatenate_response(response) -> tuple[str, str]:
    """
    AIの応答をストリーミングで取得したものをチャンクで表示し、結合して返す
    :param response: OpenAI.chat.completions.create()の戻り値
    :return: AIの応答の文字列、AIの応答の役割
    """

    print("\nAIアシスタント: ", end="")
    content_list: list[str] = []
    role = ""
    for chunk in response:
        chunk_delta = chunk.choices[0].delta
        content_chunk = chunk_delta.content if chunk_delta.content is not None else ""
        role_chunk = chunk_delta.role
        if role_chunk:
            role = role_chunk
        content_list.append(content_chunk)
        print(content_chunk, end="")
    else:
        print()
        content = "".join(content_list)

    return role, content


load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))

chat_runner()
