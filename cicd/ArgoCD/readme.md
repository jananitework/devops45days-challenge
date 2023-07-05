# Argocd

3.2. Install Argo CD on the Kubernetes cluster.

3.3. Set up a Git repository for Argo CD to track the changes in the Helm charts and Kubernetes manifests.

3.4. Create a Helm chart for the Java application that includes the Kubernetes manifests and Helm values.

3.5 Add the Helm chart to the Git repository that Argo CD is tracking.


meera [ ~ ]$ kubectl create namespace argocd
namespace/argocd created
meera [ ~ ]$ helm repo add argo https://argoproj.github.io/argo-helm
"argo" already exists with the same configuration, skipping
meera [ ~ ]$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "argo" chart repository
Update Complete. ⎈Happy Helming!⎈
meera [ ~ ]$ helm install argocd argo/argo-cd --namespace argocd --create-namespace
NAME: argocd
LAST DEPLOYED: Wed Jul  5 14:55:12 2023
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


meera [ ~ ]$ kubectl get pods -n argocd
NAME                                                READY   STATUS    RESTARTS   AGE
argocd-application-controller-0                     1/1     Running   0          58s
argocd-applicationset-controller-7458b46d87-7b7hv   1/1     Running   0          58s
argocd-dex-server-5f94cc7b99-gbbj7                  1/1     Running   0          58s
argocd-notifications-controller-7bf448c96b-bh5gm    1/1     Running   0          58s
argocd-redis-7b5cf6cdc8-hqtmf                       1/1     Running   0          58s
argocd-repo-server-78cd99dbff-57cgn                 1/1     Running   0          58s
argocd-server-f65bdb94-xll9g                        1/1     Running   0          58s
meera [ ~ ]$ 
meera [ ~ ]$ kubectl get svc -n argocd
NAME                               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)             AGE
argocd-applicationset-controller   ClusterIP   10.0.26.164    <none>        7000/TCP            68s
argocd-dex-server                  ClusterIP   10.0.37.190    <none>        5556/TCP,5557/TCP   68s
argocd-redis                       ClusterIP   10.0.254.164   <none>        6379/TCP            68s
argocd-repo-server                 ClusterIP   10.0.154.197   <none>        8081/TCP            68s
argocd-server                      ClusterIP   10.0.191.231   <none>        80/TCP,443/TCP      68s


meera [ ~ ]$ kubectl expose deploy argocd-server -n argocd --port=8000 --name=argocd-lb --target-port=8000 --type=LoadBalancer
service/argocd-lb exposed


