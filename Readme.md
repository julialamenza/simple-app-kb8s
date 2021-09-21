# Flask API dockerized


##### I use Kubectl and minikube for make this works

<br>
**Follow this guide if you dont have docker and kubernetes installed in your computer (Mac OS)**


<br>

#### Docker

```

brew install docker
```


**or**

```

Download Docker for mac from the url : https://download.docker.com/mac/stable/Docker.dmg
```


**check your docker version**

```
docker version
```


#### Kubernetes (Kubectl)

```
brew install kubectl
```


**or**


- Download the latest release:

```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
To download a specific version, replace the $(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt) portion of the command with the specific version.
```

```
For example, to download version v1.18.0 on macOS, type:

```

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/darwin/amd64/kubectl
```



- Make the kubectl binary executable.

```
chmod +x ./kubectl
```

- Move the binary in to your PATH.

```
sudo mv ./kubectl /usr/local/bin/kubectl
```



**check your kubectl version**

```
kubectl version --client
```



### Helm

```
brew install helm
```


**or**

```
Download your version - https://github.com/helm/helm/releases
```


- Unpack it

```
tar -zxvf helm-v3.0.0-linux-amd6
```


- Find the helm binary in the unpacked directory, and move it to its desired destination

```
mv linux-amd64/helm /usr/local/bin/helm
```

**check helm version**

```
helm version
```



### Start kubectl 

- Start Minikube and create a cluster:

```
minikube start
```

### clone this repository

```
git clone https://github.com/julialamenza/simple-app-kb8s
```
- go to the folder

```
cd simple-app-kb8s/
```

- to deploy de application you need to follow this order:

1- Namespace
2- ConfigMap
3- Deployment
4- Service
5-Ingress

or run

```
chmod +x deploy.sh
./deploy.sh
```
## Access application

you can acess the application checking your minikube ip

```
minikube ip
```
Curl in the app

```
curl <minikube-ip:80/>
```
Or add you ip in you /etc/hosts

```
sudo vim /etc/hosts

minikube-ip   app.ptova
```

```
curl app.prova
```
Remember your app route exist in ```/``` and ```/health```

## To deploy prometheus and grafana with helm

run these commands

```
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo add stable https://charts.helm.sh/stable
$ helm repo update
$ helm install prometheus prometheus-community/kube-prometheus-stack
$ kubectl port-forward deployment/prometheus-grafana 3000

```
 ## Login into grafana

**username:** admin
**password:** prom-operator


For more information check Kubernetes documentation -> https://kubernetes.io/docs/home/


TO DO:

- Deploy Kibana 
- Send logs to Kibana
