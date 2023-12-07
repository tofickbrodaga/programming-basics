from typing import Any


class Worker:
    def __init__(self, name: str) -> None:
        self.name = name

    def notify(self, message: str) -> None:
        print(f'{self.__class__.__name__} {self.name} recieved message: {message}')


class Mail:
    _notifier_method: str = 'notify'

    def __init__(self) -> None:
        self._clients = []

    def add_client(self, client: Any, rank: int = 1) -> None:
        if not hasattr(client, self._notifier_method):
            raise TypeError(f'Mail client should have outer public method <{self._notifier_method}>.')
        self._clients[client] = rank

    def remove_client(self, client: Any) -> None:
        if client not in self._clients.keys():
            raise ValueError(f'Client {client} is not in Mail clients list')
        del self._clients[client]

    def client_filter(self, sender: Any) -> None:
        sender_rank = self._clients[sender]
        return [client for client, rank in self._clients.items() if rank <= sender_rank]

    def message(self, message: str, sender: Any) -> None:
        for client in self.client_filter(sender):
            if client is not sender:
                getattr(client, self._notifier_method)(message)
        
workers_1 = Worker('Ivan'), Worker('Peter'), Worker('Vasiliy')
workers_2 = Worker('Egor'), Worker('Vadim'), Worker('Pavel')
yandex_mail = Mail()
for workers in workers_1, workers_2:
    for index, worker in enumerate(workers):
        yandex_mail.add_client(worker, index)

yandex_mail.message('сообщение для всех', workers_2[2])
yandex_mail.message('сообщение для некоторых', workers_2[0])
