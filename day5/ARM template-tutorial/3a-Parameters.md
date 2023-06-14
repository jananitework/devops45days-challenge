## Adding "parameters" to ARM template

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> $templateFile=".\3b-storageaccountname-as-parameter.json"

###### parameter name not same as in ARM template 
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name addparams --resource-group rg1 --template-file $templateFile --parameters storageNames='1234'

unrecognized template parameter 'storageNames'. Allowed parameters: storageName

###### parameter name same as previosly created storage account name

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name addparams --resource-group rg1 --template-file $templateFile --parameters storageName='jtew1'

```json

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/addparams",
  "location": null,
  "name": "addparams",
  "properties": {
    "correlationId": "4ad09218-278d-4509-a176-9de58ddb1947",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT0.9679673S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/jtew1",
        "resourceGroup": "rg1"
      }
    ],
    "outputs": null,
    "parameters": {
      "storageName": {
        "type": "String",
        "value": "jtew1"
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
    "templateHash": "4073480931772097755",
    "templateLink": null,
    "timestamp": "2023-06-14T13:52:43.955605+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}

```
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/a3eb7a08-5f71-44b7-891b-64a9735ee859)

###### new storage account name
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name addparams --resource-group rg1 --template-file $templateFile --parameters storageName='jtew2'

```json

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/addparams",
  "location": null,
  "name": "addparams",
  "properties": {
    "correlationId": "f7003e1c-3f4c-434d-9759-26066e315601",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT31.2622962S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/jtew2",
        "resourceGroup": "rg1"
      }
    ],
    "outputs": null,
    "parameters": {
      "storageName": {
        "type": "String",
        "value": "jtew2"
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
    "templateHash": "4073480931772097755",
    "templateLink": null,
    "timestamp": "2023-06-14T13:54:42.844748+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}
```

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/24b9d509-280d-418a-a961-e86fed5e21da)
