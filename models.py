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
    restrictionType: str = Field('field', description="restrictionType")
    restrictionFields: List[str] = Field(['allBillTitles', 'summary'], description="restrictionType")
    summaryField: str = Field('billSummary')
    enterTerms: str = Field(None)
    legislationTypes: List[str] = Field(None)
    public: bool = Field(True)
    private: bool = Field(True)
    sponsorTypes: List[str] = Field(['sponsor'])
    committeeActivity: List[int] = Field(None)
    satellite: List = Field(None, alias='satellite')
    submitted: str = Field('Submitted')
    member: str = Field(None, description='提出人')
    actionTerms: int = Field(None, description='法案所处的阶段 eg: 8000')


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
            if not value:
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
    data = {
        'congress_group': 1,
        'congress': None,
        'member': None,
        'legislationNumbers': None,
        'enterTerms': 'health care',
        'actionTerms': 8000,
        'satellite': None,
    }
    url_model = URLModel(**data)
    res = URL(url_model).get_url()
    print(res)
