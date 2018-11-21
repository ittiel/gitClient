
# Client project  
Reports to the GIT report server every 60 seconds the following git data:  
  
  - Committing user
  - Branch
  - Repository name
  - File list
  - Diff
  - Commit message

### Installation
run `python reportGit.py` on the local selected git repository

**Notes and imporvments**

 1. runs on a single local git repository while should get a directory as a parameter and scan/report all git repositories underneath it.
 2. server url is hard coded.
 3. timing is hard coded.
 4. need to add installation script
 5. run as a service
