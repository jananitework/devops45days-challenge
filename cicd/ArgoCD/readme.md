# Argocd Installation

### Run the following command to add the ArgoCD Helm repository:

```
meera [ ~ ]$ helm repo add argo https://argoproj.github.io/argo-helm
"argo" already exists with the same configuration, skipping
```

### Create a namespace for ArgoCD:
```
meera [ ~ ]$ kubectl create namespace argocd
namespace/argocd created
```

### Install ArgoCD using Helm, specifying the release name and namespace:
```
meera [ ~ ]$ helm install argocd argo/argo-cd --namespace argocd --create-namespace
NAME: argocd
LAST DEPLOYED: Wed Jul  5 16:45:37 2023
NAMESPACE: argocd
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
In order to access the server UI you have the following options:

1. kubectl port-forward service/argocd-server -n argocd 8080:443

    and then open the browser on http://localhost:8080 and accept the certificate

2. enable ingress in the values file `server.ingress.enabled` and either
      - Add the annotation for ssl passthrough: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#option-1-ssl-passthrough
      - Set the `configs.params."server.insecure"` in the values file and terminate SSL at your ingress: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#option-2-multiple-ingress-objects-and-hosts


After reaching the UI the first time you can login with username: admin and the random password generated during the installation. You can find the password by running:

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

(You should delete the initial secret afterwards as suggested by the Getting Started Guide: https://argo-cd.readthedocs.io/en/stable/getting_started/#4-login-using-the-cli)
```

### Check the installed services and deployments

```
meera [ ~ ]$ kubectl get svc -n argocd
NAME                               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)             AGE
argocd-applicationset-controller   ClusterIP   10.0.184.30    <none>        7000/TCP            20s
argocd-dex-server                  ClusterIP   10.0.168.7     <none>        5556/TCP,5557/TCP   20s
argocd-redis                       ClusterIP   10.0.245.49    <none>        6379/TCP            20s
argocd-repo-server                 ClusterIP   10.0.14.169    <none>        8081/TCP            20s
argocd-server                      ClusterIP   10.0.235.142   <none>        80/TCP,443/TCP      20s

meera [ ~ ]$ kubectl get deploy -n argocd
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
argocd-applicationset-controller   1/1     1            1           87s
argocd-dex-server                  1/1     1            1           87s
argocd-notifications-controller    1/1     1            1           87s
argocd-redis                       1/1     1            1           87s
argocd-repo-server                 1/1     1            1           87s
argocd-server                      1/1     1            1           87s
```

### To access the argocd UI, expose the argocd-server deployment using loadbalancer service

```
meera [ ~ ]$ kubectl expose deploy argocd-server -n argocd --port=8080 --target-port=8080 --name=argo-lb --type=LoadBalancer
service/argo-lb exposed

meera [ ~ ]$ kubectl get svc -n argocd
NAME                               TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)             AGE
argo-lb                            LoadBalancer   10.0.136.92    20.219.180.65   8080:30524/TCP      13s
argocd-applicationset-controller   ClusterIP      10.0.184.30    <none>          7000/TCP            2m24s
argocd-dex-server                  ClusterIP      10.0.168.7     <none>          5556/TCP,5557/TCP   2m24s
argocd-redis                       ClusterIP      10.0.245.49    <none>          6379/TCP            2m24s
argocd-repo-server                 ClusterIP      10.0.14.169    <none>          8081/TCP            2m24s
argocd-server                      ClusterIP      10.0.235.142   <none>          80/TCP,443/TCP      2m24s
```
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/970d37a0-76f5-49da-a3a6-a99898cbd06f)

### Configure the git repo which contains the k8s manifests for deploying the django app

https://github.com/jananitework/devops45days-challenge/tree/main/cicd/ArgoCD/deployments

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/a5a8c46f-015f-44b2-b821-86c6b342b97e)


### Once pod is running,you should be able to see the django-app pod and service

```
meera [ ~ ]$ kubectl get pods -o wide
NAME         READY   STATUS    RESTARTS       AGE     IP            NODE                                NOMINATED NODE   READINESS GATES
django-app   1/1     Running   1 (3m8s ago)   7m50s   10.244.0.16   aks-agentpool-86582989-vmss000001   <none>           <none>
meera [ ~ ]$ kubectl get svc -o wide
NAME            TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)          AGE     SELECTOR
django-app-lb   LoadBalancer   10.0.221.232   20.244.57.226   8000:32564/TCP   7m54s   app=webapp
kubernetes      ClusterIP      10.0.0.1       <none>          443/TCP          3h      <none>
```

### Your app should be succesfully launched in browser
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/97edee3e-b27b-4430-a704-2a098cc16298)

