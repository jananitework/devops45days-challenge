Reference : 
https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template?tabs=azure-cli

# we need a resource group to deploy our resources.
PS C:\Users\91887> az group create --name rg1 --location "Central India"

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1",
  "location": "centralindia",
  "managedBy": null,
  "name": "rg1",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
#Check in the azure portal if the resource group is created

![rg1](https://github.com/jananitework/devops45days-challenge/assets/136428700/8aef10c5-2c7d-4308-ae6c-a961aa97bddc)

# Deploy the newly created template using az cli

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> $templateFile="1b-azuredeploy.json"

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\ARM template-tutorial> az deployment group create --name blanktemplate --resource-group rg1 --template-file $templateFile

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg1/providers/Microsoft.Resources/deployments/blanktemplate",
  "location": null,
  "name": "blanktemplate",
  "properties": {
    "correlationId": "3d96cc07-8f6e-4ef4-810a-ce9505a36aaf",
    "debugSetting": null,
    "dependencies": [],
    "duration": "PT1.0249846S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [],
    "outputs": null,
    "parameters": null,
    "parametersLink": null,
    "providers": [],
    "provisioningState": "Succeeded",
    "templateHash": "11481920352792298114",
    "templateLink": null,
    "timestamp": "2023-06-14T10:37:55.149943+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg1",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/15d1dee5-9bdb-48fb-9cae-7beefebcaf7c)


