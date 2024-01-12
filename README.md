

# LeCont ![](https://user-images.githubusercontent.com/18350557/176309783-0785949b-9127-417c-8b55-ab5a4333674e.gif)
<p align="left"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://golang.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/go/go-original.svg" alt="go" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> </p>

<p align="left">
<a href="https://go.dev/doc/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/go-colored.svg" width="36" height="36" alt="Go" /></a><a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="36" height="36" alt="PostgreSQL" /></a><a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/docker-colored.svg" width="36" height="36" alt="Docker" /></a><a href="https://www.linux.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="36" height="36" alt="Linux" /></a>
</p>


Данный сервис будет проверяет валидность контейнеров, которые находятся в white листе. 

> - [Основные черты](#Основныечерты)
> - [Для кого сервис](#Для_кого_продукт)
> - [Основной функционал продукта](#Основной_функционал_продукта)
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
<h1>🚀 Основной функционал продукта</h1>
<ul>
  <li>Мониторинг контейнеров</li>
  <li>Добавление в white листы контейнера</li>
  <li>Проверка установленых контейнеров по white листу</li>
  <li>Удаление контейнеров, которые находятся не в white листе</li>
</ul>

<a name="Инструкции"></a>
<h1>📤 Инструкции</h1>
<details>
<br/><br/>
<summary><h2>♻ Установка и настройка сервисов</h2></summary> 
<li>Agent - сервис, который отвечает, чтобы ненужный контейнер не запустился на production сервисе, если этого контейнера нет в white листу.</li>
<li>Server - запускает базу данных, где будет храниться white лист; папку сервер желательно установить на отдельном сервере (где будет храниться white лист).</li>
<li>Client - может находиться и на сервере, где white лист, и в другом месте, где он будет принимать контейнеры.</li>
  
</details>
<details>
<br/><br/>
<summary><h2>💬 Установка и настройка внешнего сервера с white листом</h2></summary> 
<li>Откройте браузер и перейдите на страницу GitHub, перейдите на вкладку Репозитории и выберите репозиторий для клонирования. Скопируйте URL-адрес клона.
Выполните команду: git clone <адрес репозитория>.</li>
<li>Далее необходимо поднять контейнер с помощью команды: docker-compose up</li>
</details>


<a name="Системные_требования_продукта"></a>
<h1>🧩 Системные требования</h1>
<ul>
  <li>Docker</li>
  <li>1 CPU</li>
  <li>25 ГБ RAW</li>
  <li>1 ОЗУ</li>
  <li>Linux</li>
</ul>



<h1 align="center">
  <a href="https://docusaurus.io">
    <img width="50%" src="https://github.com/Vordazing/Agent-OEDA/blob/main/lecont-logo.png" />
  </a>
</h1>
