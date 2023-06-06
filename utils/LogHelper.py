import json
import os
from utils.urlHelper import URLHelper
import pandas as pd
from datetime import date, datetime
from mongo_logs.airline_log import AirlineLog

class LogHelper:
    path_dir = os.getcwd()
    @classmethod
    def model_array_to_data_frame(self, array_model: dict):
        return pd.DataFrame([row.__dict__ for row in array_model])

    @classmethod
    def model_to_dict(self, model):
        return model.__dict__

    @classmethod
    def to_json_to_file_log(self, _json={}, ten_file='log.json', is_json=False):
        """
        Viết ra file nếu json quá dài không log nổi trên terminal
        """
        path = os.path.join('write_log_local', ten_file)

        # Check Folder nếu chưa có thì tạo
        folder_upload = 'write_log_local'
        path_folder = os.path.join(self.path_dir, folder_upload)
        if not os.path.exists(path_folder):
            os.makedirs(path_folder)

        if is_json:
            _json = json.loads(_json)
        with open(path, 'wt', encoding='utf-8') as f:
            json.dump(_json, f, ensure_ascii=False, indent=4)
            print("In File: to_json_to_file_log", "=== ĐÃ WRITE ===")

        # Closing file
        f.close()

    @classmethod
    def write_file(self, data):
        with open('xml_to_json.xml', 'wt', encoding='utf-8') as f:
            print("In File: test_json.py, write_file", "===ĐÃ WRITE===")
            # f.write(data)
            f.write(data)

        # Closing file
        f.close()

    @classmethod
    def get_file_log(self,name, folder='write_log_local'):
        f = open(os.path.join(self.path_dir,os.path.join(folder, name)))
        data = json.load(f)
        return data
    
    @classmethod
    def save_request(self,url, data):
        folder_upload = 'logs\\req'
        path = os.path.join(URLHelper.path_dir, folder_upload)
        if not os.path.exists(path):
            os.makedirs(path)
        today = date.today()
        now = today.strftime("%d%m%Y")
        ten_file =  "rq_vj" + now +".txt"
        path_req = os.path.join(path, ten_file)
        if not os.path.exists(path_req):
            with open(path_req, 'w') as f:
                f.write("")
        f = open(path_req, "a")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data_write = "\n\n-----Data "+dt_string+"------"\
            "\n\turl:"+ str(url)+\
            "\n\tdata_req: " + str(data)
        f.write(data_write)
        f.close()
        
    @classmethod
    def save_response(self, url, status_code, data):
        folder_upload = 'logs\\res'
        path = os.path.join(URLHelper.path_dir, folder_upload)
        if not os.path.exists(path):
            os.makedirs(path)
        today = date.today()
        now = today.strftime("%d%m%Y")
        ten_file =  "rs_vj" + now +".txt"
        path_req = os.path.join(path, ten_file)
        if not os.path.exists(path_req):
            with open(path_req, 'w', encoding="utf-8") as f:
                f.write("")
        f = open(path_req, "a")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data_write = "\n\n-----Data "+dt_string+"------"\
            "\n\turl:"+ str(url)+\
            "\n\tstatus code:"+ str(status_code)+\
            "\n\tdata_res: " + str(data)
        f.write(data_write)
        f.close()

    @classmethod
    def save_mongo_log(self, url, airline, service, content, rtype = "request", status = None, request_id = None, username = None, ip = None):
        req_log = AirlineLog(
            ten_dang_nhap = username,
            ip = ip,
            url = url,
            hang = airline,
            loai = rtype,
            status_code = status,
            request_id = request_id,
            service = service,
            noi_dung = content,
            created_at = datetime.now()
        )
        req_log.save()
        return str(req_log.id)
        
class TacVuHelper:
    TACH_PNR        = "Devide"
    PNR_HISTORY     = "Pnr History"
    HUY_VE          = "Refund"
    VOID            = "Void"
    DAT_VE          = "Book"
    THONG_TIN_VE    = "Open/view"
    THANH_TOAN      = "Payment"
    DONG_BO_DU_LIEU = "Data synchronization"
    DANG_NHAP       = "Login"
    TIM_VE_NGOAI_HE_THONG   = "Find pnr outside the system"
    CAP_NHAT_HANH_KHACH     = "Change name"
    CAP_NHAT_DICH_VU        = "Add services"
    CAP_NHAT_HANH_TRINH     = "Change itinerary"
    