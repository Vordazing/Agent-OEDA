

# LeCont
             ///          
Данный продукт, будет проверяет валидность контейнеров по white листу. 

> - [Основные черты](#Основныечерты)
> - [Для кого продукт](#Для_кого_продукт)
> - [Основной функционал продукта](#Основной_функционал_продукта)
> - [Контроль и Управление](#Контроль_и_Управление)
> - [Инструкция](#Инструкция)
> - [Что необходимо понимать сотрудникам](#Что_необходимо_понимать_сотрудникам)
> - [Системные требования продукта](#Системные_требования_продукта)
> - [Как развернуть внешний сервер с white листом](#Как_развернуть_внешний_сервер_с_white_листом)
> - [Структура продукта](#Структура_продукта)


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
<h1>🌐 Для кого продукт</h1>
Для тех людей, которые разварачивают различные сервисы в докерах на серверах. 

<a name="Основной_функционал_продукта"></a>
<h1>🚀 Основной функционал продукта</h1>
<ul>
  <li>Мониторинг контейнеров. </li>
  <li>Добавление в white листы контейнера. </li>
  <li>Проверка установленых контейнеров по white листу. </li>
  <li>Начальное действие при обнаружении контейнеров не в white листе. </li>
</ul>

<a name="Контроль_и_Управление"></a>
<h1>♻ Контроль и Управление</h1>
<details>
<br/><br/>
<summary><h2>Администратор</h2></summary>
  
</details>
<details>
<br/><br/>
<summary><h2>Мониторщик</h2></summary>
  
</details>

<a name="Инструкция"></a>
<h1>📤 Инструкции</h1>
<details>
<br/><br/>
<summary><h2>Инструкция пользования для администратора</h2></summary>
  
</details>

<details>
<br/><br/>
<summary><h2>Инструкция пользования для монитрощика</h2></summary>
  
</details>


<a name="Что_необходимо_понимать_сотрудникам"></a>
<h1>🧠 Что необходимо понимать сотрудникам</h1>
<details>
<br/><br/>
<summary><h2>Администратор </h2></summary>
  
</details>

<details>
<br/><br/>
<summary><h2>Мониторщик</h2></summary>
  
</details>

<a name="Системные_требования_продукта"></a>
<h1>🧩 Системные требования продукта</h1>
<ul>
  <li>Язык программирования </li>
    <ul>
      <li>python3.10+</li></li>
    </ul>
  <li>Библиотеки </li>
    <ul>
      <li>Библиотеки питона (позже добавим весь список)</li> 
      <li>YAML </li>
      <li>JSON </li>
      <li>Docker</li>
    </ul>
   <li>Требуемая операционная система</li>
    <ul>
      <li>На сереверах Linux (Ubuntu and Debian)</li>
    </ul>
<ul/>

<a name="Как_развернуть_внешний_сервер_с_white_листом"></a>
<h1>💬 Как развернуть внешний сервер с white листом</h1>

<a name="Структура_продукта"></a>
<h1>✨ Структура продукта</h1>

```
└── Public
└── static
    └── favicon
└── src
    ├── assets
    │   ├── _base
    │   ├── _general
    │   ├── _reset
    │   ├── _vars
    │   └── main
    ├── components
    │   ├── Article_page
    |   |   ├── MainBlog
    |   |   ├── Post
    |   |   ├── Share
    |   |   └── Sidebar
    |   ├── Main_page
    |   |   ├── Article
    |   |   ├── LatestPost
    |   |   ├── MainPage
    |   |   └── Sidebar
    │   ├── Footer
    │   ├── Head
    │   ├── Header
    │   ├── Layout
    │   ├── Loader
    │   ├── Mode
    │   └── Subscribe
    ├── Pages
    │   ├── 404
    │   └── Index
    ├── Posts
    ├── templates
    │   └── blog
    └── Context

```
<h1 align="center">
  <a href="https://docusaurus.io">
    <img width="50%" src="https://github.com/Vordazing/Agent-OEDA/blob/main/logotype.png" />
  </a>
</h1>
