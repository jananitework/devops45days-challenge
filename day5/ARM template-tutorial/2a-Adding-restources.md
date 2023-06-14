## Adding a resource of type storage account

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> $templateFile=".\2b-azstorage.json"

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name storagetemplate --resource-group rg1 --template-file $templateFile
```json

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/storagetemplate",
  "location": null,
  "name": "storagetemplate",
  "properties": {
    "correlationId": "434dd383-cc96-4968-a254-1daaf59c7abf",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT26.5604649S",
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
    "parameters": null,
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
    "templateHash": "17345198972364488499",
    "templateLink": null,
    "timestamp": "2023-06-14T11:41:02.981513+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
 }
 
 ```
 
 ![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/3c35c38a-2990-4c01-9b83-cc8531dfd189)
