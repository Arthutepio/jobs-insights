from src.pre_built.sorting import sort_by


list_jobs = [
    {"date_posted": "2013-04-27", "max_salary": 6000, "min_salary": 3000},
    {"date_posted": "2027-04-27", "max_salary": 5000, "min_salary": 2000},
    {"date_posted": "2023-04-27", "max_salary": 4000, "min_salary": 1000},
]

sort_by_min_salary = [
    {"date_posted": "2023-04-27", "max_salary": 4000, "min_salary": 1000},
    {"date_posted": "2027-04-27", "max_salary": 5000, "min_salary": 2000},
    {"date_posted": "2013-04-27", "max_salary": 6000, "min_salary": 3000},
]

sort_by_max_salary = [
    {"date_posted": "2013-04-27", "max_salary": 6000, "min_salary": 3000},
    {"date_posted": "2027-04-27", "max_salary": 5000, "min_salary": 2000},
    {"date_posted": "2023-04-27", "max_salary": 4000, "min_salary": 1000},
]

sort_by_date_posted = [
    {"date_posted": "2027-04-27", "max_salary": 5000, "min_salary": 2000},
    {"date_posted": "2023-04-27", "max_salary": 4000, "min_salary": 1000},
    {"date_posted": "2013-04-27", "max_salary": 6000, "min_salary": 3000},
]


def test_sort_by_criteria():
    sort_by(list_jobs, "min_salary")
    assert list_jobs == sort_by_min_salary

    sort_by(list_jobs, "max_salary")
    assert list_jobs == sort_by_max_salary

    sort_by(list_jobs, "date_posted")
    assert list_jobs == sort_by_date_posted
