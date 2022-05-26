"""
@Author: yanzx
@Date: 2022/5/26 23:17
@Description: 
"""
from pydantic import BaseModel, Field
from typing import List, Dict


class URL(BaseModel):
    """
    advance search基类
    """
    congressGroup: List[int] = None
    congress: List[int] = None
    legislationNumbers: str = None
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


if __name__ == '__main__':
    url = URL(satellite=[1])
    print(url.json())