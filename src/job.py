from dataclasses import dataclass
from src.logging import logger

@dataclass
class Job:
<<<<<<< HEAD
    id: str = ""
    title: str = ""
=======
    role: str = ""
>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320
    company: str = ""
    location: str = ""
    link: str = ""
    apply_method: str = ""
    description: str = ""
    summarize_job_description: str = ""
    recruiter_link: str = ""
<<<<<<< HEAD
    # TODO: to move these properties to JobApplication
    resume_path: str = ""
    cover_letter_path: str = ""

    def set_summarize_job_description(self, summarize_job_description):
        logger.debug(f"Setting summarized job description: {summarize_job_description}")
        self.summarize_job_description = summarize_job_description

    def set_job_description(self, description):
        logger.debug(f"Setting job description: {description}")
        self.description = description

    def set_recruiter_link(self, recruiter_link):
        logger.debug(f"Setting recruiter link: {recruiter_link}")
        self.recruiter_link = recruiter_link

=======
    resume_path: str = ""
    cover_letter_path: str = ""

>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320
    def formatted_job_information(self):
        """
        Formats the job information as a markdown string.
        """
<<<<<<< HEAD
        logger.debug(f"Formatting job information for job: {self.title} at {self.company}")
        job_information = f"""
        # Job Description
        ## Job Information 
        - Position: {self.title}
=======
        logger.debug(f"Formatting job information for job: {self.role} at {self.company}")
        job_information = f"""
        # Job Description
        ## Job Information 
        - Position: {self.role}
>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320
        - At: {self.company}
        - Location: {self.location}
        - Recruiter Profile: {self.recruiter_link or 'Not available'}
        
        ## Description
        {self.description or 'No description provided.'}
        """
        formatted_information = job_information.strip()
        logger.debug(f"Formatted job information: {formatted_information}")
        return formatted_information