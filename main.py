import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = 'Show No GitHub env values'
    if my_input == "true":
        CIEnv = os.environ["CI"]
        GITHUB_WORKFLOWEnv = os.environ["GITHUB_WORKFLOW"]
        GITHUB_RUN_IDEnv = os.environ["GITHUB_RUN_ID"]
        GITHUB_RUN_NUMBEREnv = os.environ["GITHUB_RUN_NUMBER"]
        my_output = (f"CI {CIEnv} GITHUB_WORKFLOW {GITHUB_WORKFLOWEnv} GITHUB_RUN_ID {GITHUB_RUN_IDEnv}\n" 
                    + f"GITHUB_RUN_NUMBER {GITHUB_RUN_NUMBEREnv}" )


    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
