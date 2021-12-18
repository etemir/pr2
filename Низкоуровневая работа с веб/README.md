Дополнительные задания
При ответе вашего сервера посылайте некоторые основные заголовки:
Date
Content-type
Server
Content-length
Connection: close.

<img width="347" alt="image" src="https://user-images.githubusercontent.com/91737637/146621936-8fb51af1-1ad1-4373-858d-806de4bf3b4b.png">

<img width="430" alt="image" src="https://user-images.githubusercontent.com/91737637/146622623-1b871973-570d-427b-84da-ebd30d3231e9.png">



Создайте файл настроек вашего веб-сервера, в котором можно задать прослушиваемый порт, рабочую директорию, максимальный объем запроса в байтах. Можете добавить собственные настройки по желанию.
<img width="196" alt="image" src="https://user-images.githubusercontent.com/91737637/146621964-e4d3181e-c784-4e5f-92f8-ebf224c8ad47.png">


Если файл не найден, сервер передает в сокет специальный код ошибки - 404.

Сервер должен работать в многопоточном режиме.
Сервер должен вести логи в следующем формате: Дата запроса. IP-адрес клиента, имя запрошенного файла, код ошибки.
<img width="441" alt="image" src="https://user-images.githubusercontent.com/91737637/146622211-4f37e276-46a2-4e27-815c-eadaf846503f.png">
<img width="779" alt="image" src="https://user-images.githubusercontent.com/91737637/146622470-a71db3e7-d8b1-46cc-b209-03bf2fb9bccc.png">


Добавьте возможность запрашивать только определенные типы файлов (.html, .css, .js и так далее). При запросе неразрешенного типа, верните ошибку 403.
<img width="530" alt="image" src="https://user-images.githubusercontent.com/91737637/146622232-df7e2854-1230-4630-b669-1e45def396c5.png">

Реализуйте поддержку постоянного соединения с несколькими запросами.
<img width="229" alt="image" src="https://user-images.githubusercontent.com/91737637/146622563-8508cc66-42cd-43e9-8f27-9911f29b34a0.png">

Реализуйте поддержку бинарных типов данных, в частночти, картинок.
<img width="419" alt="image" src="https://user-images.githubusercontent.com/91737637/146622181-9ced4515-43c8-4a83-a30e-24d274d3a76e.png">

