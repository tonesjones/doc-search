---
title: "Accessing the Connect UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/accessing-the-connect-ui.html"
content_id: "k~YhIHQhfqFRr5wLZqT0dw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:38.145401+00:00"
---

# Accessing the Connect UI

After the installation is complete, the UI will be accessible in one of two ways,
depending on how the ingress controller was deployed.

## Load balancer

To obtain the Coverity Connect UI IP address if the Ingress controller was deployed
using a service type of LoadBalancer:

1. If the Ingress controller was deployed using a service type of LoadBalancer
   (default), run the following command:

   ```
   kubectl get svc -n ${NS}
   ```

   You should see an output similar to:

   ```
   NAME                 TYPE          CLUSTER-IP      EXTERNAL-IP     PORT(S)                     AGE
   redis-headless       ClusterIP     None            <none>          6379/TCP                    4h38m
   postgres-hl          ClusterIP     None            <none>          5432/TCP                    4h38m
   redis-master         ClusterIP     10.43.133.109   <none>          6379/TCP                    4h38m
   minio                ClusterIP     10.43.36.215    <none>          9000/TCP,9001/TCP           4h38m
   postgres             ClusterIP     10.43.102.168   <none>          5432/TCP                    4h38m
   ingress-controller   LoadBalancer  10.43.231.233   172.25.102.142  80:30920/TCP,443:30337/TCP  4h38m
   cim-tools            ClusterIP     None            <none>          <none>                      4h37m
   cim                  ClusterIP     10.43.16.24     <none>          8080/TCP,8443/TCP           4h37m
   cache-service        ClusterIP     10.43.255.128   <none>          8443/TCP                    4h37m
   scan-service         ClusterIP     10.43.74.193    <none>          9999/TCP                    4h37m
   storage-service      ClusterIP     10.43.98.83     <none>          9999/TCP                    4h37m
   ```
2. Find the entry for the ingress controller, it is the only entry with an
   external IP. See highlighted row above.
3. Create a host entry for your coverity hostname. For example,
   `cnc.connect1.int` with the external IP address. For
   example, 172.25.102.142
4. Once that is done, you can open a web browser and go to
   `https://${COVERITY_HOST}`. For example,
   `https://cnc.connect1.int`.

   You should see the login screen.

## NodePort

If the installation was done using NodePort:

1. Run the following command:

   ```
   kubectl get svc -n ${NS}
   ```

   You should see an output similar to:

   ```
   NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP  PORT(S)                     AGE
   ingress-controller   NodePort    10.96.57.16    <none>       80:30080/TCP,443:30443/TCP  6m9s
   minio                ClusterIP   10.96.198.122  <none>       9000/TCP,9001/TCP           6m9s
   postgres             ClusterIP   10.96.47.174   <none>       5432/TCP                    6m9s
   postgres-hl          ClusterIP   None           <none>       5432/TCP                    6m9s
   redis-headless       ClusterIP   None           <none>       6379/TCP                    6m9s
   redis-master         ClusterIP   10.96.17.142   <none>       6379/TCP                    6m9s
   cim                  ClusterIP   10.96.211.139  <none>       8080/TCP,8443/TCP           5m11s
   cim-tools            ClusterIP   None           <none>       <none>                      5m11s
   cache-service        ClusterIP   10.96.62.41    <none>       8443/TCP                    5m11s
   scan-service         ClusterIP   10.96.56.204   <none>       9999/TCP                    5m11s
   storage-service      ClusterIP   10.96.121.31   <none>       9999/TCP                    5m11s
   ```
2. Find the entry for the ingress controller, it should be the only one with
   type NodePort. Under the Port(s) column you will see which ports are being
   used to service HTTPS traffic and HTTP traffic, in the above example HTTPS
   traffic is exposed on port 30443 and HTTP traffic is exposed on port
   30080.
3. Create a host entry for your coverity hostname. For example,
   `cnc.connect1.int` with the external IP address. For
   example, 127.0.0.1
4. Once that is done, you can open a web browser and go to
   `https://${COVERITY_HOST}`. For example,
   `https://cnc.connect1.int`.

   You should see the login screen.
