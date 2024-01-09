def is_output_open_excel() -> bool:
    """
    Excelファイルが開かれているかどうかを判定する
    :return: 開かれているかの真偽値
    """

    # Windows
    if os.name == "nt":
        # Windows
        try:
            with excel_path.open("r+b"):
                return False
        except PermissionError:
            return True
        except FileNotFoundError:
            return False

    # Mac
    if os.name == "posix":
        if excel_path.exists():
            result = subprocess.run(["lsof", excel_path], stdout=subprocess.PIPE)
            return bool(result.stdout)
        return False
