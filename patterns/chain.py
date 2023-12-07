class CorseWords:
    words = 'php', 'javafx', 'windows', 'pascal', 'microsoft'

class Beaautifier:
    @staticmethod
    def censor(text: str) -> str:
        text = text.lower()
        for word in CorseWords.words:
            if len(word) > 2:
                filler = '*' * (len(word) - 2)
                new = f'{word[0]}{filler}{word[-1]}'
            else:
                new = "*" * len(word)
            text = text.replace(word, new)
        return text

    @staticmethod
    def entitler(text: str) -> str:
        return text.title()

    @staticmethod
    def dot(text: str) -> str:
        return f'{text}.' if text[-1] != '.' else text

    @classmethod
    def beautify(cls, text: str) -> str:
        return cls.dot(cls.entitler(cls.censor(text)))