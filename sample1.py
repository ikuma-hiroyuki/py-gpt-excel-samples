import random


def gacha(num):
    """
    num で指定された回数分ガチャを引き、結果をリストと文字列で返す

    :param num: ガチャを引く回数
    :returns: gacha_result_list, result ガチャの結果をリストと文字列で返す
    """

    gacha_list = []

    for i in range(num):
        # 1~100の中からランダムに数字を選ぶ
        rand_num = random.randint(1, 100)

        # 1~60の時は星1
        if rand_num <= 60:
            gacha_list.append("★")
        # 61~90の時は星2
        elif rand_num <= 90:
            gacha_list.append("★" * 2)
        # 91~99の時は星3
        elif rand_num <= 99:
            gacha_list.append("★" * 3)
        # 100の時は星4
        else:
            gacha_list.append("★" * 4)

    # ガチャの結果を文字列にする
    result = "と".join(gacha_list)

    return gacha_list, result


gacha_result_list, result_string = gacha(10)
print(gacha_result_list)
print(result_string)
