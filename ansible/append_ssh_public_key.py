#!/usr/bin/env python3
import os

"""
Used when provisioning the devops server. 
This appends the ssh public key that was created in a previous 
task to terraform.tfvars files for each environment.
"""

ENVIRONMENTS = [
    "staging",
    "production",
]
ID_RSA_PUB = "home/ubuntu/.ssh/id_rsa.pub"
TERRAFORM_SECRETS_FILE = "/code/terraform/{environment}/terraform.tfvars"


def run():
    id_rsa_pub = get_id_rsa_pub()
    for environment in ENVIRONMENTS:
        append_to_file(environment, id_rsa_pub)


def get_id_rsa_pub():
    with open(ID_RSA_PUB, "r") as _file:
        return _file.read().strip("\n")


def append_to_file(environment, id_rsa_pub):
    path = TERRAFORM_SECRETS_FILE.format(environment=environment)
    if not os.path.exists(path):
        print(f"Skipping {path}")
        return

    with open(path, "a") as _file:
        print(f"Appending to {path}")
        _file.write(f'public_key = "{id_rsa_pub}"')


if __name__ == "__main__":
    run()
