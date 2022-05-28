"""
@Author: yanzx
@Date: 2022/5/26 23:17
@Description: 
"""
from pydantic import BaseModel, Field
from typing import List, Dict


class URLModel(BaseModel):
    """
    URL模型类
    """
    congressGroup: List[int] = Field(None, description="{1973-2022, 1951-1972, 1799-1811, 1813-1873}, [1, 2, 3]")
    congress: List[int] = Field(None, description="国会")
    legislationNumbers: str = Field(None, description="eg: hr5")
    restrictionType = 'field'
    restrictionFields: List[str] = ['allBillTitles', 'summary']
    summaryField: str = 'billSummary'
    enterTerms: str = None
    legislationTypes: List[str] = None
    public: bool = True
    private: bool = True
    sponsorTypes: List[str] = ['sponsor']
    committeeActivity: List[int] = None
    satellite: List = Field(None, alias='satellite[]')
    submitted: str = 'Submitted'


class URL:
    """
    Advance Search URL拼接类
    """
    def __init__(self, url_model: URLModel):
        self.url_model = url_model
        self.base_url = "https://www.congress.gov/advanced-search/legislation?"

    def get_url(self):
        """
        获取拼接后的url
        :return:
        """
        res_li = []
        url_dict = self.url_model.dict()
        for key in url_dict.keys():
            value = url_dict.get(key)
            if value is None:
                continue
            elif isinstance(value, List):
                key = key + "[]"
                for item in value:
                    res_li.append(key + "=" + item)
            else:
                res_li.append(key + "=" + str(value))
        res_str = "&".join(res_li)
        return self.base_url + res_str



if __name__ == '__main__':
    congress_group = 1
    data = {
        'congress_group': 1,
    }
    url_model = URLModel(**data)
    res = URL(url_model).get_url()
    print(res)
