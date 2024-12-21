<<<<<<< HEAD
from job import Job
from job_application import JobApplication
=======
from src.job import Job
from src.job_application import JobApplication
>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320


from dataclasses import dataclass

@dataclass
class JobContext:
    job: Job = None
    job_application: JobApplication = None