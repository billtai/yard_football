
class FormatHelper:

    @classmethod
    def trim_payload(self, payload) -> dict:
        payload_trim = dict()
        for key, value in payload.items():
            payload_trim[key] = value.strip() if type(value) == str else value
        return payload_trim

