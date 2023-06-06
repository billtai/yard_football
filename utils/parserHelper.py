class ParserHelper:
    @classmethod
    def getattr_parser(self, obj={}, key='', default_value=None):
        value = getattr(obj, key, default_value)
        if type(value) is list and len(value) > 0:
            return value[0]
        return value

    @classmethod
    def getValue(self, value):
        if type(value) is list and len(value) > 0:
            return value[0]
        return value

    @classmethod
    def get_value_payload_or_default(self, field, payload, default_value=''):
        if field in payload:
            return self.getValue(payload[field])
        return default_value
