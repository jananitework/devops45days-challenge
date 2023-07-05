# Python django - Jenkins - Argocd - K8s

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/1ac155c6-fa30-4ba0-99b9-418811f2402f)


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

## 4. ACR for pushing docker images

- Create a ACR named  "cicddjangoimages" under newly created resource group cicd

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/dd655458-999f-40d6-aff4-82a5f8dfedff)
