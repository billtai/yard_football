ENVIRONMENT = 'prod'


def isEnvDev():
    """
        Check Môi trường.
        - Môi trờng dev: disable jwt and fill thông tin sẵn.
        - Môi trường prod: allow jwt clear thông tin có sẵn.
        - Mọi config khác điều đưa vào file config.py
    """
    return ENVIRONMENT == "dev"
