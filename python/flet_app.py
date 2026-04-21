import flet
import subprocess
import time


def app(page):
    page.title = 'Flet App'
    page.window.prevent_close = True
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.add(
        flet.Row([flet.Text('Hello, World!')],
                 alignment=flet.MainAxisAlignment.CENTER)
    )
    subprocess.Popen(['python', 'subprocess_test.py',
                      'child'], start_new_session=True)
    for i in range(3):
        print('parent:', i)
        time.sleep(1)


def main():
    flet.app(app, view=flet.AppView.FLET_APP_HIDDEN)


if __name__ == '__main__':
    main()
