from datetime import datetime
from enum import auto
import time
from string import Formatter

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

            
