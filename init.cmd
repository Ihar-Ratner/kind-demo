kind create cluster --config kind.yaml
docker build -t flask-app:0.1.0 Docker/
kind load docker-image flask-app:0.1.0
kubectl apply -f demo.yaml
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
