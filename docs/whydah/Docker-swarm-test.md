# Docker swarm test

Stigs doc for bruk av Docker swarm

- Henter ut <https://github.com/technolo-g/docker-swarm-demo> fordi det virker som at de bruker Ansible, Docker swarm og ser halv-sane ut
- Opprettet micro EC2 Ubuntu-linux burk på us-west-1.console.aws.amazon.com. ec2-54-183-185-75.us-west-1.compute.amazonaws.com Grunnen til Ubuntu er fordi Ansible-scriptene er laget for ubuntu og må omskrives hvis de skal gå mot RHEL/AWS-linux
- Lagt opp ny .pem nøkkel for å logge in på AWS på US-West
- Har endret ./hosts med amazon nøkkelen min og ip til ny AWS amazon burk

Docker swarm direkte på OS X og Ubuntuboks:  
Docker swarm moro

- Installert docker toolbox <https://www.docker.com/docker-toolbox>
- Start Docker quick start Terminal
- Kjører stegvis <https://docs.docker.com/swarm/install-w-machine/>
- Mitt token: 6059da2add25b208e6767561719644f3

Mine kommandoer:

- docker-machine create -d virtualbox --swarm --swarm-discovery token://6059da2add25b208e6767561719644f3 --swarm-master swarm-master
- docker-machine create -d virtualbox --swarm --swarm-discovery token://fe0cc96a72cf04dba8c1c4aa79536ec3 swarm-agent-01
- Status: docker-machine env swarm-master
- docker info

- På ekstern node: swarm join --discovery token://6059da2add25b208e6767561719644f3 --addr=10.0.40.195:2375
- swarm join --discovery-opt token://6059da2add25b208e6767561719644f3 --addr=10.0.40.195:2375

token2: 353b3db8760e9d0a07c7c2749fd84ab8

swarm join --advertise=localhost:2375 token://353b3db8760e9d0a07c7c2749fd84ab8

fra <https://docs.docker.com/swarm/install-manual/>  
docker pull swarm  
docker run --rm swarm create  
51e03f6e4eb9b81aae178668b606cc4a  
docker run -d swarm join --addr=localhost:2375 token://353b3db8760e9d0a07c7c2749fd84ab8 worker2  
docker run -d -p 2999:2375 swarm manage token://353b3db8760e9d0a07c7c2749fd84ab8  
docker run --rm swarm list token://353b3db8760e9d0a07c7c2749fd84ab8

docker -H tcp://<manager\_ip:manager\_port> info  
docker -H tcp://<manager\_ip:manager\_port> run ...  
docker -H tcp://<manager\_ip:manager\_port> ps  
docker -H tcp://<manager\_ip:manager\_port> logs ...

swarm manage --tlsverify --tlscacert=<CACERT> --tlscert=<CERT> --tlskey=<KEY> [...]

Docker på AWS Linux  
AWS key: d797c1bf3c26c0fd17b2e25b8cc78647

docker run -d bestn --addr=ec2-52-17-38-16.eu-west-1.compute.amazonaws.com:2375 token://d797c1bf3c26c0fd17b2e25b8cc78647

<http://devopscube.com/docker-tutorial-getting-started-with-docker-swarm/>

#Skaff Go og Swarm!  
export GOPATH=$HOME/go  
stiglau@dockeruntu:~/go$ export PATH=$HOME/go/bin:$PATH  
swarm join --advertise=52.17.38.16:2375 token://d797c1bf3c26c0fd17b2e25b8cc78647  
swarm manage -H tcp://localhost:2375 token://d797c1bf3c26c0fd17b2e25b8cc78647  
swarm list token://d797c1bf3c26c0fd17b2e25b8cc78647

Consul  
Setting up consul docker server: <https://hub.docker.com/r/progrium/consul/>

## Todo

Test this out: <http://blog.arungupta.me/docker-swarm-cluster-using-consul/>
