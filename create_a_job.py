"""
This example shows how to create job from XML file and how to delete job
"""
from __future__ import print_function
from pkg_resources import resource_string
from jenkinsapi.jenkins import Jenkins

jenkins = Jenkins("http://localhost:8080")
job_name = "foo_job2"
xml = resource_string("examples", "addjob.xml")

print(xml)

job = jenkins.create_job(jobname=job_name, xml=xml)

# Get job from Jenkins by job name
my_job = jenkins[job_name]
print(my_job)

# Delete job using method in Jenkins class
#
# Another way is to use:
#
# del jenkins[job_name]
jenkins.delete_job(job_name)

from jenkinsapi.jenkins import Jenkins
jenkins_url = 'http://ip172-18-0-11-cj4rl40gftqg0094264g-8080.direct.labs.play-with-docker.com/'
server = Jenkins(jenkins_url, username='k', password='k')
xml = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <builders>
    <hudson.tasks.Shell>
      <command>echo $JENKINS_VERSION</command>
    </hudson.tasks.Shell>
  </builders>
</project>"""

server.create_job('Test123', xml)
