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
            + f"GITHUB_RUN_NUMBER={GITHUB_RUN_NUMBEREnv}" + newLineEsc \
            + f"GITHUB_ACTION={os.environ['GITHUB_ACTION']}" + newLineEsc \
            + f"GITHUB_ACTIONS={os.environ['GITHUB_ACTIONS']}" + newLineEsc \
            + f"GITHUB_ACTOR={os.environ['GITHUB_ACTOR']}" + newLineEsc \
            + f"GITHUB_REPOSITORY={os.environ['GITHUB_REPOSITORY']}" + newLineEsc \
            + f"GITHUB_EVENT_NAME={os.environ['GITHUB_EVENT_NAME']}" + newLineEsc \
            + f"GITHUB_EVENT_PATH={os.environ['GITHUB_EVENT_PATH']}" + newLineEsc \
            + f"GITHUB_WORKSPACE={os.environ['GITHUB_WORKSPACE']}" + newLineEsc \
            + f"GITHUB_SHA={os.environ['GITHUB_SHA']}" + newLineEsc \
            + f"GITHUB_REF={os.environ['GITHUB_REF']}" + newLineEsc \
            + f"GITHUB_HEAD_REF={os.environ['GITHUB_HEAD_REF']}" + newLineEsc \
            + f"GITHUB_BASE_REF={os.environ['GITHUB_BASE_REF']}" + newLineEsc \
            + f"GITHUB_SERVER_URL={os.environ['GITHUB_SERVER_URL']}" + newLineEsc \
            + f"GITHUB_API_URL={os.environ['GITHUB_API_URL']}" + newLineEsc \
            + f"GITHUB_GRAPHQL_URL={os.environ['GITHUB_GRAPHQL_URL']}" + newLineEsc \

    if len(listOfAppEnvVars) > 0:
        my_output += newLineEsc + "App Env Vars " + newLineEsc
        my_list = listOfAppEnvVars.split(",")
        for appEnvVar in my_list:
            appEnvValue = os.environ[appEnvVar]
            my_output +=  f"{appEnvVar}={appEnvValue}" + newLineEsc


    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
