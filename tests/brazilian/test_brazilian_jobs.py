from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    expected_result = {
        "title": "Maquinista", "salary": "2000", "type": "trainee"
    }
    job_list = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert job_list[0] == expected_result
