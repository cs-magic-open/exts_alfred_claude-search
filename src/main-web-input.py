import os
import sys
import time
import webbrowser

import pyautogui
import pyperclip
from pynput.keyboard import Key, Controller

from paths import ASSETS_DIR

import darkdetect

type Approach = "dull" | "dynamic"

keyboard = Controller()


def log(s):
    # os.system(f"""
    # osascript -e 'display notification "{s}" with title "Claude Search Alfred Workflow"'
    # """)
    with open("log.txt", "a") as f:
        f.write(s + "\n")
        f.flush()


def do_paste(query):
    """
    # pyautogui自带的 write、press，pyperclip 的 paste 都没用，还得是 pynput，调了好几个小时。。
    # see: https://www.reddit.com/r/learnpython/comments/vkrhm2/comment/idr20s6/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

    # pyperclip.paste() # 无效

    # pyautogui.hotkey('Ctrl', 'V') # 无效

    :param query:
    :return:
    """
    keyboard.press(Key.cmd)
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release(Key.cmd)


def claude_search(query, is_direct=False, approach: Approach = "dynamic", max_wait_seconds=10):
    log(f'-- inputting: {query}')

    # 使用系统默认浏览器打开 Claude
    # 需要加 schema，否则没有反应
    start_url = "https://claude.ai"
    if is_direct:
        start_url += "/new"
    webbrowser.open(start_url)

    box = pyautogui.locateOnScreen((ASSETS_DIR / f"claude-input-area-{darkdetect.theme().lower()}.png").as_posix(), max_wait_seconds, grayscale=True, confidence=.7)

    if is_direct:
        x, y = pyautogui.center(box)
        pyautogui.click(x, y)
        # time.sleep(.5)

    # 使用 CV 大法绕过输入法，否则可能有中英文问题，see: https://claude.ai/chat/e3ed5bab-d651-4f13-b061-0ca98837ba93
    pyperclip.copy(query)

    do_paste(query)
    log("pasted")

    pyautogui.press('enter')
    log("finished")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        claude_search(query)
    else:
        print("Please provide a search query.")
