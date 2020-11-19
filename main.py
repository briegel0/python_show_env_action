import os
import requests  # noqa We are just importing this to prove the dependency installed correctly

#  showGithubVars

def main():
    showGitHubVars = os.environ["INPUT_SHOWGITHUBVARS"]

    listOfAppEnvVars = os.environ["INPUT_LISTOFAPPENVVARS"]

    newLineEsc = "%0A"

    my_output = ''
    if showGitHubVars == "true":
        my_output = newLineEsc + 'Git Hub Vars'
        CIEnv = os.environ["CI"]
        GITHUB_WORKFLOWEnv = os.environ["GITHUB_WORKFLOW"]
        GITHUB_RUN_IDEnv = os.environ["GITHUB_RUN_ID"]
        GITHUB_RUN_NUMBEREnv = os.environ["GITHUB_RUN_NUMBER"]
         
        # newline = %0A

        my_output += newLineEsc + f"CI={CIEnv}" + newLineEsc  \
            + f"GITHUB_WORKFLOW={GITHUB_WORKFLOWEnv}" + newLineEsc  \
            + f"GITHUB_RUN_ID={GITHUB_RUN_IDEnv}" + newLineEsc \
            + f"GITHUB_RUN_NUMBER={GITHUB_RUN_NUMBEREnv}" 



    if len(listOfAppEnvVars) > 0:
        my_output += newLineEsc + "App Env Vars " + newLineEsc
        my_list = listOfAppEnvVars.split(",")
        for appEnvVar in my_list:
            appEnvValue = os.environ[appEnvVar]
            my_output +=  f"{appEnvVar}={appEnvValue}" + newLineEsc


    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
