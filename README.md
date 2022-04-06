# Backend para to-do List

> Proyecto backend api rest construida con python y mongodb

## 💻 Pré-requisitos

Antes de comenzar, verifique que contienes los seguintes requisitos:
* Tener instalado python
* Visual Studio Code
* Crear una bases de datos en mongo db

##  Instalando

Para instalar el proyecto localmente, siga estas etapas:


<img src="https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white" />

ingresa a tu ventana de comandos y ejecuta lo siguiente para clonar el repositorio
```
git clone https://github.com/diegoabt18/backtodolist.git
```
Instala las dependecias que se encuentra en el archivo requeriments.txt
```
utiliza el comando "pip install" segudido del paquete a instalar
```
Configura el archivo settings para añadir la conexion a la bases de datos de mongo db

settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            "host":"esrcibe aqui el nombre del host",
            "name":"nombre bases de datos",
            "authMechanism":"SCRAM-SHA-1" #For atlas cloud db
        },
    }
}
```

por utimo ejecuta el comando para iniciar el servidor localmente

```
py start server
```

## ☕ Usando
<img  src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>

<img  src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>

<img  src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>

<img  src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white"/>


## 🚀 Pruebas 
Consulte las pruebas realizadas a travez de postman para validar el api rest
![image](https://user-images.githubusercontent.com/47578861/161892049-3d9cb0d5-4291-4836-bc44-aca5defc8294.png)

[despliegue de la app en heroku](https://backtodolist-v1.herokuapp.com/)

[Link test postman](https://documenter.getpostman.com/view/10382725/UVyuTFwu)
:hammer: 
## 🤝 Autores


<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/Diegoabt18" width="100px;" alt="Foto do Diego Botello no GitHub"/><br>
        <sub>
          <b>Diego Botello</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 📝 Licencia

