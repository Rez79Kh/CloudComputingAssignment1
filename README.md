# Docker and Containers Assignment

In This Assignment we have two containers as follows :

### Server
- Create a volume by name "servervol".
- The server container will mount "servervol" in "/serverdata".
- This container runs a server application which will create a file of size 1KB with random text data in "/serverdata" and then transfer the file to the client along with the checksum.
- The server application itself can be built using any language you are comfortable with. But, the container should include all the packages that are required to run your application. Choose your base image wisely and install only the necessary packages.
- The port on which the server runs must be specified as a command line argument when we run docker.

### Client
- Create a volume by name "clientvol".
- The client container will mount "clientvol" in "/clientdata".
- The client container runs an application that connects to the server, recieves the file that the server sends and saves it in "/clientdata".
- Verify that the file is received properly at the clientside by verifying the checksum.
- The client application again can be wriiten in any language that you are comfortable with, but the container should include all the necessary packages. Choose your base image wisely and install only necessary packages.

For see the question click [here.](https://www.cs.utexas.edu/~vijay/cs378-f17/projects/assignment2.htm)

## How to Run

```
$ docker compose up
```
