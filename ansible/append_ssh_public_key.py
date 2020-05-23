import os

"""
Used when provisioning the devops server. 
This appends the ssh public key that was created in a previous 
task to terraform.tfvars files for each environment.
"""

TERRAFORM_SECRETS_FILE = "/code/terraform/{environment}/terraform.tfvars"
ID_RSA_PUB = "~/.ssh/id_rsa.pub"
ENVIRONMENTS = [
    "staging",
    "production",
]


def get_id_rsa_pub():
    return os.popen(f"cat {ID_RSA_PUB}").read().strip(" \n")


def append_to_file(environment, id_rsa_pub):
    path = TERRAFORM_SECRETS_FILE.format(environment=environment)
    if not os.path.exists(path):
        print(f"Skipping {path}")
        return

    with open(path, "a") as _file:
        print(f"Appending to {path}")
        _file.write(f'public_key = "{id_rsa_pub}"')


def run():
    id_rsa_pub = get_id_rsa_pub()
    for environment in ENVIRONMENTS:
        append_to_file(environment, id_rsa_pub)


run()
