Установили nginx. Он слушает входящие соединения на 80 порту. 
<img width="206" alt="image" src="https://user-images.githubusercontent.com/91737637/146654651-b459e41d-8221-4e51-9520-db5304d5df6f.png">

Делаем прокси на порт 8000, так как на нем будет запущен gunicorn:
<img width="258" alt="image" src="https://user-images.githubusercontent.com/91737637/146654712-6416f8d6-5b6f-485b-89d4-68021ad385db.png">

<img width="326" alt="image" src="https://user-images.githubusercontent.com/91737637/146654734-1c19688e-9d34-482b-b1f2-2bbc9f879774.png">

Через gunicorn мы запускаем наше приложение flask.
Теперь мы делаем post запрос в формате json
<img width="560" alt="image" src="https://user-images.githubusercontent.com/91737637/146654768-7616989a-f5bc-4c95-9301-4ae7b9942885.png">

и получаем ответ тоже в формате json.
Происходит хэширование пароля с солью по алгоритму SHA-256.

<img width="376" alt="image" src="https://user-images.githubusercontent.com/91737637/146654806-aa9f8ca2-4426-4669-9c2f-79e164dc0f6a.png">

функция saver сохраняет словарь, который хранит логин (email) и пароль пользователя, а также дату регистрации. Она сохраняет его в виде сериализоного объекста с помощью модуля pickle.
<img width="355" alt="image" src="https://user-images.githubusercontent.com/91737637/146654830-4e6d3518-da64-42e0-b4bb-9f159ed5e99e.png">

мы создали самоподисанный сертификат SSL и транслируем входящие соединения порту 443 (протокол https) на порт 8000 gunicorn
<img width="329" alt="image" src="https://user-images.githubusercontent.com/91737637/146654916-8ef1d986-7fdc-471e-8d5c-0addb045b4a3.png">



