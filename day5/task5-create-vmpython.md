#### 1. Do an az login

#### 2. Install the dependant packages in python

<details>
<summary> PIP install requirements </summary>

```

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> pip install -r .\task5-requirement.txt
Collecting azure-mgmt-resource (from -r .\task5-requirement.txt (line 1))
  Downloading azure_mgmt_resource-23.0.1-py3-none-any.whl (2.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 350.6 kB/s eta 0:00:00
Collecting azure-mgmt-compute (from -r .\task5-requirement.txt (line 2))
  Downloading azure_mgmt_compute-30.0.0-py3-none-any.whl (4.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 126.2 kB/s eta 0:00:00
Collecting azure-mgmt-network (from -r .\task5-requirement.txt (line 3))
  Downloading azure_mgmt_network-23.1.0-py3-none-any.whl (653 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 653.9/653.9 kB 107.3 kB/s eta 0:00:00
Collecting azure-identity (from -r .\task5-requirement.txt (line 4))
  Downloading azure_identity-1.13.0-py3-none-any.whl (151 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.6/151.6 kB 148.3 kB/s eta 0:00:00
Collecting isodate<1.0.0,>=0.6.1 (from azure-mgmt-resource->-r .\task5-requirement.txt (line 1))
  Downloading isodate-0.6.1-py2.py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.7/41.7 kB 183.0 kB/s eta 0:00:00
Collecting azure-common~=1.1 (from azure-mgmt-resource->-r .\task5-requirement.txt (line 1))
  Downloading azure_common-1.1.28-py2.py3-none-any.whl (14 kB)
Collecting azure-mgmt-core<2.0.0,>=1.3.2 (from azure-mgmt-resource->-r .\task5-requirement.txt (line 1))
  Downloading azure_mgmt_core-1.4.0-py3-none-any.whl (27 kB)
Collecting azure-core<2.0.0,>=1.11.0 (from azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading azure_core-1.27.1-py3-none-any.whl (174 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 174.5/174.5 kB 91.5 kB/s eta 0:00:00
Collecting cryptography>=2.5 (from azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading cryptography-41.0.1-cp37-abi3-win_amd64.whl (2.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 100.3 kB/s eta 0:00:00
Collecting msal<2.0.0,>=1.20.0 (from azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading msal-1.22.0-py2.py3-none-any.whl (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.0/90.0 kB 67.2 kB/s eta 0:00:00
Collecting msal-extensions<2.0.0,>=0.3.0 (from azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading msal_extensions-1.0.0-py2.py3-none-any.whl (19 kB)
Collecting six>=1.12.0 (from azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting requests>=2.18.4 (from azure-core<2.0.0,>=1.11.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 167.7 kB/s eta 0:00:00
Collecting typing-extensions>=4.3.0 (from azure-core<2.0.0,>=1.11.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading typing_extensions-4.6.3-py3-none-any.whl (31 kB)
Collecting cffi>=1.12 (from cryptography>=2.5->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading cffi-1.15.1-cp311-cp311-win_amd64.whl (179 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 179.0/179.0 kB 207.8 kB/s eta 0:00:00
Collecting PyJWT[crypto]<3,>=1.0.0 (from msal<2.0.0,>=1.20.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading PyJWT-2.7.0-py3-none-any.whl (22 kB)
Collecting portalocker<3,>=1.6 (from msal-extensions<2.0.0,>=0.3.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading portalocker-2.7.0-py2.py3-none-any.whl (15 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=2.5->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 kB 157.9 kB/s eta 0:00:00
Collecting pywin32>=226 (from portalocker<3,>=1.6->msal-extensions<2.0.0,>=0.3.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading pywin32-306-cp311-cp311-win_amd64.whl (9.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 107.0 kB/s eta 0:00:00
Collecting charset-normalizer<4,>=2 (from requests>=2.18.4->azure-core<2.0.0,>=1.11.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading charset_normalizer-3.1.0-cp311-cp311-win_amd64.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.7/96.7 kB 54.8 kB/s eta 0:00:00
Collecting idna<4,>=2.5 (from requests>=2.18.4->azure-core<2.0.0,>=1.11.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB 65.6 kB/s eta 0:00:00
Collecting urllib3<3,>=1.21.1 (from requests>=2.18.4->azure-core<2.0.0,>=1.11.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading urllib3-2.0.3-py3-none-any.whl (123 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.6/123.6 kB 108.3 kB/s eta 0:00:00
Collecting certifi>=2017.4.17 (from requests>=2.18.4->azure-core<2.0.0,>=1.11.0->azure-identity->-r .\task5-requirement.txt (line 4))
  Downloading certifi-2023.5.7-py3-none-any.whl (156 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.0/157.0 kB 86.2 kB/s eta 0:00:00
Installing collected packages: pywin32, azure-common, urllib3, typing-extensions, six, PyJWT, pycparser, portalocker, idna, charset-normalizer, certifi, requests, isodate, cffi, cryptography, azure-core, azure-mgmt-core, msal, azure-mgmt-resource, azure-mgmt-network, azure-mgmt-compute, msal-extensions, azure-identity
  WARNING: The script normalizer.exe is installed in 'C:\Users\91887\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyJWT-2.7.0 azure-common-1.1.28 azure-core-1.27.1 azure-identity-1.13.0 azure-mgmt-compute-30.0.0 azure-mgmt-core-1.4.0 azure-mgmt-network-23.1.0 azure-mgmt-resource-23.0.1 certifi-2023.5.7 cffi-1.15.1 charset-normalizer-3.1.0 cryptography-41.0.1 idna-3.4 isodate-0.6.1 msal-1.22.0 msal-extensions-1.0.0 portalocker-2.7.0 pycparser-2.21 pywin32-306 requests-2.31.0 six-1.16.0 typing-extensions-4.6.3 urllib3-2.0.3

```

</details>

#### 3. Set the AZURE SUBSCRIPTION ID env variable

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az account show --query id -o tsv
f9182f0c-787c-49f3-b5e0-dda139de3996
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> setx AZURE_SUBSCRIPTION_ID f9182f0c-787c-49f3-b5e0-dda139de3996

SUCCESS: Specified value was saved.
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> gci env: | where name -like 'AZURE*'

Name                           Value
----                           -----
AZURE_SUBSCRIPTION_ID          f9182f0c-787c-49f3-b5e0-dda139de3996
```

#### 4. Run the python script.

If running it for the first time, you might see some providers not registered , it gets registered automatically in runtime

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> python .\task5-provision-ubunutu.py
Provisioned resource group task5-rg in the centralindia region
Provisioned virtual network task5-vnet with address prefixes ['10.0.0.0/16']
Provisioned virtual subnet task5-subnet with address prefix 10.0.0.0/24
Provisioned public IP address task5-ip with address 20.219.5.85
Provisioned virtual machine task5-vm
```
