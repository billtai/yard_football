from datetime import datetime, timedelta, tzinfo
from enum import auto
import time
import time as t
from string import Formatter
from sqlalchemy.sql.elements import Null
from settings.useTimeZone import time_zone_vi
from pytz import all_timezones


class TimeHelper(enumerate):
    TIME_OFFSET_MINUTES_UTC_7 = 420
    TIME_OFFSET_MINUTES_UTC_VNA = 720
    TIME_OFFSET_MINUTES_UTC_1 = 60
    TIME_OFFSET_MINUTES_UTC_0 = 0
    FORMAT_TIME_Y_M_D = "%Y-%m-%d"
    FORMAT_TIME_M_D = "%m-%d"
    FORMAT_TIME_Y_M_D_Z = "%Y-%m-%dZ"
    FORMAT_TIME__DMY = "%d/%m/%Y" 
    FORMAT_TIME_FULL = "%Y/%m/%d %H:%M:%S"
    FORMAT_TIME_FULL_Z = "%Y-%m-%dT%H:%M:%SZ"
    FORMAT_TIME_FULL_ZZ = "%Y-%m-%dT%H:%M:%S.%fZ"
    FORMAT_TIME_FULL_z = "%Y-%m-%dT%H:%M:%S%z"
    FORMAT_TIME_H_T = "%m-%dT%H:%M"
    FORMAT_TIME_Z = "%Y-%m-%d %H:%M:%SZ"
    FORMAT_TIME_D_M_Y = "%d-%m-%Y"
    FORMAT_TIME_D_M_Y__h_m_s = "%d-%m-%Y %H:%M:%S"
    FORMAT_TIME_h_m_s__D_M_Y = "%H:%M:%S %d-%m-%Y"
    FORMAT_TIME_D_M_Y_T_h_m_s = "%d-%m-%YT%H:%M:%S"
    FORMAT_TIME_Y_M_D__h_m_s = "%Y-%m-%d %H:%M:%S"
    FORMAT_TIME_Y_D_M_T_h_m_s = "%Y-%d-%mT%H:%M:%S"
    FORMAT_TIME_Y_M_D_T_h_m_s = "%Y-%m-%dT%H:%M:%S"
    FORMAT_TIME_Y_M_D__h_m_s_z = "%Y-%m-%d %H:%M:%SZ"
    FORMAT_TIME_DMY = "%d-%m-%Y" # 08/09/2021
    FORMAT_TIME_h_m = "%H:%M"
    FORMAT_TIME_h_m_s = "%H:%M:%S"
    TIME_ZONE_NAME = 'Asia/Ho_Chi_Minh'
    FORMAT_TIME_Y_M_D_T_h_m = "%Y-%m-%dT%H:%M"
    # FORMAT SQL
    SQL_FORMAT_TIME_D_M_Y__h_m_s = "%d-%m-%Y %k:%i:%s"

    HOURS = auto()
    SECONDS = auto()
    MINUTES = auto()

    @classmethod
    def getSeconds(self, days):
        return days*24*60*60

    @classmethod
    def localTzname(self):
        if time.daylight:
            offsetHour = time.altzone / 3600
        else:
            offsetHour = time.timezone / 3600
        return 'Etc/GMT%+d' % offsetHour

    @classmethod
    def get_date_now_to_str(self):
        datetime_vi = datetime.now(time_zone_vi)
        return datetime_vi.strftime(self.FORMAT_TIME_FULL)

    @classmethod
    def get_str_to_date(self, str_date):
        return datetime.strptime(str_date, TimeHelper.FORMAT_TIME_FULL)

    @classmethod
    def get_date_now_time_zone_vi(self):
        return datetime.now(time_zone_vi)

    @classmethod
    def get_date_now(self):
        return datetime.now(time_zone_vi).replace(tzinfo=None, microsecond=0)

    @classmethod
    def convert_str_form_time(self, date_time, format):
        return datetime.strftime(date_time, format)

    @classmethod
    def convert_date_body_to_request(self, str_date):
        dt_date = datetime.strptime(
            str_date, self.FORMAT_TIME_D_M_Y)
        # Xử lý ngày sinh
        date_y_m_d = datetime.strftime(
            dt_date, self.FORMAT_TIME_Y_M_D)
        return date_y_m_d

    @classmethod
    def convert_date_body_to_request_full(self, str_date):
        dt_date = datetime.strptime(
            str_date, self.FORMAT_TIME_D_M_Y__h_m_s)
        # Xử lý ngày sinh
        date_y_m_d = datetime.strftime(
            dt_date, self.FORMAT_TIME_Y_M_D)
        return date_y_m_d

    def get_format_hours_minutes(hours=0, format=HOURS):
        """
        hours -> HH:MM
        minutes -> HH:MM
        seconds -> HH:MM

        """
        if hours is None:
            return 0

        if format == TimeHelper.HOURS:
            secs = hours * 3600
        if format == TimeHelper.SECONDS:
            secs = hours
        if format == TimeHelper.MINUTES:
            secs = hours * 60

        hours = secs // 3600
        minutes = secs // 60 - hours * 60
        return "%d:%02d" % (hours, minutes)

    @classmethod
    def get_format_full_to_MMDDThhmm(self, time) -> datetime:
        date, hour = time.split("T")
        hours, minutes = map(int, hour.split(':'))
        month, day = map(int, date.split('-'))
        now = datetime.utcnow()
        date_full = datetime(now.year, month, day, hours, minutes)
        return self.convert_str_form_time(date_full, self.FORMAT_TIME_D_M_Y__h_m_s)

    @classmethod
    def get_timezone(self, time, format, time_zone = None):
        # remove timezone nếu có
        remove_time_zone = time.replace(tzinfo=None)
        time_local = None
        # Thêm offset
        if time_zone is None:
            time_local = remove_time_zone + timedelta(minutes=self.TIME_OFFSET_MINUTES_UTC_7)
        else:
            time_local = remove_time_zone + timedelta(minutes=time_zone)
            
        # format về DD-MM-YY ...
        if format is None:
            format = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s

        # if 'T' in time:
        #     format = format.replace('T', ' ')

        date_now = datetime.strftime(time_local, format)
        return date_now

    @classmethod
    def get_all_timezone(self):
        return all_timezones

    @classmethod
    def format_str_to_time(self, str="", format=None):
        if format is None:
            format = self.FORMAT_TIME_Y_M_D__h_m_s_z
        time_raw = datetime.strptime(
            str, format)
        # format về DD-MM-YY ...
        format = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s
        # if 'T' in time:
        #     format = format.replace('T', ' ')

        date_now = datetime.strftime(
            time_raw, format)
        return date_now

    @classmethod
    def convert_time_vn(self, str="", formatIn=None, formatOut=None, time_zone = None):
        if formatIn is None:
            formatIn = self.FORMAT_TIME_Y_M_D__h_m_s_z
        time_raw = datetime.strptime(str, formatIn)
        if time_zone is None:
            time_new = self.get_timezone(time=time_raw, format=formatOut)
        else:
            time_new = self.get_timezone(time=time_raw, format=formatOut, time_zone = time_zone)
        
        return time_new

    @classmethod
    def convert_ddmmyyhhmmss_yymmddhhmmss(self, date_str, isUTC0=False):
        date_format = datetime.strptime(
            date_str, TimeHelper.FORMAT_TIME_D_M_Y__h_m_s)
        if isUTC0:
            time_local = date_format - \
                timedelta(minutes=self.TIME_OFFSET_MINUTES_UTC_7)
        else:
            time_local = date_format

        str_format = datetime.strftime(
            time_local, TimeHelper.FORMAT_TIME_Y_M_D_T_h_m_s)

        return str_format

    def get_calc_time(time_start=0):
        """
        - t1 = time.time()
        Check thời gian thực thi chương trình
        - TimeHelper.get_calc_time(time_start=t1)
        """
        result = "% 12.2f" % (t.time() - time_start)
        return str(result).strip()

    def get_date_time_to_db(str_time,format=None):
        """
        date_str -> COLUMS datetime database
        """
        if format is None:
            format = TimeHelper.FORMAT_TIME_D_M_Y__h_m_s
        if not str_time:
            return Null()
        return datetime.strptime(str_time, format) 
    
    @classmethod
    def convert_ngay_sinh_db(self,ngay_sinh,format=None):
        if format is None:
            format = self.FORMAT_TIME_FULL_Z
        str_ngay_sinh = datetime.strptime(ngay_sinh, format)
        ngay_sinh_new = datetime.strftime(str_ngay_sinh, TimeHelper.FORMAT_TIME_Y_M_D__h_m_s)
        return ngay_sinh_new

    @classmethod
    def time_distance_calculation(self, time_1, time_2, format):
        "Tính khoảng cách 2 điểm thời gian -> str H:M"
        date_1 = datetime.strptime(time_1,format)
        date_2 = datetime.strptime(time_2,format)
        time_1= str(date_1.day) +"-"+ str(date_1.month) +"-"+ str(date_1.year) +":"+ str(date_1.hour) + ":" + str(date_1.minute)
        time_2 = str(date_2.day) +"-"+ str(date_2.month) +"-"+ str(date_2.year) +":"+  str(date_2.hour)+ ":" + str(date_2.minute)
        FMT = '%d-%m-%Y:%H:%M'
        result_time = datetime.strptime(time_2, FMT) - datetime.strptime(time_1, FMT)
        result_time = datetime.strptime(str(result_time),TimeHelper.FORMAT_TIME_h_m_s)
        return result_time.strftime('%H:%M')
    
    def get_format_hours_minutes_of_vna(time_str):
        """
        hours -> HH:MM
        minutes -> HH:MM
        seconds -> HH:MM

        """
        if time_str is None:
            return 0

        hours = int(time_str.split(".")[0])
        minutes = int(time_str.split(".")[1])
        return "%d:%02d" % (hours, minutes)

    @classmethod
    def get_date_now_to_str_two(self):
        datetime_vi = datetime.now(time_zone_vi)
        return datetime_vi.strftime(self.FORMAT_TIME_FULL_Z)
    
    @classmethod
    def format_time(self, data, format_in, format_out):
        try:
            input = datetime.strptime(data, format_in)
            return datetime.strftime(input, format_out)
        except:
            return None
    
    def strfdelta(tdelta, fmt='{D:02}d {H:02}h {M:02}m {S:02}s', inputtype='timedelta'):
        """Convert a datetime.timedelta object or a regular number to a custom-
        formatted string, just like the stftime() method does for datetime.datetime
        objects.

        The fmt argument allows custom formatting to be specified.  Fields can 
        include seconds, minutes, hours, days, and weeks.  Each field is optional.

        Some examples:
            '{D:02}d {H:02}h {M:02}m {S:02}s' --> '05d 08h 04m 02s' (default)
            '{W}w {D}d {H}:{M:02}:{S:02}'     --> '4w 5d 8:04:02'
            '{D:2}d {H:2}:{M:02}:{S:02}'      --> ' 5d  8:04:02'
            '{H}h {S}s'                       --> '72h 800s'

        The inputtype argument allows tdelta to be a regular number instead of the  
        default, which is a datetime.timedelta object.  Valid inputtype strings: 
            's', 'seconds', 
            'm', 'minutes', 
            'h', 'hours', 
            'd', 'days', 
            'w', 'weeks'
        """

        # Convert tdelta to integer seconds.
        if inputtype == 'timedelta':
            remainder = int(tdelta.total_seconds())
        elif inputtype in ['s', 'seconds']:
            remainder = int(tdelta)
        elif inputtype in ['m', 'minutes']:
            remainder = int(tdelta)*60
        elif inputtype in ['h', 'hours']:
            remainder = int(tdelta)*3600
        elif inputtype in ['d', 'days']:
            remainder = int(tdelta)*86400
        elif inputtype in ['w', 'weeks']:
            remainder = int(tdelta)*604800

        f = Formatter()
        desired_fields = [field_tuple[1] for field_tuple in f.parse(fmt)]
        possible_fields = ('W', 'D', 'H', 'M', 'S')
        constants = {'W': 604800, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1}
        values = {}
        for field in possible_fields:
            if field in desired_fields and field in constants:
                values[field], remainder = divmod(remainder, constants[field])
        return f.format(fmt, **values)

            
