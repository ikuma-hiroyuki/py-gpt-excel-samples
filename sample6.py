import os

from dotenv import load_dotenv
from openai import OpenAI


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


def chat_runner(gpt_model: str):
    """チャットを開始"""

    # チャットのログを保存するリスト
    chat_log: list[dict] = []

    # 役割がある場合はチャットログに追加
    system_role = give_role_to_system()
    if system_role:
        chat_log.append({"role": "system", "content": system_role})

    while True:
        prompt = input("\nあなた: ")
        if prompt == "exit()":
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


load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))

# チャットを開始
gpt_models = fetch_gpt_model_list()
choice = choice_model(gpt_models)
chat_runner(choice)
