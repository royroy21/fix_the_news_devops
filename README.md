This project creates and provisions the devops server for fixthenews.com 

## Terraform (v0.12.24)
Terraform is used for creating, changing and destroying the devops server.

Currently this is designed to be run locally.

Secrets are stored in terraform.tfvars files for each environment.

terraform.tfvars files are not part of this repo.

## Ansible (2.9.9)
Ansible is used for provisioning the devops server.

The devops server is designed to be provisioned locally.

The devops server is responsible for creating, changing, destroying and 
provisioning staging and production environments. 

The devops server is responsible for creating/renewing and pushing SSL 
certificates to environments.

All files in the inventories directory are encrypted. A password.txt file is 
required to decrypt these files. 

The password.txt file is not part of this repo.

## Notes
A directory for both staging and production should exist in the terraform 
directory each with a terraform.tfvars file. These are copied over to the 
devops server at provisioning.

## Quick start
Create devops server:

`cd terraform/devops`

`terraform init`

`terraform apply`


Provision devops server:

`cd ansible`

`ansible-playbook devops_server.yml -i inventories/devops --vault-id password.txt`
