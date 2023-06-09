from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = 0
    exeption = ['', 'invalid']
    for salary in data:
        if salary['max_salary'] not in exeption:
            max_salary = max(max_salary, int(salary['max_salary']))
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = float("inf")
    exeption = ['', 'invalid']
    for salary in data:
        if salary['min_salary'] not in exeption:
            min_salary = min(min_salary, int(salary['min_salary']))
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_salary = int(job['max_salary'])
        min_salary = int(job['min_salary'])
        salary = int(salary)
    except (KeyError, TypeError, ValueError):
        raise ValueError
    if min_salary > max_salary:
        raise ValueError('xablau')
    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except (KeyError, TypeError, ValueError):
            print('error')
    return filtered_jobs
