Ограничьте возможности пользователя рамками одной определенной директории. Внутри нее он может делать все, что хочет: создавать и удалять любые файлы и папки. Нужно проследить, чтобы пользователь не мог совершить никаких действий вне пределов этой директории. Пользователь, в идеале, вообще не должен догадываться, что за пределами этой директории что-то есть.
<img width="307" alt="image" src="https://user-images.githubusercontent.com/91737637/146652873-81944186-2bf1-4ecb-905d-f8bbf420e49e.png">


Создаем каталог temirr с помощью команды mkdir

<img width="292" alt="image" src="https://user-images.githubusercontent.com/91737637/146652275-e6e1d909-3b83-4df8-abdf-a4c014c2f03b.png">

<img width="566" alt="image" src="https://user-images.githubusercontent.com/91737637/146652292-6f47e631-688a-425d-93b1-c274c39ed548.png">

<img width="505" alt="image" src="https://user-images.githubusercontent.com/91737637/146652297-ff0c2807-348c-4c36-80df-47b45f0b0cda.png">

удаляем каталог temirr с помощью команды deldir
<img width="166" alt="image" src="https://user-images.githubusercontent.com/91737637/146652336-8316c27c-0cc5-4bfe-b0e3-d4359c1b80fe.png">

<img width="686" alt="image" src="https://user-images.githubusercontent.com/91737637/146652358-2ae593cf-fe88-4e0f-a431-a7adade4da31.png">

создаем файл с помощью команды touch

<img width="127" alt="image" src="https://user-images.githubusercontent.com/91737637/146652367-06a28c1d-5897-441b-88f9-8eee86ec6489.png">

<img width="646" alt="image" src="https://user-images.githubusercontent.com/91737637/146652499-43406e48-cd21-475e-aea7-00f84ca6930a.png">

<img width="182" alt="image" src="https://user-images.githubusercontent.com/91737637/146652514-ecc6a84c-b4d3-4425-b1d3-da021b3fdf96.png">

<img width="591" alt="image" src="https://user-images.githubusercontent.com/91737637/146652520-f9db1b06-96c9-4e19-a54f-e551c23ab9e4.png">

Создаем файл, а затем переименовываю его, с помощью команды mv


<img width="218" alt="image" src="https://user-images.githubusercontent.com/91737637/146652560-25c48478-b872-4e9c-b500-c5119eb27a98.png">

с помощбю команды cat выводим содержимое файла: 

<img width="206" alt="image" src="https://user-images.githubusercontent.com/91737637/146652612-db068265-47e6-4c09-b38b-737ce31335b5.png">

получаем файл с помощью команды get:

<img width="161" alt="image" src="https://user-images.githubusercontent.com/91737637/146652986-009c60c3-5ae9-4f3e-86f6-d202cec32e87.png">
<img width="575" alt="image" src="https://user-images.githubusercontent.com/91737637/146652999-4cd79444-44d0-4277-ae4a-832675758bba.png">

отправляем файл от клиента серверу, с помощью команды send:

<img width="287" alt="image" src="https://user-images.githubusercontent.com/91737637/146653077-367d27a9-114b-4735-9c9d-aff56fdaae11.png">

<img width="372" alt="image" src="https://user-images.githubusercontent.com/91737637/146653082-6580120b-b2e6-40e8-95c0-b5bae58f2648.png">

Добавьте логирование всех действий сервера в файл. Можете использовать разные файлы для разных действий, например: подключения, авторизации, операции с файлами.
Добавьте возможность авторизации пользователя на сервере.
<img width="534" alt="image" src="https://user-images.githubusercontent.com/91737637/146653134-90ff341a-15aa-43db-904f-6c6dc15a1b0b.png">

Добавьте возможность регистрации новых пользователей на сервере. При регистрации для пользователя создается новая рабочая папка (проще всего для ее имени использовать логин пользователя) и сфера деятельности этого пользователя ограничивается этой папкой.

Реализуйте учётную запись администратора сервера.
Реализуете квотирование дискового пространства для каждого пользователя.

<img width="207" alt="image" src="https://user-images.githubusercontent.com/91737637/146653269-d192a26d-256f-4a71-9f4a-909a5d551c6a.png">
<img width="440" alt="image" src="https://user-images.githubusercontent.com/91737637/146653321-0e3aa91e-0fd5-473e-a6de-bf234aaa98aa.png">


