import os
import requests  # noqa We are just importing this to prove the dependency installed correctly

#  showGithubVars

def main():
    my_input = os.environ["INPUT_SHOWGITHUBVARS"]

    my_output = 'Show No GitHub env values'
    if my_input == "true":
        CIEnv = os.environ["CI"]
        GITHUB_WORKFLOWEnv = os.environ["GITHUB_WORKFLOW"]
        GITHUB_RUN_IDEnv = os.environ["GITHUB_RUN_ID"]
        GITHUB_RUN_NUMBEREnv = os.environ["GITHUB_RUN_NUMBER"]
         
        # newline = %0A

        my_output = (f"CI {CIEnv} GITHUB_WORKFLOW {GITHUB_WORKFLOWEnv} GITHUB_RUN_ID {GITHUB_RUN_IDEnv}%0A" 
                    + f"GITHUB_RUN_NUMBER {GITHUB_RUN_NUMBEREnv}" )

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
