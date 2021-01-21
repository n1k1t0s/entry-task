Я решил использовать для реализации задания язык python и готовые библиотеки для этого языка от Google, а также Directory API.
Авторизация взята мной из раздела Quickstart, во время изучения API.

Для коректной работы программы необходимы библиотеки для python и файл credentials.json, находящийся в одной папке с фалйом .py

[ссылка для получения файла c данными для работы программы (кнопка Enable the Directory API)](https://developers.google.com/admin-sdk/directory/v1/quickstart/python?hl=uk)

На той же странице имеется команда для установки всех необходимых библиотек.

Касаемо идемпотентности, при попытке создать нового пользователя с данными, которые повторяют уже существующую учетную звпись, возвращается ошибка:
><HttpError 409 when requesting https://admin.googleapis.com/admin/directory/v1/users?alt=json returned "Entity already exists.". Details: "Entity already exists.">

Надеюсь я правильно воспринял и выполнил ваше задание.
