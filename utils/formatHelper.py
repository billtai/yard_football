from unidecode import unidecode


class FormatHelper:
    @classmethod
    def trim(self, value):
        return value.strip() if value == str else value

    @classmethod
    def trim_payload(self, payload) -> dict:
        payload_trim = dict()
        for key, value in payload.items():
            payload_trim[key] = value.strip() if type(value) == str else value
        return payload_trim

    @classmethod
    def vi_without_accent_payload(self, payload) -> dict:
        payload_accent = dict()
        for key, value in payload.items():
            payload_accent[key] = unidecode(value.strip()) if type(
                value) == str else value
        return payload_accent

    @classmethod
    def vi_without_accent(self, _str):
        return unidecode(_str)

    @classmethod
    def get_default(self, value, key):
        return value[key] if key in value else ""
