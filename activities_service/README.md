## Activities Service
### Зона ответственности
- Управление созданием, хранением и редактированием постов.
- Организация системы комментариев, позволяющей пользователям взаимодействовать с контентом.
- Поддержка системы тегирования для организации и поиска контента.

### Основные функции
- Управление данными постов с использованием таблицы Post, где хранится информация о контенте и времени создания.
- Организация комментариев в таблице Comment, содержащей ссылки на посты и пользователей, а также временные метки.
- Управление метаданными тегов через таблицу Tag для классификации и поиска контента.

### Границы сервиса
- Отвечает исключительно за управление контентом (посты и комментарии), не затрагивая процессы аутентификации или анализа статистики.
- Взаимодействует с сервисом пользователей для проверки подлинности автора контента.
- Обеспечивает передачу данных о активности (например, количество комментариев) в сервис статистики для дальнейшей агрегации.
