Модифицировать простой эхо-сервер таким образом, чтобы при подключении клиента создавался новый поток, в котором происходило взаимодействие с ним.
Работа с клиентом происходит в функции user_thread, которая запускается в отдельном потоке.

<img width="609" alt="image" src="https://user-images.githubusercontent.com/91737637/146837781-b20f2453-fb08-479d-a772-538300dc32ee.png">

Реализовать простой чат сервер на базе сервера аутентификации. Сервер должен обеспечивать подключение многих пользователей одновременно, отслеживание имен пользователей, поддерживать историю сообщений и пересылку сообщений от каждого пользователя всем остальным.

Запустили три клиента и один сервер и переслали сообщения друг другу.

<img width="833" alt="image" src="https://user-images.githubusercontent.com/91737637/146838507-63047c83-2a41-4dac-952c-6a60dd4ba268.png">

Даже после отключения одного клиента программа продолжает работать.

<img width="827" alt="image" src="https://user-images.githubusercontent.com/91737637/146838726-41d6eb7c-1db4-4fae-93bd-e1128081ea4d.png">

Реализовать сервер с управляющим потоком. При создании сервера прослушивание портов происходит в отдельном потоке, а главный поток программы в это время способен принимать команды от пользователя. Необходимо реализовать следующие команды:
вся работа программы с клиентами выполняется в функции в гет-коннект.

<img width="568" alt="image" src="https://user-images.githubusercontent.com/91737637/146838901-bc4af95f-4e9e-464e-84cd-dfd0d15df57f.png">

Отключение сервера (завершение программы);
Сервер отключился вместе с клиентами.

<img width="825" alt="image" src="https://user-images.githubusercontent.com/91737637/146839042-eecebdb7-97d4-4bf9-9408-36d03d01fade.png">

Пауза (остановка прослушивание порта);
После вызова команды stop listen остановилась прослушка порта.
<img width="677" alt="image" src="https://user-images.githubusercontent.com/91737637/146839495-d5832c89-8b3d-4b4b-ad43-af3e5e356106.png">

после вызова команды start listen возобновилась прослушка порта и клиент был подключен.
<img width="754" alt="image" src="https://user-images.githubusercontent.com/91737637/146839665-7f2324c8-afd1-4b92-b2cc-9801a6b274c4.png">

Очистка логов;
после вызова команды clear log файл с логами был очищен, как и консольный вывод.

<img width="501" alt="image" src="https://user-images.githubusercontent.com/91737637/146839738-8a5dec65-aabc-436b-bc73-cf443ed8c548.png">

<img width="556" alt="image" src="https://user-images.githubusercontent.com/91737637/146839786-c75d79af-2886-4f06-966a-e0742a5efaa0.png">

Очистка файла идентификации.

<img width="297" alt="image" src="https://user-images.githubusercontent.com/91737637/146839967-80499e9a-227f-4f2d-9c30-fade9e7f7850.png">

<img width="187" alt="image" src="https://user-images.githubusercontent.com/91737637/146840002-d4a77beb-8589-4b2f-b6fc-03b33d86d464.png">

<img width="450" alt="image" src="https://user-images.githubusercontent.com/91737637/146840038-d0f0bc18-af1a-4456-ac1c-7f502f285f7c.png">

