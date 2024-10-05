import os
import sys


def get_chrome_user_data_dir():
    if sys.platform == "darwin":  # macOS
        return os.path.expanduser('~/Library/Application Support/Google/Chrome')
    elif sys.platform.startswith("linux"):  # Linux
        return os.path.expanduser('~/.config/google-chrome')
    elif sys.platform == "win32":  # Windows
        return os.path.expandvars('%LOCALAPPDATA%\\Google\\Chrome\\User Data')
    else:
        raise OSError("Unsupported operating system")
