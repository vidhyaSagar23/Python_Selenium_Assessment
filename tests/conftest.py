import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()


# Extends the pytest plugin to take and embed screenshot in html report, whenever test fails.

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
