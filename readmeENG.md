# LeCont ![](https://github.com/bastndev/GitHub_Emoji.gif/blob/main/assets/gif/vr%20(1).gif) 

<p align="left">
<a href="https://go.dev/doc/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/go-colored.svg" width="36" height="36" alt="Go" /></a><a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="36" height="36" alt="PostgreSQL" /></a><a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/docker-colored.svg" width="36" height="36" alt="Docker" /></a><a href="https://www.linux.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="36" height="36" alt="Linux" /></a>
</p>


This service will check the validity of the containers that are in the white list.

> - [The main features](#Themainfeatures)
> - [Who is the service for](#Whoistheservicefor)
> - [The main functionality](#Themainfunctionality)
> - [Instructions](#Instructions)
> - [System requirements](#Systemrequirements)

<a name="Themainfeatures"></a>
<h1>📌 The main features</h1>
<ul>
<li>🌈 Secure deployment</li>
<li> 🆎 Scalability</li>
<li> 💠 Transparency</li>
<li> 🤠 User uniqueness</li>
<li> 🕊 Lightness</li>
<li> ✍️ Customizability</li>
</ul>

<a name="Whoistheservicefor"></a>
<h1>🌐 Who is the service for</h1>
For professionals who regularly interact with various services in the Docker container environment.

<a name="Themainfunctionality"></a>
<h1>🚀 The main functionality</h1>
<ul>
  <li>Container monitoring</li>
  <li>Adding legitimate containers to the white list</li>
  <li>Checking installed containers by white list</li>
  <li>Deleting containers that are not in the white list</li>
</ul>

<a name="Instructions"></a>
<h1> 📤 Instructions</h1>
<h2> ♻ Installing and configuring services</h2></summary>
<li>The agent is a server who responds that a small container has not been launched for the production of servers, that container is not in the white sheet.</li>
<li>Server - loads the database where the white sheet will be stored; it is desirable to install the server folder on a separate server (where the white sheet will be stored).</li>
<li>Client - the client required for exporting converged containers</li>

<h2>Preview in the pipeline</h2>

<h3>1. Add using GitLab</h3>

<li>Use digitized instructions for your operating system</li>
<li>Follow the instructions indicating the availability of your system</li>
<li>Edit the GitLab configuration file to create parameters, as URL and security</li>
<li>Reinstall GitLab to add changes</li>

<h3>2. Add GitLab Runner</h3>

<lithium>Installing Gitlab Runner: follow the official instructions for your operating system, which can be found on the Gitlab Runner installation page

`
https://docs.gitlab.com/runner/install/
`
<li>Sign the registration command after installation, specifying the URL and registration token, which can be obtained from the desktop project on GitLab:</li>

```
sudo gitlab-Runner registration
```

<h3>3. Add a Pipeline with a feed</h3>
Install in GitLab /Build/Pipeline Editor:

```
default:
image:
oeda services:
- oeda
before_script:
- information about the docker

variables:

DOCKER_TLS_CERTDIR: "/certificates"

build:
stage:
build script:
- docker pull nginx
security:
stage:
build script:
- oeda
```
<h3>4. Download and up the docker image of dind</h3>
<li>Download along the way:</li>

`
/LeCont/blob object/main/Dockerfile
`
<li>Up:</li>

```
build docker -f Dockerfile-find . -t oeda
```



<h2>Agent Installation</h2></short description>
<li> Download a folder from the command line along the path:</li>

`
/LeCont/tree/home/cmd/agent
`
<li> Download Dockerfile along the way:</li>

`
/LeCont/blob/main/Dockerfile
`
After downloading, you need to disable the docker-compose-agent.yaml and change the string - SERVER_IP=x.x.x.x, where x.x.x.x.x is your local ip address on which this server will be blocked</li>
<li> Fill out the form:</li>

```
docker compose -f docker-compose-agent.yaml up --build
```
<h2>Server installation</h2></summary>
<li> Download the folder from cmd along the path:</li>

`
/LeCount/tree/main/intermediate
`
<li> Download the intermediate folder along the path:</li>

`
/LeCont/tree/home/cmd/server
`

<li> Download Dockerfile along the way:</li>

`
/LeCont/blob/main/docker-compose.yaml
`
After downloading, you need to disable docker-compose-agent.yaml and change portals to those that are not available on your server</li>

```
ports:
- 8000:8000
```

```
ports:
- "26257:26257"
- "8080:8080"
```
<li> Add a comment:</li>

```
docker -up layout --build
```

<h2>Client registration</h2></short description>
<li> Download the folder from the command line along the path:</li>

`
/LeCont/tree/home/cmd/client
`
<li> Download Dockerfile along the way:</li>

`
/LeCont/blob/main/Dockerfile
`
<li> After downloading, you need to open the docker-compose client.yaml and change the string - SERVER_IP=x.x.x.x, where x.x.x.x.x is your local ip address on which this server will be blocked</li>
<li> Fill out the form:</li>

```
docker compose -f docker-compose-client.yaml up --build
```



<a name="Systemrequirements"></a>
<h1>🧩 System requirements</h1>
<ul>
  <li>Docker</li>
  <li>1 CPU</li>
  <li>25G hdd/ssd</li>
  <li>1 RAM</li>
  <li>Linux</li>
</ul>


<h1 align="center">
  <a href="https://docusaurus.io">
    <img width="50%" src="https://github.com/Vordazing/Agent-OEDA/blob/main/lecont-logo.png" />
  </a>
</h1>
