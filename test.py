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
    # html = req()
    with open("./health_care_demo.txt") as f:
        text = f.read()
        html = etree.HTML(text)

    # 总的大框框
    main_element = html.xpath("//div[@id='main']")[0]
    item_elements = main_element.xpath("./ol/li[@class='expanded']")

    # for item_element in item_elements:
    #     try:
    #         get_item(item_element)
    #     except Exception:
    #         pass

    get_item(item_elements[12])



def get_item(item_element):
    # 单个法案信息
    item = {}
    # 法案的id, 搜索后排序的id
    bill_id = "".join(item_element.xpath("./text()"))
    bill_id = re.findall(r'\d+', bill_id)[0]
    # 法案的heading, eg:  H.R.6776 — 117th Congress (2021-2022)
    heading_text = item_element.xpath(".//span[@class='result-heading']//text()")
    heading = "".join(heading_text)
    # 法案的bill_url, 详细信息
    bill_url = item_element.xpath(".//span[@class='result-heading']/a/@href")[0]
    bill_url = utils.format_url(bill_url)
    # 法案的title, eg: Health Care Worker and First Responder Social Security Beneficiary Choice Act of 2022
    title_text = item_element.xpath(".//span[@class='result-title']//text()")
    title = "".join(title_text)
    # 法案的类型 eg: BILL、RESOLUTION、...
    type = item_element.xpath(".//span[@class='visualIndicator']/text()")[0]
    # 法案的进程
    tracker = item_element.xpath(".//span[@class='result-item result-tracker']//li[@class='selected']/text()")
    tracker = item_element.xpath(".//span[@class='result-item result-tracker']//li[@class='selected mediumTrack last']/text()")[0] if not tracker else tracker[0]
    item['bill_id'] = bill_id
    item['type'] = type
    item['tracker'] = tracker
    item['heading'] = heading
    item['bill_url'] = bill_url
    item['title'] = title

    # Sponsor Committees Latest_Action
    result_item_elements = item_element.xpath(".//span[@class='result-item']")
    for result_item_element in result_item_elements:
        keys = result_item_element.xpath("./strong/text()")
        values = result_item_element.xpath(".//text()")
        for key in keys:
            index = values.index(key) + 1
            if key == 'Sponsor:':
                index_Cosponsors = values.index('Cosponsors:')
                value = "".join(values[index: index_Cosponsors])
                Sponsor_url = result_item_element.xpath('./a[1]/@href')[0]
                Sponsor_url = utils.format_url(Sponsor_url)
                item['Sponsor_url'] = Sponsor_url
            else:
                value = "".join(values[index:])
                # 如果是贡献者，那么将其余部分去掉
                if key == 'Cosponsors:':
                    try:
                        value = re.findall(r'\d+', value)[0]
                    except Exception:
                        value = 0
            item[key[:-1]] = value
    utils.print_dict(item)



    # print(item['bill_id'])

if __name__ == '__main__':
    # with open('health_care_demo.txt', 'w') as f:
    #     text = "dadfa"
    #     f.write(text)
    main()
