### Deploying template by making use of functions

In 3b, we hardcoded the location name. In 4b json file, we use resourceGroup() function to get the location

```
"location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]"
    }
```

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name addlocationparameter --resource-group rg1 --template-file $templateFile --parameters storageName=jtew3

```json

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/addlocationparameter",
  "location": null,
  "name": "addlocationparameter",
  "properties": {
    "correlationId": "62de8c79-fdc7-4cd6-b17f-0dd5f9fe6531",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT29.7466945S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/jtew3",
        "resourceGroup": "rg1"
      }
    ],
    "outputs": null,
    "parameters": {
      "location": {
        "type": "String",
        "value": "centralindia"
      },
      "storageName": {
        "type": "String",
        "value": "jtew3"
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
            **"locations": [**
              **"centralindia"**
            **],**
            "properties": null,
            "resourceType": "storageAccounts",
            "zoneMappings": null
          }
        ]
      }
    ],
    "provisioningState": "Succeeded",
    "templateHash": "8780199338499280860",
    "templateLink": null,
    "timestamp": "2023-06-14T14:25:17.426963+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}
```

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/460c4251-8a23-44ad-b3fa-292762177129)
