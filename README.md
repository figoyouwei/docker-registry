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
```

## 3.Pull,Tag and Push image to registry
```
docker pull hello-world
docker tag hello-world localhost:5000/hello-world
docker push localhost:5000/hello-world
```

## 4.Verify the image is pushed to registry
```
curl http://localhost:5000/v2/_catalog
```

## 5.Solve the https issue & pull image on local machine
```
docker pull docker-registry.asia/hello-world
```