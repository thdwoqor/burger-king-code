# Burger King Code
<a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"/></a>
<a href="https://www.nginx.com/"><img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white"/></a>
<a href="https://fastapi.tiangolo.com/ko/"><img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"/></a>
<a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/></a>  
>버거킹 설문조사 코드 공유 사이트 

| **메인페이지** | **메인 페이지** - 검색 |
| :---: | :---: | 
| ![메인페이지](https://user-images.githubusercontent.com/83541246/157061650-f7ddfe50-7cf8-4c4a-8e60-4acc1bf856b9.png)| ![메인 페이지 - 검색](https://user-images.githubusercontent.com/83541246/157061745-5a12b2cd-ceb2-4c84-84e8-4d6475cf52b7.png) |  

| **코드가 등록된 경우** | **코드가 등록 안된 경우** |
| :---: | :---: | 
| ![코드가 등록된 경우](https://user-images.githubusercontent.com/83541246/157061919-add7cc12-1ce4-40c2-9c56-738f315d1888.png)| ![코드가 등록 안된 경우](https://user-images.githubusercontent.com/83541246/157061924-0c008d7d-d351-4f1b-a8a6-c9f8f47c5923.png) | 
## Getting Started  

### Installation

<pre><code>git clone https://github.com/thdwoqor/burger-king-code.git

echo "MARIADB_USER=[<b>MARIADB_USER</b>]" >> .env
echo "MARIADB_PASSWORD=[<b>MARIADB_PASSWORD</b>]" >> .env
echo "MARIADB_HOST=[<b>MARIADB_HOST</b>]" >> .env
echo "MARIADB_PORT=[<b>MARIADB_PORT</b>]" >> .env
echo "MARIADB_DATABASE=[<b>MARIADB_DATABASE</b>]" >> .env

mkdir -p mariadb/{sql,config}
# your initial setting file put it in sql
# your mariadb config file put it in config

touch nginx.conf 
# your nginx.conf file
</code></pre>

### Run Attendance

<pre><code>docker-compose up</code></pre>

## LICENSE

[MIT License](./LICENSE)
