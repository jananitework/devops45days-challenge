### Creating a Ubuntu VM using ARM template

##### 1. We need a resource group
``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az group create --name rg2 --location "central india" ```

<details>
<summary>JSON output</summary>

```json
{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2",
  "location": "centralindia",
  "managedBy": null,
  "name": "rg2",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
```

</details>

##### 2. Create ssh keys 
```ssh-keygen -m PEM -t rsa -b 4096 ```
Note down the path

##### 3.a. Create an ARM template 
- Parameters :
    - projectName
    - location
    - adminUsername
    - adminPublicKey
    - vmSize

- Variables :
    - "vNetName":task3-vnet
    - "vNetAddressPrefixes": "10.0.0.0/16",
    - "vNetSubnetName": "default",
    - "vNetSubnetAddressPrefix": "10.0.0.0/24",
    - "vmName": task3-vm
    - "publicIPAddressName": task3-ip
    - "networkInterfaceName": task3-nic
    - "networkSecurityGroupName": task3-nsg
    - "networkSecurityGroupName2": default-nsg

- Resources :
    - Microsoft.Network/networkSecurityGroups
    - Microsoft.Network/publicIPAddresses
    - Microsoft.Network/virtualNetworks
    - Microsoft.Network/networkInterfaces
    - Microsoft.Compute/virtualMachines
  
 ##### 3.b. Create parameter file
  
 ##### 4. Deploying ARM template

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> $templateFile="task3-create-ubuntu-ARM.json"
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> $parameterFile="task3-parameter.json"

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az deployment group create --resource-group rg2  --template-file $templateFile --parameters  $parameterFile
```
<details>
<summary>JSON output</summary>

```json

{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Resources/deployments/task3-create-ubuntu-ARM",
  "location": null,
  "name": "task3-create-ubuntu-ARM",
  "properties": {
    "correlationId": "50ada299-ce07-4dbd-a02c-afc9cb935fe8",
    "debugSetting": null,
    "dependencies": [
      {
        "dependsOn": [
          {
            "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkSecurityGroups/default-nsg",
            "resourceGroup": "rg2",
            "resourceName": "default-nsg",
            "resourceType": "Microsoft.Network/networkSecurityGroups"
          }
        ],
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/virtualNetworks/task3-vnet",
        "resourceGroup": "rg2",
        "resourceName": "task3-vnet",
        "resourceType": "Microsoft.Network/virtualNetworks"
      },
      {
        "dependsOn": [
          {
            "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/publicIPAddresses/task3-ip",
            "resourceGroup": "rg2",
            "resourceName": "task3-ip",
            "resourceType": "Microsoft.Network/publicIPAddresses"
          },
          {
            "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/virtualNetworks/task3-vnet",
            "resourceGroup": "rg2",
            "resourceName": "task3-vnet",
            "resourceType": "Microsoft.Network/virtualNetworks"
          },
          {
            "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkSecurityGroups/task3-nsg",
            "resourceGroup": "rg2",
            "resourceName": "task3-nsg",
            "resourceType": "Microsoft.Network/networkSecurityGroups"
          }
        ],
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkInterfaces/task3-nic",
        "resourceGroup": "rg2",
        "resourceName": "task3-nic",
        "resourceType": "Microsoft.Network/networkInterfaces"
      },
      {
        "dependsOn": [
          {
            "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkInterfaces/task3-nic",
            "resourceGroup": "rg2",
            "resourceName": "task3-nic",
            "resourceType": "Microsoft.Network/networkInterfaces"
          }
        ],
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Compute/virtualMachines/task3-vm",
        "resourceGroup": "rg2",
        "resourceName": "task3-vm",
        "resourceType": "Microsoft.Compute/virtualMachines"
      }
    ],
    "duration": "PT38.2809592S",
    "error": null,
    "mode": "Incremental",
    "onErrorDeployment": null,
    "outputResources": [
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Compute/virtualMachines/task3-vm",
        "resourceGroup": "rg2"
      },
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkInterfaces/task3-nic",
        "resourceGroup": "rg2"
      },
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkSecurityGroups/default-nsg",
        "resourceGroup": "rg2"
      },
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/networkSecurityGroups/task3-nsg",
        "resourceGroup": "rg2"
      },
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/publicIPAddresses/task3-ip",
        "resourceGroup": "rg2"
      },
      {
        "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg2/providers/Microsoft.Network/virtualNetworks/task3-vnet",
        "resourceGroup": "rg2"
      }
    ],
    "outputs": null,
    "parameters": {
      "adminPublicKey": {
        "type": "String",
        "value": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC0MW50Kd/EHwPzFYI/CkCq+PnvPGXILuWn+HXO5aOV17GXgkOVE8aptYk5KBEFl+pYbelN/8IwvFK0VMxX1MkODpKhfZsUCxB43WsZlkO1z7xzI+4Le7cLpPE9DVBa0o23Nc9/swkh8zKA0twUuRs+AekLDyYP1vImKV65f8JNDnYinRTGH39Q5mjklL9v0IQrkfQF23ZYYQYvHQTa25WDEFR7gI9N/bjSya995Irm3J9Uk0/puG7p95BQZ2/Sqq1LztlDHDrk62eCUQf60/+fMn8rcDgpCB4S6gLUcEeiatwfu7AuHbaufE7mnAtAmUsc7R3jClaNKgdNdOitA8CvKC1RYI2PV9syxNt9nzG7LlzVThoXOgdxPqQEEGDbYht4FCfUP4NgOnJFlAeKY3hEQw4MpBOlz/tiRcaNWErQxmynvuhkeuZRDAra7ZOcwU784tH3UJW6fodzTSm+K9odtp3EHr4Tu0iwY93Lx380zC7PdZV01ZEP4UyW9vCGBlLvVCOMMUMFCCxX7BvfhgA1DN+BpBQNTlkkuWYljkO1BUQ3vyfMrsWXkftQEIWPlDCICGWH8QbCvHcmoY5teJ/J1SYj12ZQuE0/4k3MSA+uCOtWoL/fH9AYebAOFc8/EZQB0b647PsqCgXKUuC8yox/vPmzoHEGRiSR9uWWE5+2YQ== 91887@DESKTOP-CNIQLGC"
      },
      "adminUsername": {
        "type": "String",
        "value": "jananite"
      },
      "location": {
        "type": "String",
        "value": "centralindia"
      },
      "projectName": {
        "type": "String",
        "value": "task3"
      },
      "vmSize": {
        "type": "String",
        "value": "Standard_D2s_v3"
      }
    },
    "parametersLink": null,
    "providers": [
      {
        "id": null,
        "namespace": "Microsoft.Network",
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
            "resourceType": "networkSecurityGroups",
            "zoneMappings": null
          },
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
            "resourceType": "publicIPAddresses",
            "zoneMappings": null
          },
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
            "resourceType": "virtualNetworks",
            "zoneMappings": null
          },
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
            "resourceType": "networkInterfaces",
            "zoneMappings": null
          }
        ]
      },
      {
        "id": null,
        "namespace": "Microsoft.Compute",
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
            "resourceType": "virtualMachines",
            "zoneMappings": null
          }
        ]
      }
    ],
    "provisioningState": "Succeeded",
    "templateHash": "15431376192861435978",
    "templateLink": null,
    "timestamp": "2023-06-14T16:54:50.099774+00:00",
    "validatedResources": null
  },
  "resourceGroup": "rg2",
  "tags": null,
  "type": "Microsoft.Resources/deployments"
}
```
</details>

##### 5. SSH to the server

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az vm show --resource-group rg2 --name "task3-vm" --show-details --query publicIps --output tsv
20.198.64.31

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> ssh jananite@20.198.64.31
```

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/3bdc6d01-349a-4f89-8152-a1d797ebf48c)
