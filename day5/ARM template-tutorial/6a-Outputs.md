### Using "outputs" in template

You can use outputs to return values from the template. It might be helpful, for example, to get the endpoints for your new storage account.

```
"outputs": {
    "storageEndpoint": {
      "type": "object",
      "value": "[reference(variables('uniqueStorageName')).primaryEndpoints]"
    }
  }
 ```
 The type of returned value is set to object, which means it returns a JSON object.
 
 PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> $templateFile=".\6b-Using-outputs.json"
 
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name getoutputs --resource-group rg1 --template-file $templateFile --parameters storagePrefix=abcd

```json
{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/getoutputs",
  "location": null,
  "name": "getoutputs",
  "properties": {
    "correlationId": "6acf7200-9846-417c-b4c2-6abba80dc52d",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT30.2145804S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/abcdcpbwfsgluargk",
        "resourceGroup": "rg1"
      }
    ],
    "outputs": {
      "storageEndpoint": {
        "type": "Object",
        ** "value": {
          "blob": "https://abcdcpbwfsgluargk.blob.core.windows.net/",
          "dfs": "https://abcdcpbwfsgluargk.dfs.core.windows.net/",
          "file": "https://abcdcpbwfsgluargk.file.core.windows.net/",
          "queue": "https://abcdcpbwfsgluargk.queue.core.windows.net/",
          "table": "https://abcdcpbwfsgluargk.table.core.windows.net/",
          "web": "https://abcdcpbwfsgluargk.z29.web.core.windows.net/"
        } **
      }
    },
    "parameters": {
      "location": {
        "type": "String",
        "value": "centralindia"
      },
      "storagePrefix": {
        "type": "String",
        "value": "abcd"
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
    "templateHash": "7000218183965269215",
    "templateLink": null,
    "timestamp": "2023-06-14T14:48:47.492859+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}
```
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/a15eec13-c6d8-4754-b1ca-4444f9cb791e)
