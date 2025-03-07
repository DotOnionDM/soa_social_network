## User Service
### Зона ответственности
- Регистрация новых пользователей и их аутентификация.
- Хранение и управление данными пользователей, в том числе профилей и ролей.
- Управление сессиями пользователей для обеспечения безопасности и стабильности аутентификации.

### Основные функции
- Хранение детальной информации о каждом пользователе (таблица User).
- Управление ролями пользователей с дополненной информацией в таблице Role (описание, даты создания и обновления).
- Управление сессиями через таблицу Session, включающей данные о токенах, времени создания и истечения сессии.

### Границы сервиса
- Изолированная бизнес-логика, задача которой – безопасное и надёжное управление пользователями.
- Не занимается обработкой контента, статистики или маршрутизацией запросов – только данные пользователей.
- Обеспечивает взаимодействие с другими сервисами посредством API: предоставляет информацию по пользователю, необходимую для создания записей в сервисе постов и комментариев.
