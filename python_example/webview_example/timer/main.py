import webview

def main():
    webview.create_window("Timer", html="<h1>Hello Webview</h1>")

    webview.start()

if __name__ == "__main__":
    main()

