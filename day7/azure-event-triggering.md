## 1. Storage Account

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day7> az storage account create -n eventtriggersa -g event-trigger -l "central india" --sku Standard_LRS ```

<details>
 
```
The public access to all blobs or containers in the storage account will be disallowed by default in the future, which means default value for --allow-blob-public-access is still null but will be equivalent to false.
{
  "accessTier": "Hot",
  "allowBlobPublicAccess": true,
  "allowCrossTenantReplication": null,
  "allowSharedKeyAccess": null,
  "allowedCopyScope": null,
  "azureFilesIdentityBasedAuthentication": null,
  "blobRestoreStatus": null,
  "creationTime": "2023-06-20T09:06:53.311009+00:00",
  "customDomain": null,
  "defaultToOAuthAuthentication": null,
  "dnsEndpointType": null,
  "enableHttpsTrafficOnly": true,
  "enableNfsV3": null,
  "encryption": {
    "encryptionIdentity": null,
    "keySource": "Microsoft.Storage",
    "keyVaultProperties": null,
    "requireInfrastructureEncryption": null,
    "services": {
      "blob": {
        "enabled": true,
        "keyType": "Account",
        "lastEnabledTime": "2023-06-20T09:06:53.389145+00:00"
      },
      "file": {
        "enabled": true,
        "keyType": "Account",
        "lastEnabledTime": "2023-06-20T09:06:53.389145+00:00"
      },
      "queue": null,
      "table": null
    }
  },
  "extendedLocation": null,
  "failoverInProgress": null,
  "geoReplicationStats": null,
  "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/event-trigger/providers/Microsoft.Storage/storageAccounts/eventtriggersa",
  "identity": null,
  "immutableStorageWithVersioning": null,
  "isHnsEnabled": null,
  "isLocalUserEnabled": null,
  "isSftpEnabled": null,
  "keyCreationTime": {
    "key1": "2023-06-20T09:06:53.389145+00:00",
    "key2": "2023-06-20T09:06:53.389145+00:00"
  },
  "keyPolicy": null,
  "kind": "StorageV2",
  "largeFileSharesState": null,
  "lastGeoFailoverTime": null,
  "location": "centralindia",
  "minimumTlsVersion": "TLS1_0",
  "name": "eventtriggersa",
  "networkRuleSet": {
    "bypass": "AzureServices",
    "defaultAction": "Allow",
    "ipRules": [],
    "resourceAccessRules": null,
    "virtualNetworkRules": []
  },
  "primaryEndpoints": {
    "blob": "https://eventtriggersa.blob.core.windows.net/",
    "dfs": "https://eventtriggersa.dfs.core.windows.net/",
    "file": "https://eventtriggersa.file.core.windows.net/",
    "internetEndpoints": null,
    "microsoftEndpoints": null,
    "queue": "https://eventtriggersa.queue.core.windows.net/",
    "table": "https://eventtriggersa.table.core.windows.net/",
    "web": "https://eventtriggersa.z29.web.core.windows.net/"
  },
  "primaryLocation": "centralindia",
  "privateEndpointConnections": [],
  "provisioningState": "Succeeded",
  "publicNetworkAccess": null,
  "resourceGroup": "event-trigger",
  "routingPreference": null,
  "sasPolicy": null,
  "secondaryEndpoints": null,
  "secondaryLocation": null,
  "sku": {
    "name": "Standard_LRS",
    "tier": "Standard"
  },
  "statusOfPrimary": "available",
  "statusOfSecondary": null,
  "storageAccountSkuConversionStatus": null,
  "tags": {},
  "type": "Microsoft.Storage/storageAccounts"
}
  
```
  
</details>

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day7> az storage container create --name sample-cont --account-name eventtriggersa ```

<details>

```
There are no credentials provided in your command and environment, we will query for account key for your storage account.
It is recommended to provide --connection-string, --account-key or --sas-token in your command as credentials.

You also can add `--auth-mode login` in your command to use Azure Active Directory (Azure AD) for authorization if your login account is assigned required RBAC roles.
For more information about RBAC roles in storage, visit https://docs.microsoft.com/azure/storage/common/storage-auth-aad-rbac-cli.

In addition, setting the corresponding environment variables can avoid inputting credentials in your command. Please use --help to get more information about environment variable usage.
{
  "created": true
}

```
</details>

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/aef515d4-9548-4872-8878-179ee03ae34f)


## 2. Azure Service Bus

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day7> az servicebus namespace create --resource-group event-trigger --name eventtriggerns --location "central india" ```

<details>
  
```
{
  "createdAt": "2023-06-20T09:16:49.67Z",
  "disableLocalAuth": false,
  "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/event-trigger/providers/Microsoft.ServiceBus/namespaces/eventtriggerns",
  "location": "Central India",
  "metricId": "f9182f0c-787c-49f3-b5e0-dda139de3996:eventtriggerns",
  "minimumTlsVersion": "1.2",
  "name": "eventtriggerns",
  "premiumMessagingPartitions": 0,
  "provisioningState": "Succeeded",
  "publicNetworkAccess": "Enabled",
  "resourceGroup": "event-trigger",
  "serviceBusEndpoint": "https://eventtriggerns.servicebus.windows.net:443/",
  "sku": {
    "name": "Standard",
    "tier": "Standard"
  },
  "status": "Active",
  "tags": {},
  "type": "Microsoft.ServiceBus/Namespaces",
  "updatedAt": "2023-06-20T09:17:34.553Z",
  "zoneRedundant": false
}
```
  
</details>

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day7> az servicebus topic create --resource-group event-trigger --namespace-name eventtriggerns --name event-topic1 ```

<details>

```
{
  "accessedAt": "0001-01-01T00:00:00",
  "autoDeleteOnIdle": "P10675199DT2H48M5.4775807S",
  "countDetails": {
    "activeMessageCount": 0,
    "deadLetterMessageCount": 0,
    "scheduledMessageCount": 0,
    "transferDeadLetterMessageCount": 0,
    "transferMessageCount": 0
  },
  "createdAt": "2023-06-20T09:20:33.997Z",
  "defaultMessageTimeToLive": "P10675199DT2H48M5.4775807S",
  "duplicateDetectionHistoryTimeWindow": "PT10M",
  "enableBatchedOperations": true,
  "enableExpress": false,
  "enablePartitioning": false,
  "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/event-trigger/providers/Microsoft.ServiceBus/namespaces/eventtriggerns/topics/event-topic1",
  "location": "centralindia",
  "maxMessageSizeInKilobytes": 256,
  "maxSizeInMegabytes": 1024,
  "name": "event-topic1",
  "requiresDuplicateDetection": false,
  "resourceGroup": "event-trigger",
  "sizeInBytes": 0,
  "status": "Active",
  "subscriptionCount": 0,
  "supportOrdering": true,
  "type": "Microsoft.ServiceBus/namespaces/topics",
  "updatedAt": "2023-06-20T09:20:34.077Z"
}
```
</details>

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/6ed4dbd5-eee0-4aa9-95af-791a8741a3d9)



## 3. Azure Function 


``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day7> az functionapp create --name trigger-blob-upload --storage-account eventtriggersa --consumption-plan-location "centralindia" --resource-group event-trigger --os-type Linux --runtime python --runtime-version 3.10  --functions-version 4 ```

<details>
  
```
Your Linux function app 'trigger-blob-upload', that uses a consumption plan has been successfully created but is not active until content is published using Azure Portal or the Functions Core Tools.
Application Insights "trigger-blob-upload" was created for this Function App. You can visit https://portal.azure.com/#resource/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/event-trigger/providers/microsoft.insights/components/trigger-blob-upload/overview to view your Application Insights component
{
  "availabilityState": "Normal",
  "clientAffinityEnabled": false,
  "clientCertEnabled": false,
  "clientCertExclusionPaths": null,
  "clientCertMode": "Required",
  "cloningInfo": null,
  "containerSize": 0,
  "customDomainVerificationId": "4DDC6F7B26722D45A0A5AC65A82ACF7F0E83AD8D364097913D39A376A08AE384",
  "dailyMemoryTimeQuota": 0,
  "defaultHostName": "trigger-blob-upload.azurewebsites.net",
  "enabled": true,
  "enabledHostNames": [
    "trigger-blob-upload.azurewebsites.net",
    "trigger-blob-upload.scm.azurewebsites.net"
  ],
  "extendedLocation": null,
  "hostNameSslStates": [
    {
      "certificateResourceId": null,
      "hostType": "Standard",
      "ipBasedSslResult": null,
      "ipBasedSslState": "NotConfigured",
      "name": "trigger-blob-upload.azurewebsites.net",
      "sslState": "Disabled",
      "thumbprint": null,
      "toUpdate": null,
      "toUpdateIpBasedSsl": null,
      "virtualIp": null
    },
    {
      "certificateResourceId": null,
      "hostType": "Repository",
      "ipBasedSslResult": null,
      "ipBasedSslState": "NotConfigured",
      "name": "trigger-blob-upload.scm.azurewebsites.net",
      "sslState": "Disabled",
      "thumbprint": null,
      "toUpdate": null,
      "toUpdateIpBasedSsl": null,
      "virtualIp": null
    }
  ],
  "hostNames": [
    "trigger-blob-upload.azurewebsites.net"
  ],
  "hostNamesDisabled": false,
  "hostingEnvironmentProfile": null,
  "httpsOnly": false,
  "hyperV": false,
  "id": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/event-trigger/providers/Microsoft.Web/sites/trigger-blob-upload",
  "identity": null,
  "inProgressOperationId": null,
  "isDefaultContainer": null,
  "isXenon": false,
  "keyVaultReferenceIdentity": "SystemAssigned",
  "kind": "functionapp,linux",
  "lastModifiedTimeUtc": "2023-06-20T09:36:39.940000",
  "location": "centralindia",
  "maxNumberOfWorkers": null,
  "name": "trigger-blob-upload",
  "outboundIpAddresses": "52.172.195.80,52.172.197.124,52.172.204.47,52.172.198.32,52.172.208.112,52.172.195.80",
  "possibleOutboundIpAddresses": "52.172.195.80,52.172.197.124,52.172.204.47,52.172.198.32,52.172.208.112,13.71.21.87,13.71.30.16,52.172.195.80",
  "publicNetworkAccess": null,
  "redundancyMode": "None",
  "repositorySiteName": "trigger-blob-upload",
  "reserved": true,
  "resourceGroup": "event-trigger",
  "scmSiteAlsoStopped": false,
  "serverFarmId": "/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/event-trigger/providers/Microsoft.Web/serverfarms/CentralIndiaLinuxDynamicPlan",
  "siteConfig": {
    "acrUseManagedIdentityCreds": false,
    "acrUserManagedIdentityId": null,
    "alwaysOn": false,
    "antivirusScanEnabled": null,
    "apiDefinition": null,
    "apiManagementConfig": null,
    "appCommandLine": null,
    "appSettings": null,
    "autoHealEnabled": null,
    "autoHealRules": null,
    "autoSwapSlotName": null,
    "azureMonitorLogCategories": null,
    "azureStorageAccounts": null,
    "connectionStrings": null,
    "cors": null,
    "customAppPoolIdentityAdminState": null,
    "customAppPoolIdentityTenantState": null,
    "defaultDocuments": null,
    "detailedErrorLoggingEnabled": null,
    "documentRoot": null,
    "elasticWebAppScaleLimit": null,
    "experiments": null,
    "fileChangeAuditEnabled": null,
    "ftpsState": null,
    "functionAppScaleLimit": 0,
    "functionsRuntimeScaleMonitoringEnabled": null,
    "handlerMappings": null,
    "healthCheckPath": null,
    "http20Enabled": false,
    "http20ProxyFlag": null,
    "httpLoggingEnabled": null,
    "ipSecurityRestrictions": [
      {
        "action": "Allow",
        "description": "Allow all access",
        "headers": null,
        "ipAddress": "Any",
        "name": "Allow all",
        "priority": 2147483647,
        "subnetMask": null,
        "subnetTrafficTag": null,
        "tag": null,
        "vnetSubnetResourceId": null,
        "vnetTrafficTag": null
      }
    ],
    "ipSecurityRestrictionsDefaultAction": null,
    "javaContainer": null,
    "javaContainerVersion": null,
    "javaVersion": null,
    "keyVaultReferenceIdentity": null,
    "limits": null,
    "linuxFxVersion": "",
    "loadBalancing": null,
    "localMySqlEnabled": null,
    "logsDirectorySizeLimit": null,
    "machineKey": null,
    "managedPipelineMode": null,
    "managedServiceIdentityId": null,
    "metadata": null,
    "minTlsCipherSuite": null,
    "minTlsVersion": null,
    "minimumElasticInstanceCount": 0,
    "netFrameworkVersion": null,
    "nodeVersion": null,
    "numberOfWorkers": 1,
    "phpVersion": null,
    "powerShellVersion": null,
    "preWarmedInstanceCount": null,
    "publicNetworkAccess": null,
    "publishingPassword": null,
    "publishingUsername": null,
    "push": null,
    "pythonVersion": null,
    "remoteDebuggingEnabled": null,
    "remoteDebuggingVersion": null,
    "requestTracingEnabled": null,
    "requestTracingExpirationTime": null,
    "routingRules": null,
    "runtimeADUser": null,
    "runtimeADUserPassword": null,
    "scmIpSecurityRestrictions": [
      {
        "action": "Allow",
        "description": "Allow all access",
        "headers": null,
        "ipAddress": "Any",
        "name": "Allow all",
        "priority": 2147483647,
        "subnetMask": null,
        "subnetTrafficTag": null,
        "tag": null,
        "vnetSubnetResourceId": null,
        "vnetTrafficTag": null
      }
    ],
    "scmIpSecurityRestrictionsDefaultAction": null,
    "scmIpSecurityRestrictionsUseMain": null,
    "scmMinTlsVersion": null,
    "scmType": null,
    "sitePort": null,
    "storageType": null,
    "supportedTlsCipherSuites": null,
    "tracingOptions": null,
    "use32BitWorkerProcess": null,
    "virtualApplications": null,
    "vnetName": null,
    "vnetPrivatePortsCount": null,
    "vnetRouteAllEnabled": null,
    "webSocketsEnabled": null,
    "websiteTimeZone": null,
    "winAuthAdminState": null,
    "winAuthTenantState": null,
    "windowsConfiguredStacks": null,
    "windowsFxVersion": null,
    "xManagedServiceIdentityId": null
  },
  "slotSwapStatus": null,
  "state": "Running",
  "storageAccountRequired": false,
  "suspendedTill": null,
  "tags": null,
  "targetSwapSlot": null,
  "trafficManagerHostNames": null,
  "type": "Microsoft.Web/sites",
  "usageState": "Normal",
  "virtualNetworkSubnetId": null,
  "vnetContentShareEnabled": false,
  "vnetImagePullEnabled": false,
  "vnetRouteAllEnabled": false
}
```
</details>

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/4f17d94b-0f7c-4484-992e-872dfabccccd)

## 4.Deploy Azure functions using VS code

### Prerequisities 
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/7a31a0fd-c5bb-425d-a941-f5788d5d6674)


<details>
<summary> Deploy logs in VS code </summary>

```
3:14:52 PM trigger-blob-upload: Starting deployment...
3:14:52 PM trigger-blob-upload: Creating zip package...
3:15:06 PM trigger-blob-upload: Zip package size: 42.5 MB
3:15:10 PM trigger-blob-upload: Fetching changes.
3:15:11 PM trigger-blob-upload: Cleaning up temp folders from previous zip deployments and extracting pushed zip file /tmp/zipdeploy/cf15d156-4bc2-4bcd-bbcf-8f0048c7628a.zip (40.57 MB) to /tmp/zipdeploy/extracted
3:15:14 PM trigger-blob-upload: Updating submodules.
3:15:15 PM trigger-blob-upload: Preparing deployment for commit id '9551166c-3'.
3:15:15 PM trigger-blob-upload: PreDeployment: context.CleanOutputPath False
3:15:15 PM trigger-blob-upload: PreDeployment: context.OutputPath /home/site/wwwroot
3:15:15 PM trigger-blob-upload: Repository path is /tmp/zipdeploy/extracted
3:15:15 PM trigger-blob-upload: Running oryx build...
3:15:15 PM trigger-blob-upload: Command: oryx build /tmp/zipdeploy/extracted -o /home/site/wwwroot --platform python --platform-version 3.10.4 -p packagedir=.python_packages/lib/site-packages
3:15:16 PM trigger-blob-upload: Operation performed by Microsoft Oryx, https://github.com/Microsoft/Oryx
3:15:16 PM trigger-blob-upload: You can report issues at https://github.com/Microsoft/Oryx/issues
3:15:16 PM trigger-blob-upload: Oryx Version: 0.2.20230210.1, Commit: a49c8f6b8abbe95b4356552c4c884dea7fd0d86e, ReleaseTagName: 20230210.1
3:15:16 PM trigger-blob-upload: Build Operation ID: 21961dbba191414b
3:15:16 PM trigger-blob-upload: Repository Commit : 9551166c-30fa-496f-bda4-2bada42189ac
3:15:16 PM trigger-blob-upload: OS Type           : bullseye
3:15:16 PM trigger-blob-upload: Image Type        : githubactions
3:15:16 PM trigger-blob-upload: Detecting platforms...
3:15:19 PM trigger-blob-upload: Detected following platforms:
3:15:19 PM trigger-blob-upload:   python: 3.10.4
3:15:19 PM trigger-blob-upload: Version '3.10.4' of platform 'python' is not installed. Generating script to install it...
3:15:20 PM trigger-blob-upload: Source directory     : /tmp/zipdeploy/extracted
3:15:20 PM trigger-blob-upload: Destination directory: /home/site/wwwroot
3:15:20 PM trigger-blob-upload: Downloading and extracting 'python' version '3.10.4' to '/tmp/oryx/platforms/python/3.10.4'...
3:15:20 PM trigger-blob-upload: Detected image debian flavor: bullseye.
3:15:21 PM trigger-blob-upload: Downloaded in 1 sec(s).
3:15:21 PM trigger-blob-upload: Verifying checksum...
3:15:21 PM trigger-blob-upload: Extracting contents...
3:15:25 PM trigger-blob-upload: performing sha512 checksum for: python...
3:15:25 PM trigger-blob-upload: Done in 5 sec(s).
3:15:26 PM trigger-blob-upload: image detector file exists, platform is python..
3:15:26 PM trigger-blob-upload: OS detector file exists, OS is bullseye..
3:15:26 PM trigger-blob-upload: Python Version: /tmp/oryx/platforms/python/3.10.4/bin/python3.10
3:15:26 PM trigger-blob-upload: Creating directory for command manifest file if it does not exist
3:15:26 PM trigger-blob-upload: Removing existing manifest file
3:15:26 PM trigger-blob-upload: Running pip install...
3:15:27 PM trigger-blob-upload: Done in 2 sec(s).
3:15:27 PM trigger-blob-upload: [09:45:26+0000] Collecting azure-functions
3:15:27 PM trigger-blob-upload: [09:45:26+0000]   Downloading azure_functions-1.15.0-py3-none-any.whl (165 kB)
3:15:27 PM trigger-blob-upload: [09:45:27+0000] Installing collected packages: azure-functions
3:15:27 PM trigger-blob-upload: [09:45:27+0000] Successfully installed azure-functions-1.15.0
3:15:27 PM trigger-blob-upload: WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
3:15:27 PM trigger-blob-upload: WARNING: You are using pip version 21.2.4; however, version 23.1.2 is available.
3:15:27 PM trigger-blob-upload: You should consider upgrading via the '/tmp/oryx/platforms/python/3.10.4/bin/python3.10 -m pip install --upgrade pip' command.
3:15:27 PM trigger-blob-upload: Not a vso image, so not writing build commands
3:15:27 PM trigger-blob-upload: Preparing output...
3:15:27 PM trigger-blob-upload: Copying files to destination directory '/home/site/wwwroot'...
3:15:28 PM trigger-blob-upload: Done in 1 sec(s).
3:15:28 PM trigger-blob-upload: Removing existing manifest file
3:15:28 PM trigger-blob-upload: Creating a manifest file...
3:15:28 PM trigger-blob-upload: Manifest file created.
3:15:28 PM trigger-blob-upload: Copying .ostype to manifest output directory.
3:15:28 PM trigger-blob-upload: Done in 8 sec(s).
3:15:31 PM trigger-blob-upload: Running post deployment command(s)...
3:15:31 PM trigger-blob-upload: Generating summary of Oryx build
3:15:31 PM trigger-blob-upload: Deployment Log file does not exist in /tmp/oryx-build.log
3:15:31 PM trigger-blob-upload: The logfile at /tmp/oryx-build.log is empty. Unable to fetch the summary of build
3:15:31 PM trigger-blob-upload: Triggering recycle (preview mode disabled).
3:15:31 PM trigger-blob-upload: Linux Consumption plan has a 1.5 GB memory limit on a remote build container.
3:15:31 PM trigger-blob-upload: To check our service limit, please visit https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale#service-limits
3:15:31 PM trigger-blob-upload: Writing the artifacts to a squashfs file
3:15:45 PM: Error: request to https://trigger-blob-upload.scm.azurewebsites.net/api/deployments/latest?deployer=ms-azuretools-vscode&time=2023-06-20_09-45-10Z failed, reason: getaddrinfo ENOTFOUND trigger-blob-upload.scm.azurewebsites.net
3:20:21 PM trigger-blob-upload: Starting deployment...
3:20:21 PM trigger-blob-upload: Creating zip package...
3:20:37 PM trigger-blob-upload: Zip package size: 42.5 MB
3:20:38 PM trigger-blob-upload: Fetching changes.
3:20:39 PM trigger-blob-upload: Cleaning up temp folders from previous zip deployments and extracting pushed zip file /tmp/zipdeploy/ba3660e5-c9f5-4a9c-a6ee-52d8e2fbd7e9.zip (40.57 MB) to /tmp/zipdeploy/extracted
3:20:43 PM trigger-blob-upload: Updating submodules.
3:20:44 PM trigger-blob-upload: Preparing deployment for commit id '0d311806-5'.
3:20:44 PM trigger-blob-upload: PreDeployment: context.CleanOutputPath False
3:20:44 PM trigger-blob-upload: PreDeployment: context.OutputPath /home/site/wwwroot
3:20:44 PM trigger-blob-upload: Repository path is /tmp/zipdeploy/extracted
3:20:44 PM trigger-blob-upload: Running oryx build...
3:20:44 PM trigger-blob-upload: Command: oryx build /tmp/zipdeploy/extracted -o /home/site/wwwroot --platform python --platform-version 3.10.4 -p packagedir=.python_packages/lib/site-packages
3:20:45 PM trigger-blob-upload: Operation performed by Microsoft Oryx, https://github.com/Microsoft/Oryx
3:20:45 PM trigger-blob-upload: You can report issues at https://github.com/Microsoft/Oryx/issues
3:20:45 PM trigger-blob-upload: Oryx Version: 0.2.20230210.1, Commit: a49c8f6b8abbe95b4356552c4c884dea7fd0d86e, ReleaseTagName: 20230210.1
3:20:45 PM trigger-blob-upload: Build Operation ID: c870dd9e216f1040
3:20:45 PM trigger-blob-upload: Repository Commit : 0d311806-5ca3-4619-845d-6532454c526b
3:20:45 PM trigger-blob-upload: OS Type           : bullseye
3:20:45 PM trigger-blob-upload: Image Type        : githubactions
3:20:45 PM trigger-blob-upload: Detecting platforms...
3:20:48 PM trigger-blob-upload: Detected following platforms:
3:20:48 PM trigger-blob-upload:   python: 3.10.4
3:20:49 PM trigger-blob-upload: Version '3.10.4' of platform 'python' is not installed. Generating script to install it...
3:20:49 PM trigger-blob-upload: Source directory     : /tmp/zipdeploy/extracted
3:20:49 PM trigger-blob-upload: Destination directory: /home/site/wwwroot
3:20:49 PM trigger-blob-upload: Downloading and extracting 'python' version '3.10.4' to '/tmp/oryx/platforms/python/3.10.4'...
3:20:49 PM trigger-blob-upload: Detected image debian flavor: bullseye.
3:20:50 PM trigger-blob-upload: Downloaded in 1 sec(s).
3:20:50 PM trigger-blob-upload: Verifying checksum...
3:20:50 PM trigger-blob-upload: Extracting contents...
3:20:54 PM trigger-blob-upload: performing sha512 checksum for: python...
3:20:55 PM trigger-blob-upload: Done in 6 sec(s).
3:20:55 PM trigger-blob-upload: image detector file exists, platform is python..
3:20:55 PM trigger-blob-upload: OS detector file exists, OS is bullseye..
3:20:56 PM trigger-blob-upload: Python Version: /tmp/oryx/platforms/python/3.10.4/bin/python3.10
3:20:56 PM trigger-blob-upload: Creating directory for command manifest file if it does not exist
3:20:56 PM trigger-blob-upload: Removing existing manifest file
3:20:56 PM trigger-blob-upload: Running pip install...
3:20:57 PM trigger-blob-upload: Done in 2 sec(s).
3:20:57 PM trigger-blob-upload: [09:50:56+0000] Collecting azure-functions
3:20:57 PM trigger-blob-upload: [09:50:56+0000]   Downloading azure_functions-1.15.0-py3-none-any.whl (165 kB)
3:20:57 PM trigger-blob-upload: [09:50:56+0000] Installing collected packages: azure-functions
3:20:57 PM trigger-blob-upload: [09:50:57+0000] Successfully installed azure-functions-1.15.0
3:20:57 PM trigger-blob-upload: WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
3:20:57 PM trigger-blob-upload: WARNING: You are using pip version 21.2.4; however, version 23.1.2 is available.
3:20:57 PM trigger-blob-upload: You should consider upgrading via the '/tmp/oryx/platforms/python/3.10.4/bin/python3.10 -m pip install --upgrade pip' command.
3:20:57 PM trigger-blob-upload: Not a vso image, so not writing build commands
3:20:57 PM trigger-blob-upload: Preparing output...
3:20:57 PM trigger-blob-upload: Copying files to destination directory '/home/site/wwwroot'...
3:20:58 PM trigger-blob-upload: Done in 1 sec(s).
3:20:58 PM trigger-blob-upload: Removing existing manifest file
3:20:58 PM trigger-blob-upload: Creating a manifest file...
3:20:58 PM trigger-blob-upload: Manifest file created.
3:20:58 PM trigger-blob-upload: Copying .ostype to manifest output directory.
3:20:58 PM trigger-blob-upload: Done in 9 sec(s).
3:21:01 PM trigger-blob-upload: Running post deployment command(s)...
3:21:01 PM trigger-blob-upload: Generating summary of Oryx build
3:21:01 PM trigger-blob-upload: Deployment Log file does not exist in /tmp/oryx-build.log
3:21:01 PM trigger-blob-upload: The logfile at /tmp/oryx-build.log is empty. Unable to fetch the summary of build
3:21:01 PM trigger-blob-upload: Triggering recycle (preview mode disabled).
3:21:01 PM trigger-blob-upload: Linux Consumption plan has a 1.5 GB memory limit on a remote build container.
3:21:01 PM trigger-blob-upload: To check our service limit, please visit https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale#service-limits
3:21:01 PM trigger-blob-upload: Writing the artifacts to a squashfs file
3:21:13 PM trigger-blob-upload: Parallel mksquashfs: Using 1 processor
3:21:13 PM trigger-blob-upload: Creating 4.0 filesystem on /home/site/artifacts/functionappartifact.squashfs, block size 131072.
3:21:25 PM trigger-blob-upload: [==============================/                               ]  800/1607  49%
3:21:25 PM trigger-blob-upload: [=============================================================-] 1607/1607 100%
3:21:25 PM trigger-blob-upload: Exportable Squashfs 4.0 filesystem, gzip compressed, data block size 131072
3:21:25 PM trigger-blob-upload: 	compressed data, compressed metadata, compressed fragments,
3:21:25 PM trigger-blob-upload: 	compressed xattrs, compressed ids
3:21:25 PM trigger-blob-upload: 	duplicates are removed
3:21:25 PM trigger-blob-upload: Filesystem size 42779.10 Kbytes (41.78 Mbytes)
3:21:25 PM trigger-blob-upload: 	23.25% of uncompressed filesystem size (184026.20 Kbytes)
3:21:25 PM trigger-blob-upload: Inode table size 5969 bytes (5.83 Kbytes)
3:21:25 PM trigger-blob-upload: 	46.91% of uncompressed inode table size (12724 bytes)
3:21:25 PM trigger-blob-upload: Directory table size 2415 bytes (2.36 Kbytes)
3:21:25 PM trigger-blob-upload: 	40.76% of uncompressed directory table size (5925 bytes)
3:21:25 PM trigger-blob-upload: Number of duplicate files found 3
3:21:25 PM trigger-blob-upload: Number of inodes 219
3:21:25 PM trigger-blob-upload: Number of files 185
3:21:25 PM trigger-blob-upload: Number of fragments 13
3:21:25 PM trigger-blob-upload: Number of symbolic links  0
3:21:25 PM trigger-blob-upload: Number of device nodes 0
3:21:25 PM trigger-blob-upload: Number of fifo nodes 0
3:21:25 PM trigger-blob-upload: Number of socket nodes 0
3:21:25 PM trigger-blob-upload: Number of directories 34
3:21:25 PM trigger-blob-upload: Number of ids (unique uids + gids) 1
3:21:25 PM trigger-blob-upload: Number of uids 1
3:21:25 PM trigger-blob-upload: 	root (0)
3:21:25 PM trigger-blob-upload: Number of gids 1
3:21:25 PM trigger-blob-upload: 	root (0)
3:21:25 PM trigger-blob-upload: Creating placeholder blob for linux consumption function app...
3:21:25 PM trigger-blob-upload: SCM_RUN_FROM_PACKAGE placeholder blob scm-latest-trigger-blob-upload.zip located
3:21:25 PM trigger-blob-upload: Uploading built content /home/site/artifacts/functionappartifact.squashfs for linux consumption function app...
3:21:26 PM trigger-blob-upload: Resetting all workers for trigger-blob-upload.azurewebsites.net
3:21:26 PM trigger-blob-upload: Deployment successful. deployer = ms-azuretools-vscode deploymentPath = Functions App ZipDeploy. Extract zip. Remote build.
3:22:10 PM trigger-blob-upload: Syncing triggers...
3:22:11 PM trigger-blob-upload: Querying triggers...
3:22:12 PM trigger-blob-upload: No HTTP triggers found.
```  
</details>

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/a9a7527b-fadb-420a-bd43-76435852a3ce)


**NOTE : Dont forget to upload local settings from VS Code (View--> Command Palette --> Azure Functions: Upload Local settings)**

Check if the local settings is updated in remote

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/f27b684d-a472-4f3c-8c6e-b5a026156acf)

### Upload a new blob and check azure functions monitor

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/af52eeaa-ceab-43be-8906-a6ef5282b2b1)

# DEBUGGING ERRORS:

- If the deployment fails, please check "AzureWebJobsStorage" is set in local.settings.json
- If deployment fails, check if the storage account connection sting is correct.
- If Trigger fails for some package dependency, please update requirement.txt


