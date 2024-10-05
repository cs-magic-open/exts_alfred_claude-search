from ..paths import PROJECT_DIR


def inject_stealth_script_into_driver(driver):
    with open(PROJECT_DIR / 'stealth.min.js') as f:
        js = f.read()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": js })
