# Configure Azure storage account as terraform backend

## Prerequisities - resource group, storage account

```
az group create --name rg16 --location "central india"
az storage container create -n tfstate --account-name task16sa
az storage account create -n task16sa -g rg16 -l centralindia --sku Standard_LRS
```

## Set the service principle credentials in power shell

```
$env:ARM_CLIENT_ID = "0f57c09a-58a5-4be3-a6be-1fcac92535fc"
$env:ARM_CLIENT_SECRET = "Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa"
$env:ARM_TENANT_ID = "14347c6c-c7da-4f47-a3eb-89e0ac0d8850"
$env:ARM_SUBSCRIPTION_ID = "f9182f0c-787c-49f3-b5e0-dda139de3996"
```

## Set storage account as backend

```
terraform init -backend-config storage_account_name="task16sa" -backend-config key="task16-vm.tfstate" -backend-config container_name="tfstate" -backend-config access_key="VtfMVzR+WMPW5cA48+MDosagyaCk0BXcj2Dpz2BTDFcGUq/rhJSHTtUK0G7OV5NQmxRVlJxpoR9D+AStuQX0Gw=="  --reconfigure
```

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/7b5160a1-8b45-43a7-83dd-6e8d8a2983b1)

## Terraform init , plan, apply

### When terraform plan runs, the file will be automatically locked

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/85c458c6-cfc1-4358-8e61-888056449f65)

### Contents of the file after terraform apply
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/2392f40c-4a90-428c-b95c-e6a6f3a5e52c)



