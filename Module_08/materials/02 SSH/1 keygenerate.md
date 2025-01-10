## Проверить наличие SSH
ssh -y

## Генерация откртого и закрытого ключа
ssh-keygen -t rsa  -b 2048 -C "TimeWeb Machine" -f timeweb


## Посмотреть открытый ключ
cat timeweb.pub