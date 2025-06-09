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

### Links:
- https://kind.sigs.k8s.io/
