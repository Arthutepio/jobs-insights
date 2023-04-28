import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", newline="") as file:
        reader_csv = csv.DictReader(file)
        list_dict = [row for row in reader_csv]
    return list_dict


def get_unique_job_types(path: str) -> List[str]:
    data_jobs_csv = read(path)
    list_column_job_type = set([type["job_type"] for type in data_jobs_csv])
    return list_column_job_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
