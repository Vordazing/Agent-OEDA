# LeCont ![](https://github.com/bastndev/GitHub_Emoji.gif/blob/main/assets/gif/vr%20(1).gif) 

<p align="left">
<a href="https://go.dev/doc/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/go-colored.svg" width="36" height="36" alt="Go" /></a><a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="36" height="36" alt="PostgreSQL" /></a><a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/docker-colored.svg" width="36" height="36" alt="Docker" /></a><a href="https://www.linux.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="36" height="36" alt="Linux" /></a>
</p>


Данный сервис будет проверяет валидность контейнеров, которые находятся в white листе. 

> - [Основные черты](#Основныечерты)
> - [Для кого сервис](#Для_кого_продукт)
> - [Основной функционал](#Основной_функционал_продукта)
> - [Инструкции](#Инструкции)
> - [Системные требования](#Системные_требования_продукта)


<a name="Основныечерты"></a>
<h1>📌 Основные черты</h1>
<ul>
  <li>🌈 Безопасное развертывание</li>
  <li>🆎 Масштабируемость</li>
  <li>💠 Прозрачность</li>
  <li>🤠 Уникальность для пользователя</li>
  <li>🕊 Легкость</li>
  <li>✍️ Настраиваемость</li>
</ul>

<a name="Для_кого_продукт"></a>
<h1>🌐 Для кого севрис</h1>
Для специалистов, которые регулярно взаимодействуют с различными сервисами в среде контейнеров Docker.

<a name="Основной_функционал_продукта"></a>
<h1>🚀 Основной функционал</h1>
<ul>
  <li>Мониторинг контейнеров</li>
  <li>Добавление легитимных контейнеров в white лист</li>
  <li>Проверка установленых контейнеров по white листу</li>
  <li>Удаление контейнеров, которые находятся не в white листе</li>
</ul>

<a name="Инструкции"></a>
<h1>📤 Инструкции</h1>
<h2>♻ Установка и настройка сервисов</h2></summary> 
<li>Agent - сервис, который отвечает, чтобы ненужный контейнер не запустился на production сервисе, если этого контейнера нет в white листе.</li>
<li>Server - запускает базу данных, где будет храниться white лист; папку сервер желательно установить на отдельном сервере (где будет храниться white лист).</li>
<li>Client - клиент необходимый для экспорта сбилженных контейнеров</li>

<h2>Сценарий использования в pipeline</h2>
1. Понять свой GitLab
2. Поднять GitLab Runner
3. Пример использования в pipeline

```
default:
  image: oeda 
  services:
    - oeda 
  before_script:
    - docker info

variables:

  DOCKER_TLS_CERTDIR: "/certs"

build:
  stage: build
  script:
    - docker pull nginx
security:
  stage: build
  script:
    - oeda
```

4. Сбилдить докер образ dind

```
docker build -f Dockerfile-dind . -t oeda
```

<h2>Установка Agent</h2></summary>
<li> Скачать папку из cmd по пути:</li>
 
 `
 /LeCont/tree/main/cmd/agent
 `
<li> Также скачать Dockerfile по пути:</li>

`
/LeCont/blob/main/Dockerfile
`
<li> После скачивания нужно открыть файл docker-compose-agent.yaml и изменить строчку - SERVER_IP=x.x.x.x, где x.x.x.x - ваш локальный ip-адрес, на котором будет запущен данный сервис</li>
<li> Выполнить команду:</li>

```
docker compose -f docker-compose-agent.yaml up --build
```
<h2>Установка Server</h2></summary>
<li> Скачать папку из cmd по пути:</li>
 
 `
 /LeCont/tree/main/cmd/server
 `
<li> Также скачать Dockerfile по пути:</li>

`
/LeCont/blob/main/docker-compose.yaml
`
<li> После скачивания нужно открыть файл docker-compose-agent.yaml и изменить порты на доступные на вашем сервере</li>

```
 ports:
      - 8000:8000
```

```
 ports:
      - "26257:26257"
      - "8080:8080"
```
<li> Выполнить команду:</li>

```
docker compose -up --build
```

<h2>Установка Client</h2></summary>
<li> Скачать папку из cmd по пути:</li>
 
 `
 /LeCont/tree/main/cmd/client
 `
<li> Также скачать Dockerfile по пути:</li>

`
/LeCont/blob/main/Dockerfile
`
<li> После скачивания нужно открыть файл docker-compose-client.yaml и изменить строчку - SERVER_IP=x.x.x.x, где x.x.x.x - ваш локальный ip-адрес, на котором будет запущен данный сервис</li>
<li> Выполнить команду:</li>

```
docker compose -f docker-compose-client.yaml up --build
```


<a name="Системные_требования_продукта"></a>
<h1>🧩 Системные требования</h1>
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
