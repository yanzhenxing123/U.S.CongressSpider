"""
@Author: yanzx
@Date: 2022/5/19 22:40
@Description: This a test file
"""

import re
import utils

from lxml import etree
root_url = "https://www.congress.gov/"

def main():
    li = [[], [], [], 1]
    if any(li):
        res = map(str, li)
        print("".join(res).replace('[', '').replace(']', ''))
if __name__ == '__main__':
    # with open('health_care_demo.txt', 'w') as f:
    #     text = "dadfa"
    #     f.write(text)
    main()
