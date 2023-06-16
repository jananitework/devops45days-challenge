
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
#### 2. Create azure key vault and store the credentials for SP

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az keyvault create --name azurecredentials --resource-group rg6 --location "central india"
Resource provider 'Microsoft.KeyVault' used by this operation is not registered. We are registering for you.
Registration succeeded.
```
``` json

{
  "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.KeyVault/vaults/azurecredentials",
  "location": "centralindia",
  "name": "azurecredentials",
  "properties": {
    "accessPolicies": [
      {
        "applicationId": null,
        "objectId": "c17ed43a-02da-48c6-b8f7-1b940ae0ba26",
        "permissions": {
          "certificates": [
            "all"
          ],
          "keys": [
            "all"
          ],
          "secrets": [
            "all"
          ],
          "storage": [
            "all"
          ]
        },
        "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850"
      }
    ],
    "createMode": null,
    "enablePurgeProtection": null,
    "enableRbacAuthorization": null,
    "enableSoftDelete": true,
    "enabledForDeployment": false,
    "enabledForDiskEncryption": null,
    "enabledForTemplateDeployment": null,
    "hsmPoolResourceId": null,
    "networkAcls": null,
    "privateEndpointConnections": null,
    "provisioningState": "Succeeded",
    "publicNetworkAccess": "Enabled",
    "sku": {
      "family": "A",
      "name": "standard"
    },
    "softDeleteRetentionInDays": 90,
    "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "vaultUri": "https://azurecredentials.vault.azure.net/"
  },
  "resourceGroup": "rg6",
  "systemData": {
    "createdAt": "2023-06-16T08:14:39.788000+00:00",
    "createdBy": "0f57c09a-58a5-4be3-a6be-1fcac92535fc",
    "createdByType": "Application",
    "lastModifiedAt": "2023-06-16T08:14:39.788000+00:00",
    "lastModifiedBy": "0f57c09a-58a5-4be3-a6be-1fcac92535fc",
    "lastModifiedByType": "Application"
  },
  "tags": {},
  "type": "Microsoft.KeyVault/vaults"
}
```

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az keyvault secret set --vault-name azurecredentials --name 'subscriptionid' --value 'f9182f0c-787c-49f3-b5e0-dda139de3996' ```

``` json
{
  "attributes": {
    "created": "2023-06-16T08:20:20+00:00",
    "enabled": true,
    "expires": null,
    "notBefore": null,
    "recoveryLevel": "Recoverable+Purgeable",
    "updated": "2023-06-16T08:20:20+00:00"
  },
  "contentType": null,
  "id": "https://azurecredentials.vault.azure.net/secrets/subscriptionid/f0aa9b562a134d39b1e66db4be978843",
  "kid": null,
  "managed": null,
  "name": "subscriptionid",
  "tags": {
    "file-encoding": "utf-8"
  },
  "value": "f9182f0c-787c-49f3-b5e0-dda139de3996"
}
```

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az keyvault secret set --vault-name azurecredentials --name 'tenantid' --value '14347c6c-c7da-4f47-a3eb-89e0ac0d8850' ```

``` json
{
  "attributes": {
    "created": "2023-06-16T08:20:46+00:00",
    "enabled": true,
    "expires": null,
    "notBefore": null,
    "recoveryLevel": "Recoverable+Purgeable",
    "updated": "2023-06-16T08:20:46+00:00"
  },
  "contentType": null,
  "id": "https://azurecredentials.vault.azure.net/secrets/tenantid/d844d71f699a4f1388e61f1531912957",
  "kid": null,
  "managed": null,
  "name": "tenantid",
  "tags": {
    "file-encoding": "utf-8"
  },
  "value": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850"
}
```

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az keyvault secret set --vault-name azurecredentials --name 'clientid' --value '0f57c09a-58a5-4be3-a6be-1fcac92535fc' ```

``` json
{
  "attributes": {
    "created": "2023-06-16T08:21:12+00:00",
    "enabled": true,
    "expires": null,
    "notBefore": null,
    "recoveryLevel": "Recoverable+Purgeable",
    "updated": "2023-06-16T08:21:12+00:00"
  },
  "contentType": null,
  "id": "https://azurecredentials.vault.azure.net/secrets/clientid/405b538e7ef54b4f9d04e0c6eaa740c7",
  "kid": null,
  "managed": null,
  "name": "clientid",
  "tags": {
    "file-encoding": "utf-8"
  },
  "value": "0f57c09a-58a5-4be3-a6be-1fcac92535fc"
}
```

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az keyvault secret set --vault-name azurecredentials --name 'clientsecret' --value 'Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa' ```

``` json
{
  "attributes": {
    "created": "2023-06-16T08:21:37+00:00",
    "enabled": true,
    "expires": null,
    "notBefore": null,
    "recoveryLevel": "Recoverable+Purgeable",
    "updated": "2023-06-16T08:21:37+00:00"
  },
  "contentType": null,
  "id": "https://azurecredentials.vault.azure.net/secrets/clientsecret/e0643c106eb248dfbf2a87cad50821b8",
  "kid": null,
  "managed": null,
  "name": "clientsecret",
  "tags": {
    "file-encoding": "utf-8"
  },
  "value": "Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa"
}
```

#### 3. Check if your are authorised to read the key vault's secret.

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/8e77f68d-57db-4664-a4cb-6f15ca489998)

If not, 
- check if key vault reader role is assigned to SP
- check if key vault reader role is assigned to your subscription
- Check for access policies tab in KeyVault and add the necessary user and sp.

#### 4. Download terraform binaries and add to system path

# Use terraform to create a VM

Reference: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret
https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-windows-powershell?tabs=bash#create-a-service-principal
