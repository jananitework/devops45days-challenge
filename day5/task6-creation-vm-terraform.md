
# Install Terraform on windows 

#### 1. Create service principle 
A Service Principal is an application within Azure Active Directory whose authentication tokens can be used as the client_id, client_secret, and tenant_id fields needed by Terraform (subscription_id can be independently recovered from your Azure account details).

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "id": "f9182f0c-787c-49f3-b5e0-dda139de3996",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "user": {
      "name": "meera0569@gmail.com",
      "type": "user"
    }
  }
]
```

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az ad sp create-for-rbac --name sp1 --role Contributor --scopes /subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996
Creating 'Contributor' role assignment under scope '/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996'
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "0f57c09a-58a5-4be3-a6be-1fcac92535fc",
  "displayName": "sp1",
  "password": "Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa",
  "tenant": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850"
}
```
- appId is the client_id defined above.
- password is the client_secret defined above.
- tenant is the tenant_id defined above.

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/ffdc4cba-5957-4934-af47-b0ff5cfe78ea)

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az login --service-principal -u 0f57c09a-58a5-4be3-a6be-1fcac92535fc -p Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa --tenant 14347c6c-c7da-4f47-a3eb-89e0ac0d8850
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "id": "f9182f0c-787c-49f3-b5e0-dda139de3996",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "user": {
      "name": "0f57c09a-58a5-4be3-a6be-1fcac92535fc",
      "type": "servicePrincipal"
    }
  }
]

```
#### 2. Download terraform binaries and add to system path

# Use terraform to create a VM

Reference: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret
https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-windows-powershell?tabs=bash#create-a-service-principal
