# test_api
_______________RUN API____________________

1) создайте файл .env в site_transations

	.env:
 	
		SECRET_KEY=django-insecure-u_3-yl-wpziw*fpyw5^^dtnki*d83sk25sc&$&-t4_dl@d576-
		EMAIL_HOST_USER=your_email
		EMAIL_HOST_PASSWORD=your_pass
		PASSWORD_DB=exemple()
		DB_NAME=postgres
		DB_USER=postgres
		DB_PORT=5432
		DB_HOST=db
		REDIS_PORT=6379
		REDIS_HOST=redis
	"приизменении портов или хостов пропишите их в docker-compouse.yml"

2) запустите сборку контейнеров:
	docker-compouse docker-compouse.yml build

3) запустите контейнера:
	docker-compouse docker-compouse.yml up -d
4) чтобы добавить root:
	docker-compouse exec web python manage.py createsuperuser

_________Использование API__________________________________
Регестрация пользователя:
(POST) link - http://adress:1337/api/auth/users/, data(username, email, password)
Авторизация 
(POST) link - http://adress:1337/auth/token/login, data(username, password) response(token)

Добовление новой категории 
(POST) link - http://adress:1337/category/ date(name) head(token) 

Добовление новой транзакции
(POST) link - http://adress:1337/transactions/ date(name) head(token)
при добовлении суммы включающуюю категорию расходов добовляйте отрицательный знак перед при указании summ

Изменение удаление просмотр категории, транзакции
(PUT, DELETE, GET) link - http://adress:1337/transactions(category)/id_category(id_transactions)/ date(name) head(token)

Просмотр транзакций или категорй
(GET) link - http://adress:1337/transactions(category)/ date(name) head(token)

Просмотр баланса 
(GET) link -  http://adress:1337/balance/ date(name) head(token)

Фидьтрация и сортировка Транзакций: 
(GET) link - http://adress:1337/transactions(category)?ordering=по чем сортировать,   date(name) head(token)

(GET) link - GET /api/transactions/?summ=&time_after=14:50&time_before=21:00&date_after=2022-11-07&date_before=2022-11-16&summ_min=&summ_max=   date(name) head(token)


_____________________________________________________________________________________________________________________________



______________________sql task__________________

Запросы sql согласно задания
_______________________________________________