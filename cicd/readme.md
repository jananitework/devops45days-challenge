# Python django - Jenkins - Argocd - K8s

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/1ac155c6-fa30-4ba0-99b9-418811f2402f)


# E2E demo 
https://github.com/jananitework/devops45days-challenge/blob/main/cicd/e2e-demo/readme.md

# Prerequisites 

1. Vm1 : To develop the source code for django and containerize it 
2. Jenkins vm 
3. Aks cluster : For deployments 
4. ACR : Repository for django images


## 1. Creation of vm1 for checking django source code

- Create a new resource group named "cicd"
- Create a new azure vm in that resource group with minimal compute (Standard B1s)
- Allow port 22 for ssh login

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/d5e8ca3e-6a7c-4974-8e64-878c09c9b03e)

  
## 2. Creation of Jenkins VM

- Follow the exact same procedure as in https://github.com/iam-veeramalla/Jenkins-Zero-To-Hero#readme
- Install GitHub plugin

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/01ca3f25-40e1-4341-89b0-df3d8093ee09)


## 3. Creation of AKS cluster for deployments

- Create an AKS cluster with minimal compute
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/63cb79e8-e201-4f47-90c9-a776b9b7f39f)

- Create a pod.yaml file to run the djangoapp as pod and expose it via loadbalancer service.
   - https://github.com/jananitework/devops45days-challenge/blob/main/cicd/Django-webapp/django-app-pod-svc.yaml

- Note : if there is an issue with pulling images run the following command

```az aks update -n dev-aks -g cicd --attach-acr /subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/cicd/providers/Microsoft.ContainerRegistry/registries/cicddjangoimages ```

<details>
<summary>Output</summary>

<json>
AAD role propagation done[############################################]  100.0000%{
  "aadProfile": null,
  "addonProfiles": {
    "azureKeyvaultSecretsProvider": {
      "config": null,
      "enabled": false,
      "identity": null
    },
    "azurepolicy": {
      "config": null,
      "enabled": false,
      "identity": null
    }
  },
  "agentPoolProfiles": [
    {
      "availabilityZones": null,
      "count": 1,
      "creationData": null,
      "currentOrchestratorVersion": "1.25.6",
      "enableAutoScaling": false,
      "enableEncryptionAtHost": null,
      "enableFips": false,
      "enableNodePublicIp": false,
      "enableUltraSsd": null,
      "gpuInstanceProfile": null,
      "hostGroupId": null,
      "kubeletConfig": null,
      "kubeletDiskType": "OS",
      "linuxOsConfig": null,
      "maxCount": null,
      "maxPods": 110,
      "minCount": null,
      "mode": "System",
      "name": "agentpool",
      "nodeImageVersion": "AKSUbuntu-2204gen2containerd-202306.26.0",
      "nodeLabels": null,
      "nodePublicIpPrefixId": null,
      "nodeTaints": null,
      "orchestratorVersion": "1.25.6",
      "osDiskSizeGb": 128,
      "osDiskType": "Managed",
      "osSku": "Ubuntu",
      "osType": "Linux",
      "podSubnetId": null,
      "powerState": {
        "code": "Running"
      },
      "provisioningState": "Succeeded",
      "proximityPlacementGroupId": null,
      "scaleDownMode": null,
      "scaleSetEvictionPolicy": null,
      "scaleSetPriority": null,
      "spotMaxPrice": null,
      "tags": null,
      "type": "VirtualMachineScaleSets",
      "upgradeSettings": null,
      "vmSize": "Standard_B2s",
      "vnetSubnetId": null,
      "workloadRuntime": null
    }
  ],
  "apiServerAccessProfile": null,
  "autoScalerProfile": null,
  "autoUpgradeProfile": {
    "upgradeChannel": "patch"
  },
  "azureMonitorProfile": null,
  "azurePortalFqdn": "dev-aks-dns-ekj1k627.portal.hcp.centralindia.azmk8s.io",
  "currentKubernetesVersion": "1.25.6",
  "disableLocalAccounts": false,
  "diskEncryptionSetId": null,
  "dnsPrefix": "dev-aks-dns",
  "enablePodSecurityPolicy": null,
  "enableRbac": true,
  "extendedLocation": null,
  "fqdn": "dev-aks-dns-ekj1k627.hcp.centralindia.azmk8s.io",
  "fqdnSubdomain": null,
  "httpProxyConfig": null,
  "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourcegroups/cicd/providers/Microsoft.ContainerService/managedClusters/dev-aks",
  "identity": {
    "principalId": "664ebd48-15f8-454f-bd92-48d075bf1f1c",
    "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "type": "SystemAssigned",
    "userAssignedIdentities": null
  },
  "identityProfile": {
    "kubeletidentity": {
      "clientId": "27f81ff9-adbf-4e63-ad7f-b9fa33756134",
      "objectId": "ab617406-d5be-4049-b654-c1badb78a59e",
      "resourceId": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourcegroups/MC_cicd_dev-aks_centralindia/providers/Microsoft.ManagedIdentity/userAssignedIdentities/dev-aks-agentpool"
    }
  },
  "kubernetesVersion": "1.25.6",
  "linuxProfile": null,
  "location": "centralindia",
  "maxAgentPools": 100,
  "name": "dev-aks",
  "networkProfile": {
    "dnsServiceIp": "10.0.0.10",
    "ipFamilies": [
      "IPv4"
    ],
    "loadBalancerProfile": {
      "allocatedOutboundPorts": null,
      "effectiveOutboundIPs": [
        {
          "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/MC_cicd_dev-aks_centralindia/providers/Microsoft.Network/publicIPAddresses/6c8f34ff-6a28-41ce-9e55-97f1ca1cc30c",
          "resourceGroup": "MC_cicd_dev-aks_centralindia"
        }
      ],
      "enableMultipleStandardLoadBalancers": null,
      "idleTimeoutInMinutes": null,
      "managedOutboundIPs": {
        "count": 1,
        "countIpv6": null
      },
      "outboundIPs": null,
      "outboundIpPrefixes": null
    },
    "loadBalancerSku": "Standard",
    "natGatewayProfile": null,
    "networkDataplane": null,
    "networkMode": null,
    "networkPlugin": "kubenet",
    "networkPluginMode": null,
    "networkPolicy": null,
    "outboundType": "loadBalancer",
    "podCidr": "10.244.0.0/16",
    "podCidrs": [
      "10.244.0.0/16"
    ],
    "serviceCidr": "10.0.0.0/16",
    "serviceCidrs": [
      "10.0.0.0/16"
    ]
  },
  "nodeResourceGroup": "MC_cicd_dev-aks_centralindia",
  "oidcIssuerProfile": {
    "enabled": false,
    "issuerUrl": null
  },
  "podIdentityProfile": null,
  "powerState": {
    "code": "Running"
  },
  "privateFqdn": null,
  "privateLinkResources": null,
  "provisioningState": "Succeeded",
  "publicNetworkAccess": null,
  "resourceGroup": "cicd",
  "securityProfile": {
    "azureKeyVaultKms": null,
    "defender": null,
    "imageCleaner": null,
    "workloadIdentity": null
  },
  "servicePrincipalProfile": {
    "clientId": "msi",
    "secret": null
  },
  "sku": {
    "name": "Base",
    "tier": "Free"
  },
  "storageProfile": {
    "blobCsiDriver": null,
    "diskCsiDriver": {
      "enabled": true
    },
    "fileCsiDriver": {
      "enabled": true
    },
    "snapshotController": {
      "enabled": true
    }
  },
  "supportPlan": "KubernetesOfficial",
  "systemData": null,
  "tags": null,
  "type": "Microsoft.ContainerService/ManagedClusters",
  "windowsProfile": null,
  "workloadAutoScalerProfile": {
    "keda": null
  }
}

</json>

</details>

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/6a945b0e-820b-4b22-bae6-d0ada6c2e20f)

Check for the loadbalancer service in azure portal

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/b7058839-9ae8-43ae-a5fd-2d09cb261266)


## 4. ACR for pushing docker images

- Create a ACR named  "cicddjangoimages" under newly created resource group cicd

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/44c0a0e1-c95e-4484-8db0-f35d15a02ae3)

It already has a repository named sampleweb app created from django-app dockerfile

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/ca0da6d6-12a5-4f8c-8eb6-725b14d748f0)


