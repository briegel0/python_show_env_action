import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = ''
    if my_input == "true":
        ciEnv = os.environ["CI"]
        my_output = f"CI {ciEnv}"
    

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
