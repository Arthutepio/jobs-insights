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
    print("XXXXXXXXXXXXX", data_jobs_csv)
    list_column_job_type = set([type["job_type"] for type in data_jobs_csv])
    return list(list_column_job_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
