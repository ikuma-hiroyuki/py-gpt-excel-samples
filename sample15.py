def write_chat_log(ws, chat_log: list[dict]):
    """
    チャットの履歴を書き込み書式設定する
    :param ws: 出力対象のワークシート
    :param chat_log: チャットの履歴
    """

    row_height_adjustment_standard = 17
    font_style = Font(name="メイリオ", size=10)
    assistant_color = PatternFill(fill_type="solid", fgColor="d9d9d9")

    # チャット内容の書き込み
    for row_number, content in enumerate(chat_log, 3):
        cell_role, cell_content = ws[f"A{row_number}"], ws[f"B{row_number}"]

        # ロールと発言内容を書き込み
        cell_role.value = content["role"]
        cell_content.value = content["content"]

        # セル内改行の調整
        cell_content.alignment = Alignment(wrapText=True)

        # 行の高さを調整
        adjusted_row_height = len(content["content"].split("\n")) * row_height_adjustment_standard
        ws.row_dimensions[row_number].height = adjusted_row_height

        # 書式設定
        cell_role.font = font_style
        cell_content.font = font_style
        if content["role"] == "assistant":
            cell_role.fill = assistant_color
            cell_content.fill = assistant_color
