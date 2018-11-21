
  
# Client project 

An agent that  report commits from the users over the network every 60 seconds the following git data:    
    
 - Committing user  
 - Branch  
 - Repository name  
 - File list  
 - Diff  
 - Commit message  
  
### Installation  
run `python reportGit.py` on the local selected git repository  
  
**Notes and imporvments**  
  
 1. uses python 3
 2. runs on a single local git repository while should get a directory as a parameter and scan/report all git repositories underneath it.  
 3. server url is hard coded.  
 4. timing is hard coded.  
 5. need to add installation script  
 6. run as a service