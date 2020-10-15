# -- FILE: features/environment.py
import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pycon_ar import create_app

# Use the chrome driver specific to your version of Chrome browser and put
# it in ./driver directory
CHROME_DRIVER = '/usr/local/bin/chromedriver'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")


def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(create_app())
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(options=chrome_options,
                                       executable_path=CHROME_DRIVER)
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()
