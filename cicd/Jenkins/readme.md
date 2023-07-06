# Jenkins pipeline configuration and github webhook configuration

## Step1. Install docker in jenkins vm and make sure the jenkins user has the permission for docker .

```
sudo apt update
sudo apt install docker.io

sudo su - 
usermod -aG docker jenkins
usermod -aG docker <jenkinsusername>
systemctl restart docker
```

## Step2. Grant permissions for jenkins user to enable pull and push to ACR

- Generate access keys in ACR

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/0c91215f-3f72-4008-94ee-b093d1e3dfd2)

- Login to jenkins vm and do docker login

```
jenkins@jenkins-vm:~/workspace/trial1/cicd/ArgoCD/deployments$ docker login cicddjangoimages.azurecr.io
Username: cicddjangoimages
Password:
WARNING! Your password will be stored unencrypted in /var/lib/jenkins/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Use the username and password as in Access keys section of ACR.

## Step3. Enable Webhooks in GitHub that has django-web-app

1. Go to the settings tab of github repo which has the django code. In our case its https://github.com/jananitework/devops45days-challenge.git.

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/82152524-f223-4a76-bb81-144bfa8daea3)

Make sure there is a green tick near the configured webhook.

2. Add the jenkins ssh keys to your github account for authentication purpose
3. Add the jenkins credentials as global credentials to check git repos. Manage Jenkins --> configure credentials.

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/51c37934-77c9-43ce-9364-64c3314e1de6)


## Step4. Write the jenkins declarative file with following stages

1. Checkout the source code of django-web-app for every new push/pr
2. Build the docker image with new tag (build number is the tag)
3. Push the artifacts to ACR
4. Checkout the repository which has the k8s manifests for deploying django-web-app
5. Update the image of the django-web-app with the latest image tag



