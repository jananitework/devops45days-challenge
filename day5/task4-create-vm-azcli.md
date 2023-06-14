#### 1. Create resource group

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az group create --name rg3 --location "central india"
{
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg3",
  "location": "centralindia",
  "managedBy": null,
  "name": "rg3",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
```
#### 2. Create SSH keys

#### 3. Create VM using AZ cli

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az vm create --resource-group rg3 --name task4vm --image UbuntuLTS --admin-username jananite --ssh-key-values C:\Users\91887\.ssh\id_rsa.pub
Ignite (November) 2023 onwards "az vm/vmss create" command will deploy Gen2-Trusted Launch VM by default. To know more about the default change and Trusted Launch, please visit https://aka.ms/TLaD
It is recommended to use parameter "--public-ip-sku Standard" to create new VM with Standard public IP. Please note that the default public IP used for VM creation will be changed from Basic to Standard in the future.
Consider using the "Ubuntu2204" alias. On April 30, 2023,the image deployed by the "UbuntuLTS" alias reaches its end of life. The "UbuntuLTS" will be removed with the breaking change release of Fall 2023.
{
  "fqdns": "",
  "id": "/subscriptions/f790a660-c085-4f59-b4db-5637f5559878/resourceGroups/rg3/providers/Microsoft.Compute/virtualMachines/task4vm",
  "location": "centralindia",
  "macAddress": "60-45-BD-72-1A-BE",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "20.219.167.172",
  "resourceGroup": "rg3",
  "zones": ""
}
```

#### 4. SSH using public ip

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> ssh jananite@20.219.167.172

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/ed7900d7-d303-4a4f-9f07-4f57671eab37)
