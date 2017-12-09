from selenium import webdriver


def before_scenario(context, feature):
    if not hasattr(context, 'driver'):
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        context.driver = webdriver.Chrome(chrome_options=chrome_options)

    context.driver.maximize_window()
    context.driver.get('https://www.facebook.com')


def after_scenario(context, feature):
    if hasattr(context, 'driver'):
        context.driver.quit()
