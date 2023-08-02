"""
This example shows how to create job from XML file and how to delete job
"""
from config import *
from jenkinsapi.jenkins import Jenkins

jenkins = Jenkins(jenkins_url, username, password)
job_name = "Simple"

print(xml)
# Create Job
job = jenkins.create_job(jobname=job_name, xml=xml)

# Get job from Jenkins by job name
my_job = jenkins[job_name]
print(f'Job {my_job} has been created')

# Delete job using method in Jenkins class
# del jenkins[job_name]
jenkins.delete_job(job_name)
