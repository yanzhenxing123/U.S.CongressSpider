"""
@Author: yanzx
@Date: 2022/5/18 23:03
@Description: main函数
"""
import sys
import requests
import os
import time
from lxml import etree
import undetected_chromedriver as uc

import utils

ROOT_PATH = utils.get_project_path()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    'authority': 'www.congress.gov',
    'cookie': 'PHPSESSID=a7fcba14bdd6a778d96a748929357be9; AMCVS_0D15148954E6C5100A4C98BC%40AdobeOrg=1; quickSearchFormExpanded=0; KWICViewExpanded-advanced-search-legislation=true; KWICViewCompact-advanced-search-legislation=false; KWICViewExpanded-search=true; KWICViewCompact-search=false; AMCV_0D15148954E6C5100A4C98BC%40AdobeOrg=-1124106680%7CMCIDTS%7C19131%7CMCMID%7C58532803776396922704760696810774771296%7CMCOPTOUT-1652894103s%7CNONE%7CvVersion%7C5.2.0',
    'sec-ch-ua-platform': "Windows",
    'sec-ch-ua-mobile': '?0'
}

root_url = "https://www.congress.gov/"


def req():
    driver_executable_path = ROOT_PATH + '\\exe_foder\\chromedriver.exe'
    # driver_executable_path = 'F:\\Files\\spiders\\U.S.CongressSpider\\exe_folder\\chromedriver.exe'
    browser = uc.Chrome(
        version_main=95,
        driver_executable_path=driver_executable_path,
        # browser_executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    browser.get(root_url)
    delay = 6
    time.sleep(delay)
    text = browser.page_source
    html = etree.HTML(text)
    print(html)


def main():
    req()


if __name__ == '__main__':
    main()
