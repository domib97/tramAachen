# Deployment Guide: tramOS Control Layer (K3s + ArgoCD)

This guide walks you through deploying the `control-layer-app` to your mixed-architecture cluster (CachyOS x86_64 Control Plane + Pi 5 ARM64 Workers).

## 1. Multi-Arch Build (Crucial for Pi 5)
Since your worker nodes are Raspberry Pi 5s (ARM64) and your control plane is CachyOS (x86_64), you should build a multi-arch image or specifically an `arm64` image.

```bash
# On your CachyOS machine, use Docker Buildx
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 \
  -t gitea.local/dom/tramaachen/control-layer:v1.2 \
  --push .
```

## 2. Push to Gitea
Ensure the code is committed to your Gitea repository so ArgoCD can see it:
```bash
git add .
git commit -m "feat: Add V2G Decision Engine and Simulation"
git push origin main
```

## 3. ArgoCD Deployment
Apply the ArgoCD application manifest:
```bash
kubectl apply -f tramAachen/tramOS/argo-app.yaml
```

## 4. Port-Forward for Testing
To run the `simulate_day.py` from your CachyOS desktop:
1. Find the service: `kubectl get svc -n tramos`
2. Forward the port:
   ```bash
   kubectl port-forward svc/control-layer-service 8000:80 -n tramos
   ```
3. Run the simulation script:
   ```bash
   python tramAachen/tramOS/control-layer-app/simulate_day.py
   ```

## 5. Monitoring (Observability)
Since you have **Loki** and **Kube-PrometheusStack** installed:

### Log Analysis (Loki):
Go to your Grafana instance and use Explore with this query:
`{app="control-layer", namespace="tramos"}`
*You will see every V2G decision being logged here in real-time.*

### Metrics (Prometheus):
Check the pod metrics to see the CPU/Memory usage on your Pi 5 nodes:
`container_memory_usage_bytes{pod=~"control-layer-app-.*"}`

---
**Learning Note (KCNA/LPIC-1):**
*   **LPIC-1**: Notice how the `Dockerfile` uses `python:slim` to reduce the image size, which is vital for the SD-card performance on your Pis.
*   **KCNA**: The `argo-app.yaml` uses a `finalizer`, ensuring that if you delete the app in ArgoCD, it cleanly removes all K8s resources from your Pi nodes.
