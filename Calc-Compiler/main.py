import webview

class CompilerAPI:
    """
    docstring
    """
    pass

def main():
    webview.create_window("Owen's Calc Compiler", "index.html", js_api=CompilerAPI, width=800, height=600)
    webview.start()

if __name__ == "__main__":
    main()