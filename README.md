Docker command after building:

Assuming the Docker image is: `stlitsandbox:latest`

```
docker run --rm -d  -p 8080:8080/tcp stlitsandbox:latest
```

App can be accessed in: http://localhost:8080/
