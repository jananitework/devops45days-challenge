### Using variables in ARM templates

In 5b json, we make use of a variable named uniqueStorageName for providing a unique name to our storage account

```
  "parameters": {
    "storagePrefix": {
      "type": "string",
      "minLength": 3,
      "maxLength": 11
    },
"variables": {
    "uniqueStorageName": "[concat(parameters('storagePrefix'), uniqueString(resourceGroup().id))]"
  },
```
- The uniqueString function creates a 13-character hash value.
- The concat function takes values and combines them. For this variable, it takes the string from the parameter and the string from the uniqueString function and combines them into one string.
- The storagePrefix parameter lets you pass in a prefix that helps you identify storage accounts.

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name addvariables --resource-group rg1 --template-file $templateFile --parameters storagePrefix=abc

```json

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/addvariables",
  "location": null,
  "name": "addvariables",
  "properties": {
    "correlationId": "3946d7ad-2369-47d8-ae81-49f51a34b37c",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT30.8992971S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [
      {
        **"id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/abccpbwfsgluargk",**
        "resourceGroup": "rg1"
      }
    ],
    "outputs": null,
    "parameters": {
      "location": {
        "type": "String",
        "value": "centralindia"
      },
      "storagePrefix": {
        "type": "String",
        "value": "abc"
      },
      "storageSKU": {
        "type": "String",
        "value": "Standard_LRS"
      }
    },
    "parametersLink": null,
    "providers": [
      {
        "id": null,
        "namespace": "Microsoft.Storage",
        "providerAuthorizationConsentState": null,
        "registrationPolicy": null,
        "registrationState": null,
        "resourceTypes": [
          {
            "aliases": null,
            "apiProfiles": null,
            "apiVersions": null,
            "capabilities": null,
            "defaultApiVersion": null,
            "locationMappings": null,
            "locations": [
              "centralindia"
            ],
            "properties": null,
            "resourceType": "storageAccounts",
            "zoneMappings": null
          }
        ]
      }
    ],
    "provisioningState": "Succeeded",
    "templateHash": "17737384834291520106",
    "templateLink": null,
    "timestamp": "2023-06-14T14:37:08.269785+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}
```
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/e6db0fd4-cf21-4c5a-9f13-10b1ba7b8ce6)

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/ca273d5c-f478-4c5a-8e84-d61ea2bbc9b1)
