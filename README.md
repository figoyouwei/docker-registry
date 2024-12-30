# docker-registry
Explore docker registry with local checkin on 2024.12.23

## 1.Run registry
```
sudo docker-compose up -d
```

## 2.Verify the registry is running
```
# locahost registry at port 5000
curl http://localhost:5000/v2/_catalog

# ip registry at port 5000
curl http://43.129.80.220:5000/v2/_catalog

# ip registry at port 80    
curl http://43.129.80.220/v2/_catalog

# domain registry
curl https://www.docker-registry.asia/v2/_catalog
```

## 3.Pull,Tag and Push image to registry from docker.io
```
docker pull hello-world
docker tag hello-world localhost:5000/hello-world
docker push localhost:5000/hello-world
```

## 4.Pull image on local machine
```
docker pull www.docker-registry.asia/nginx:latest
```

## 5.Run the image on local macbook
```
docker run --platform linux/amd64 www.docker-registry.asia/nginx:latest
```

## 6.Run the image on suaee
```
docker run www.docker-registry.asia/hello-world
```

## 7.Inspect the image
```
docker inspect nginx:latest | grep -i version
docker images | grep localhost
```

## 8.Repositories
```
storage/docker/registry/v2/repositories
``` 

## 9.Pull image from registry with a different name
- Docker requires ssl
```
docker pull www.docker-registry.asia/nginx:latest
``` 
- Pull with platform
```
docker pull www.docker-registry.asia/nginx:latest --platform linux/amd64
```
- Tag after pull
```
docker tag www.docker-registry.asia/nginx:latest nginx1226:test
```

## 10.Push Existing Image to Registry
```bash
# Tag the image with registry domain
docker tag <source-image>:<tag> www.docker-registry.asia/<image-name>:<tag>

# Push to registry
docker push www.docker-registry.asia/<image-name>:<tag>

# Example with TimescaleDB
docker tag timescale/timescaledb-ha:pg16 localhost:5000/timescaledb-ha:pg16
docker push localhost:5000/timescaledb-ha:pg16
```
