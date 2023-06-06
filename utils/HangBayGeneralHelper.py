from flask import request, current_app

class HangBayGeneralHelper:
    def get_info_hang_bay(model):
        """
        -> Check nếu như chưa nhập trên tat thì trả null
        """
        if bool(model):
            return {
                "logo"          : current_app.config['BASE_URL'] + "/assets/" + getattr(model, 'logo', None),
                "ten_hang_bay"  : getattr(model, 'ten', None),
                "ten_tat"       : getattr(model, 'ten_tat', None)
                
            }
        return {
            "logo": None,
            "ten_hang_bay": None,
            "ten_tat" : None
        }
