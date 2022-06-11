from abc import ABC


class EMailSender(ABC):
    def send(self) -> bool:
        pass

    def get_message(self) -> str:
        pass
