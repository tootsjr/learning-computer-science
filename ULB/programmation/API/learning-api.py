import requests

base_job_url = "https://jobicy.com/api/v2/remote-jobs"


class Job:
    """
    A class used to represent a job

    Attributes
    ----------
    title : str
        A string containing the job's title
    location : str
        A string containing the location of the job
    salary_min : int
        An integer containing the lowest salary for the position
    salary_max : int
            An integer containing the highest salary for the position
    Methods
    -------
    __str__ (self) -> str
        returns a string containing the information about a job



    """

    def __init__(
        self, title: str, location: str, salary_min: int, salary_max: int
    ) -> None:
        self.title = title
        self.location = location
        self.salary_min = salary_min
        self.salary_max = salary_max

    def __str__(self) -> str:
        return f"{self.title} in : {self.location}\nSalary : {self.salary_min}-{self.salary_max}"


def get_jobs(job_name: str, location: str) -> list:
    """
    returns a list of jobs found using the inputed job_name and location in a query

    Parameters:
                    job_name (str): the 'tag' used in our URL params to find the job
                    location (str): the 'geo' param used to find the location

            Returns:
                    jobs (list): a list containing all found jobs excluding ones found without 'salaryMin' or 'salaryMax'
    """
    response = requests.get(
        base_job_url, params={"geo": location, "tag": job_name, "count": 15}
    )
    if response.status_code != 200:
        print(f"Failed to retreive data error code {response.status_code}")
        return []
    jobs = []
    for data in response.json()["jobs"]:
        if "salaryMin" not in data or "salaryMax" not in data:
            continue
        jobs.append(
            Job(data["jobTitle"], data["jobGeo"], data["salaryMin"], data["salaryMax"])
        )
    return jobs


def compare_jobs(jobs: list):
    filtered_list = sorted(jobs, key=lambda job: job.salary_max, reverse=True)
    for job in filtered_list:
        print(f"{job}\t")


job_titles = input("Enter the jobs (separate with a comma ',') : ")
titles = [t.strip() for t in job_titles.split(",") if t.strip()]
user_inputed_location = input("Enter the location : ")
jobs_list = []
for title in titles:
    for job in get_jobs(title, user_inputed_location):
        jobs_list.append(job)
compare_jobs(jobs_list)
