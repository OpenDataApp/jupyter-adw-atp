# Jupyter-adw-atp-json Oracle On Docker

Jupyter lab environment ready to use with ADW-ATP-JSON

This container is ready to use jupyter notebooks with Autonomous Data Warehouse, Autnonomous Transaction Processing or Autonomous JSON.

## How to use

In command line you can put follow command:

```docker
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes pavelsjo/jupyter-adw-atp:1.0
```

# How to Oracle Registry?

Example using windows environment:

```docker
#AUTENTICATION
winpty docker login us-ashburn-1.ocir.io
oracleidentitycloudservice/you.user@domain.com
<your_pasword> #Auth token

#PUSH
docker tag pavelsjo/jupyter-adw-atp:1.0 us-ashburn-1.ocir.io/idmivk6wh2wj/orion/jupyter-adw-atp:latest
docker push us-ashburn-1.ocir.io/idmivk6wh2wj/orion/jupyter-adw-atp
```

## Temp references

- [ipython-sql](https://github.com/catherinedevlin/ipython-sql)
- [cx_oracle.md](https://gist.github.com/kimus/10012910)
- [Docker best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#exclude-with-dockerignore)
- [Docker for Data Science — A Step by Step Guide](https://godatadriven.com/blog/write-less-terrible-code-with-jupyter-notebook/)
- [How to Put Jupyter Notebooks in a Dockerfile](https://u.group/thinking/how-to-put-jupyter-notebooks-in-a-dockerfile/)
- [Write less terrible code with Jupyter Notebook](https://godatadriven.com/blog/write-less-terrible-code-with-jupyter-notebook/)
- [Pull an Image from Oracle Cloud Infrastructure Registry when Deploying a Load-Balanced Application to a Cluster](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-and-registry/index.html#CreateaSecretfortheTutorial)
