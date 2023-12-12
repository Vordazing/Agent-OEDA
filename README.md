![изображение](https://github.com/Vordazing/Agent-OEDA/assets/105577583/206a3805-9f36-4dc5-9b91-c011ef37a275)

# Agent-OEDA
             OOOOO   EEEEEEE  DDDDD      AAA   
            OO   OO  EE       DD  DD    AAAAA  
            OO   OO  EEEEE    DD   DD  AA   AA 
            OO   OO  EE       DD   DD  AAAAAAA 
             OOOOO   EEEEEEE  DDDDDD   AA   AA           

> - [Основные черты](#Основныечерты)
> - [Компоненты](#Компоненты)
> - [Что используется](#Что_используется)
> - [Как начать пользоваться](#Как_начать_пользоваться)
> - [Структура](#Структура)


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

<a name="Компоненты"></a>
<h1>📤 Компоненты</h1>
<details>
<br/><br/>
<summary><h2>🛠 Obtain Capabilities</h2></summary>
Компонент обеспечивает защиту от несанционированного доступа, проверяет auth.log и по заданным параметрам блокирует подозрительные соединения: если обнаруживает активность, то либо блокирует IP (если подключаются по ssh), либо прерывают сессию пользователя (если пытаются с того же компьютера войти в систему). Если активности нет, то засыпает.
</details>

<details>
<br/><br/>
<summary><h2>📈 Estabilish Accounts</h2></summary>
Этот компонент проверяет создание учётных записей. Если было замечено создание учётной записи, то он запросит подтверждение и заблокирует созданную учётную запись, если его создание не подтверждено.
</details>

<details>
<br/><br/>
<summary><h2>💻 Deploy Container</h2></summary>
Текст
</details>

<details>
<br/><br/>
<summary><h2>📋 Active Scanning</h2></summary>
Для обнаружения сканирования портов используется conntrack (функция ядра, которая отвечает за отслеживание соединений). Скрипт собирает информацию в реальном времени, затем обрабатывает его, если замечается большое количество отмененных (DESTROY) соединений с разными портами, то запоминается адрес устройства, с которого приходили запросы, и выводится уведомление.
</details>




<a name="Что_используется"></a>
<h1>🚀 Что используется</h1>

<a name="Как_начать_пользоваться"></a>
<h1>🧩 Как начать пользоваться</h1>


<a name="Структура"></a>
<h1>✨ Структура</h1>

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
