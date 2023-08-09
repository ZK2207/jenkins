jenkins_url = 'http://ip172-18-0-13-cj9g14mfml8g009qun6g-8080.direct.labs.play-with-docker.com/'
username = 'zoe'
password = 'zoe'
xml = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <builders>
    <hudson.tasks.Shell>
      <command>echo $JENKINS_VERSION</command>
    </hudson.tasks.Shell>
  </builders>
</project>"""
