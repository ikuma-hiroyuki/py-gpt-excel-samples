def create_workbook(title: str, wb: openpyxl.Workbook, is_new: bool):
    """
    シートを作成してシート名に使えない文字を除去したうえでシート名を変更して返す
    :param title: シート名(プロンプトの要約)
    :param wb: 対象になるワークブックオブジェクト
    :param is_new: ワークブックが新規作成されたかどうかのフラグ
    :return: ワークシートオブジェクト
    """

    # シート名に使えない文字を除去
    trimmed_title = trim_invalid_chars(title)

    if is_new:
        # アクティブシート(Sheet)を取得
        ws = wb.active
        ws.title = trimmed_title
    else:
        # シートを追加
        ws = wb.create_sheet(title=trimmed_title)
        wb.move_sheet(ws, offset=-len(wb.worksheets) + 1)
        wb.active = ws

    return ws
