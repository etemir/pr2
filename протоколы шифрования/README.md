Основной алгоритм работы клиента и сервера.
При запуске клиент и сервер генерируют каждый свою пару ключей.

генерация ключей в server.py:
<img width="596" alt="image" src="https://user-images.githubusercontent.com/91737637/146613209-f3fdbf08-bd93-4c9c-9289-118b4208d8f5.png">

генерация ключей в client.py:
<img width="458" alt="image" src="https://user-images.githubusercontent.com/91737637/146613326-365ad776-b44f-4d51-8a30-99cab295191b.png">

При подключении клиент посылает серверу свой открытый ключ.
<img width="283" alt="image" src="https://user-images.githubusercontent.com/91737637/146613456-b60ad779-341b-45c6-896e-cebc7c0ff500.png">

В ответ, сервер посылает клиенту открытый ключ сервера.
<img width="253" alt="image" src="https://user-images.githubusercontent.com/91737637/146613524-bccb51a4-b93d-44d1-b568-6ba944d4ab36.png">

Клиент посылает сообщение серверу, шифруя его своим закрытым ключом и открытым ключом сервера.
<img width="286" alt="image" src="https://user-images.githubusercontent.com/91737637/146613690-ae57362b-e643-4585-a145-551baafa087a.png">

Сервер принимает сообщение, расшифровывает его сначала своим закрытым ключом, а потом - открытым ключом клиента.
<img width="280" alt="image" src="https://user-images.githubusercontent.com/91737637/146613703-64f58195-924b-4728-83d4-7a5470139067.png">


Обратное сообщение посылается аналогично.

Модифицируйте код клиента и сервера так, чтобы приватный и публичный ключ хранились в текстовых файлах на диске и, таким образом, переиспользовались между запусками.

<img width="623" alt="image" src="https://user-images.githubusercontent.com/91737637/146613899-e4e3deca-9daf-4917-9204-9cd8ac14fb40.png">

client:
<img width="602" alt="image" src="https://user-images.githubusercontent.com/91737637/146613992-87a60143-1c5b-47be-8088-f3bb798ab2ee.png">

server:
<img width="483" alt="image" src="https://user-images.githubusercontent.com/91737637/146614018-ee0ac21b-b2d0-4542-b8aa-3eb876465d5c.png">

Проведите рефакторинг кода клиента и сервера так, чтобы все, относящееся к генерации ключей, установлению режима шифрования, шифрованию исходящих и дешифрованию входящих сообщений было отделено от основного алгоритма обмена сообщениями.

<img width="618" alt="image" src="https://user-images.githubusercontent.com/91737637/146614313-e9ad96ae-bd19-4f22-b983-af2e63ad875e.png">

<img width="471" alt="image" src="https://user-images.githubusercontent.com/91737637/146614326-0298eea8-7961-4e54-bccf-e6a52744176d.png">

Реализуйте на сервере проверку входящих сертификатов. На сервере должен храниться список разрешенных ключей. Когда клиент посылает на сервер свой публичный ключ, сервер ищет его среди разрешенных и, если такого не находит, разрывает соединение. Проверьте правильность работы не нескольких разных клиентах.
<img width="574" alt="image" src="https://user-images.githubusercontent.com/91737637/146614490-7e2dc339-0a0c-4a9b-b11a-dafe0c49adaa.png">

<img width="567" alt="image" src="https://user-images.githubusercontent.com/91737637/146614527-026fa2dd-b792-4422-94da-f5210da83fd3.png">


Модифицируйте код клиента и сервера таким образом, чтобы установление режима шифрования происходило при подключении на один порт, а основное общение - на другом порту. Номер порта можно передавать как первое зашифрованное сообщение.
<img width="575" alt="image" src="https://user-images.githubusercontent.com/91737637/146614567-454ddb42-afa9-4057-a191-ded5cdb9bc28.png">
