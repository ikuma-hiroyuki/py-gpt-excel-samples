import openpyxl


def load_or_create_workbook() -> tuple[openpyxl.Workbook, bool]:
    """
    ワークブックを読み込み、そのオブジェクトを返すとともに新規作成したかどうかを返す
    :returns: ワークブックのオブジェクト, 新規作成したかどうか
    """

    # ワークブックの読み込み
    if excel_path.exists():
        wb = openpyxl.load_workbook(excel_path)
        return wb, False
    else:
        wb = openpyxl.Workbook()
        return wb, True
