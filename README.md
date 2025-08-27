# kind-demo

### Create cluster
Next command will create cluster with one node(control plane) and extra port mapping for NodePort and to simulate ingress behavior.
`kind create cluster --config kind.yaml`

### Building test flask Docker image  and load it to kind
- `docker build -t flask-app:0.1.0 .`
- `kind load docker-image flask-app:0.1.0`

### Deploy demo with NodePort
- `kubectl apply -f demo.yaml`
- `curl localhost:30080/test`
- `curl localhost:30080/hello`

### Ingress Demo
- Install ingress NGINX: `kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml`
- Wait untill ingress up and running
- Deploy ingress for already working <b>demo</b> service: `kubectl apply -f ingress-demo.yaml`
- `curl localhost/test`
- `curl localhost/hello`

### ARGO CD
1. kubectl create namespace argocd
2. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
3. kubectl apply -f helm_application.yaml
4. kubectl port-forward -n argocd svc/argocd-server 8080:80

### Prometheus Stack
1. helm upgrade --install prometheus prometheus-community/kube-prometheus-stack --version 77.0.2 --namespace monitoring --create-namespace -f prometheus/values.yaml
2. kubectl port-forward -n monitoring   svc/prometheus-kube-prometheus-prometheus 9090:9090 for prometheus
3. kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80 for grafana

### Links:
- https://kind.sigs.k8s.io/
