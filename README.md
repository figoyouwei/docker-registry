# docker-registry
Explore docker registry with local checkin on 2024.12.23

## 1.Run registry
```
sudo docker-compose up -d
```

## 2.Verify the registry is running
```
curl http://localhost:5000/v2/_catalog
curl http://43.129.80.220:5000/v2/_catalog
curl https://www.docker-registry.asia/v2/_catalog
```

## 3.Pull,Tag and Push image to registry
```
docker pull hello-world
docker tag hello-world localhost:5000/hello-world
docker push localhost:5000/hello-world
```

## 4.Solve the https issue & pull image on local machine
```
docker pull www.docker-registry.asia/hello-world
```

## 5.Run the image on local macbook
```
docker run --platform linux/amd64 www.docker-registry.asia/hello-world
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
```
docker pull www.docker-registry.asia/nginx:latest --platform linux/amd64
docker tag www.docker-registry.asia/nginx:latest nginx1226:test
``` 