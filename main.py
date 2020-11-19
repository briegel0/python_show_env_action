import os
import requests  # noqa We are just importing this to prove the dependency installed correctly

#  showGithubVars

def main():
    showGitHubVars = os.environ["INPUT_SHOWGITHUBVARS"]

    listOfAppEnvVars = os.environ["INPUT_LISTOFAPPENVVARS"]

    newLineEsc = "%0A"

    my_output = ''
    if showGitHubVars == "true":
        CIEnv = os.environ["CI"]
        GITHUB_WORKFLOWEnv = os.environ["GITHUB_WORKFLOW"]
        GITHUB_RUN_IDEnv = os.environ["GITHUB_RUN_ID"]
        GITHUB_RUN_NUMBEREnv = os.environ["GITHUB_RUN_NUMBER"]
         
        # newline = %0A

        my_output = f"CI {CIEnv} GITHUB_WORKFLOW {GITHUB_WORKFLOWEnv} GITHUB_RUN_ID {GITHUB_RUN_IDEnv}" +  newLineEsc \
                    + f"GITHUB_RUN_NUMBER {GITHUB_RUN_NUMBEREnv}" 

    if len(listOfAppEnvVars) > 0:
        my_list = listOfAppEnvVars.split(",")
        # for env in my_list:




    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
