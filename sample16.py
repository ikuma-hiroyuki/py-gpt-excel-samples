def open_workbook():
    """エクセルを開く"""
    if os.name == "nt":
        # windows
        os.system(f"start {excel_path}")
    elif os.name == "posix":
        # mac
        os.system(f"open {excel_path}")
