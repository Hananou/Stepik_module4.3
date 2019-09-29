
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Укажите язык отображения страницы в формате --language=..")

@pytest.fixture(scope="function")
def browser(request):
    lg = request.config.getoption("language")
    if lg:
        print('\nstart chrome browser for test..')
        print('\nВы выбрали язык: '+lg)
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lg})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("Укажите язык отображения страницы в формате --language=..")
    yield browser
    print("\nquit browser..")
    browser.quit()