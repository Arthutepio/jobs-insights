from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    list_column_indrustry = set([industry['industry']
                                 for industry in data
                                 if industry['industry'] not in ''])
    return list_column_indrustry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industries = []
    for industries in jobs:
        if industries['industry'] == industry:
            filtered_industries.append(industries)
    return filtered_industries
