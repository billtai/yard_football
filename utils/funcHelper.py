import pandas as pd
from sqlalchemy import func

from utils.timeHelpers import TimeHelper
import pandas as pd
import datetime as dt


class FuncHelper:
    @classmethod
    def group_array(self, _fun_json_object, _label):
        return func.concat("[",
                           func.group_concat(
                               _fun_json_object.distinct()
                           ), "]"
                           ).label(_label)

    def remove_duplicates(data: list):
        # Trường hợp hạng chỗ bị null thì không cần lấy.
        if None in data:
            data = list(filter(None, data))
        new_list = []
        for n, i in enumerate(data):
            if i not in data[n + 1:]:
                new_list.append(i)
        return new_list

    def remove_list_object_null(data: list, key_check: str):
        new_list = []
        for k, i in enumerate(data):
            if i[key_check] is not None:
                new_list.append(i)
        return new_list

    def get_hb(ma_hang_bay: str, hb: dict):
        """
           get hãng bay
           - Nếu ko có trong dict thì lấy default
        """
        init_hb = {
            "logo": None,
            "ten_chuyen_bay": None
        }
        try:
            info_hb = hb.get(ma_hang_bay.lower(), init_hb)
            return info_hb
        except KeyError:
            return init_hb

    def get_series_date_time_format(series, format_input=None, format_out=None,offset_7=None):
        if format_input is None:
            format_input = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s
            # format_input_1 = TimeHelper.FORMAT_TIME_Y_M_D__h_m_s
        if format_out is None:
            format_out = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s

        # .dt.strftime(format_out)
        series_new = pd.to_datetime(
            series, errors='coerce', format=format_input)
        
        if offset_7 is not None:
            series_new = series_new.apply(lambda x: x+dt.timedelta(minutes=420))

        return series_new.dt.strftime(format_out)

    def format_timezone_database(series, format_input=None, format_out=None, offset_7=None):
        if format_input is None:
            format_input = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s
            # format_input_1 = TimeHelper.FORMAT_TIME_Y_M_D__h_m_s
        if format_out is None:
            format_out = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s

        # .dt.strftime(format_out)
        series_new = pd.to_datetime(
            series, errors='coerce', format=format_input)

        if offset_7 is not None:
            series_new = series_new.apply(
                lambda x: x-dt.timedelta(minutes=420))

        return series_new.dt.strftime(format_out)
