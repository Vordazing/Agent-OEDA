# LeCont ![](https://github.com/bastndev/GitHub_Emoji.gif/blob/main/assets/gif/vr%20(1).gif) 

<p align="left">
<a href="https://go.dev/doc/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/go-colored.svg" width="36" height="36" alt="Go" /></a><a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="36" height="36" alt="PostgreSQL" /></a><a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/docker-colored.svg" width="36" height="36" alt="Docker" /></a><a href="https://www.linux.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="36" height="36" alt="Linux" /></a>
</p>


This service will check the validity of the containers that are in the white list.

> - [The main features](#Основныечерты)
> - [Who is the service for](#Для_кого_продукт)
> - [The main functionality](#Основной_функционал_продукта)
> - [Instructions](#Инструкции)
> - [System requirements](#Системные_требования_продукта)

Russian version: https://github.com/Vordazing/LeCont/blob/main/README.md

<a name="Основныечерты"></a>
<h1>📌 The main features</h1>
<ul>
<li>🌈 Secure deployment</li>
<li> 🆎 Scalability</li>
<li> 💠 Transparency</li>
<li> 🤠 User uniqueness</li>
<li> 🕊 Lightness</li>
<li> ✍️ Customizability</li>
</ul>

<a name="Для_кого_продукт"></a>
<h1>🌐 Who is the service for</h1>
For professionals who regularly interact with various services in the Docker container environment.

<a name="Основной_функционал_продукта"></a>
<h1>🚀 The main functionality</h1>
<ul>
  <li>Container monitoring</li>
  <li>Adding a container to the white list</li>
  <li>Checking installed containers by white list</li>
  <li>Deleting containers that are not in the white list</li>
</ul>

<a name="Инструкции"></a>
<h1>📤 Instructions</h1>
<h2>♻ Installing and configuring services</h2></summary> 
<li>Agent - is a service that is responsible for preventing an unnecessary container from running on the production service if this container is not in the white list.</li>
<li>Server - runs the database where the white list will be stored; it is desirable to install the server folder on a separate server (where the white list will be stored).</li>
<li>Client - is an example scenario for using legitimate containers in a white list.</li>
  
<h2>💬 Installing and configuring an external server with a white list</h2></summary> 
<li>Run the command:</li>

```bash
git clone https://github.com/Vordazing/LeCont/tree/main
```
  
<li>Next, you need to raise the service using the command:</li>

```bash
docker-compose up
```

<a name="Системные_требования_продукта"></a>
<h1>🧩 System requirements</h1>
<ul>
  <li>Docker</li>
  <li>1 CPU</li>
  <li>25G hdd/ssd</li>
  <li>1 ОЗУ</li>
  <li>Linux</li>
</ul>


<h1 align="center">
  <a href="https://docusaurus.io">
    <img width="50%" src="https://github.com/Vordazing/Agent-OEDA/blob/main/lecont-logo.png" />
  </a>
</h1>
