# vuln-app
#Уязвимая версия приложения

### Инструкция по сборке и запуску приложения

> - git clone "текущий репозиторий"
> - cd app
> - python __init__.py
> - flask приложение будет запущено по адресу http://127.0.0.1:8089

![image](https://github.com/medarov411/vuln-app/assets/60567375/302c807a-5503-411e-a291-bbe552f247ec)



### Proof of Concept
SSTI
url - http://127.0.0.1:8089/contact


### Дополнительные комментарии
> От себя решил добавить SSTI с фильтрацией, все таки это flask. Не добавить в него ssti, было бы неуважительно :)


