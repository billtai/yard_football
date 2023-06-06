class MessageHelper:
    CHECK_VN_CODE = " gồm chữ cái và số, không bao gồm ký tự đặt biệt"
    CHECK_REPLACE_MAIL_GD = 'Email giao dịch đã tồn tại',
    CHECK_REPLACE_MAIL_KT = 'Email kế toán đã tồn tại',
    NEED_CHANGE_PASSWORD = "Cần đổi mật khẩu trước khi đăng nhập"
    ACCOUNT_NAME_NOT_FOUND = "Tên đang nhập hoặc email đại lý không đúng",
    USER_NAME_NOT_FOUND = 'Tên đăng nhập không tồn tại'
    USER_NAME_DELETED = 'Tên đăng nhập không tồn tại'
    USER_NAME_INVALID = 'Tên đăng nhập không đúng'
    USER_NAME_EMPTY = 'Tên đăng nhập không được bỏ trống'
    PASS_WORD_EMPTY = 'Mật khẩu không được bỏ trống'
    PASS_WORD_INVALID = 'Mật khẩu không đúng'
    LOGOUT_SUCCESS = 'Đăng xuất thành công'
    REGISTER_SUCCESS = 'Đăng ký thành công'
    USER_EXIST = 'Tên đăng nhập đã tồn tại'
    AIRPORT_CODE_EXIST = 'Mã sân bay đã tồn tại'
    MATCH_PASS = 'Mật khẩu hiện tại không khớp'
    CHANGE_PASS_SUCCESS = 'Thay đổi mật khẩu thành công'
    REFRESH_SUCCESS = 'Làm mới token thành công'
    LOGIN_SUCCESS = 'Đăng nhập thành công'
    LOGOUTED = 'Tên đăng nhập đã đăng xuất'
    TOKEN_INVALID = 'Token không đúng'
    TOKEN_EXPIRES = 'Token hết hạn'
    TOKEN_LOGOUT = 'Token đã đăng xuất'
    ONLY_REFRESH = 'Chỉ cho phép refresh token'
    PHONE_EXIST = 'Số điện thoại đã tồn tại'
    EMAIL_EXIST = 'Email đã tồn tại'
    PAGE_EMPTY = 'Vui lòng nhập số trang'
    LIMIT_EMPTY = 'Vui lòng nhập số lượng trang'
    GET_LIST_SUCCESS = 'Lấy danh sách thành công'
    GET_LIST_FAIL = 'Lấy danh sách thất bại'
    ID_FOREIGN_DELETE = 'Không lấy được dữ liệu hoặc tham chiếu đã bị xóa'
    PAGE = 'Trang không đúng format'
    ITEM_PER_PAGE = 'Lấy không đúng format'
    UPDATE_FAILED = 'Cập nhật thất bại'
    UPDATE_SUCCESS = 'Cập nhật thành công'
    STATUS_EMTPY = 'Trạng thái không bỏ trống'
    STATUS_ACCEPT = 'Trạng thái chỉ chấp nhận 0 và 1'
    ID_NOT_FOUND = 'ID không tồn tại'
    DELETE_FAILED = 'Xóa thất bại'
    DELETE_SUCCESS = 'Xóa thành công'
    ID_DELETED = 'ID không tồn tại'
    NAME_AGENCY_EXIST = 'Tên đại lý đã tồn tại'
    CODE_AGENCY_EXIST = 'Mã đại lý đã tồn tại'
    UPDATE_NO_CHANGE = 'Không có thay đổi'
    ID_AGENCY_NO_FOUND = 'Đại lý không tồn tại'
    USER_NAME_BLOCK = 'Tên đăng nhập đã bị khóa'
    ORDER_A_Z_STATUS = 'Sắp xếp theo A-Z chỉ chấp nhận 0 và 1'
    NOT_FIELD_MODEL = 'Không tồn tại tên cột'
    ID_AGENCY_NO_FOUND_AND_DELETE = 'Đại lý không tồn tại'
    NAME_EXIST = 'Tên đã tồn tại'
    USER_NAME_EXIST = 'Tên đăng nhập đã tồn tại'
    DIEN_THOAI_EXIST = 'Số điện thoại đã tồn tại'
    EMAIL_EXIST = 'Email đã tồn tại'
    CODE_AGENCY_EXIST = 'Mã đại lý đã tồn tại'
    NAME_AGENCY_EXIST = 'Tên đại lý đã tồn tại'
    NO_GET_TOKEN = 'Không lấy được token'
    USER_NAME_NOT_INCLUDE_TOKEN = 'Không tồn tại tên đăng nhập từ token'
    INVALID_VIET_NAME = 'Số điện thoại không đúng định dạng đầu số việt nam'
    INVALID_PHONE_FORMAT = 'Số điện thoại không đúng định dạng'
    INVALID_EMAIL_FORMAT = 'Email không đúng định dạng'
    INVALID_PASSWORD = 'Mật khẩu tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ thường, một số và một ký tự đặc biệt'
    INVALID_USER_NAME_FORMAT = 'Tên đăng nhập không đúng định dạng'
    INVALID_USER_NAME_FORMAT_DOT = 'Tên đăng nhập không chứa dấu chấm kề nhau hoặc ở đầu và cuối'
    INVALID_CODE_FORMAT = 'Mã không đúng định dạng'
    INVALID_NAME_FORMAT = 'Tên không đúng định dạng'
    INVALID_FOREIGN_FORMAT = 'ID tham chiếu không đúng format'
    TYPE_FORGOT_FIELD = 'Loại chỉ chấp nhận email'
    TYPE_FORGOT_PHONE_FIELD = 'Chưa config OTP'
    EMAIL_NOT_FOUND_OR_NOT_EXIST = 'Email bị xóa hoặc không tồn tại'
    EMAIL_SEND_SUCCESS = 'Email đã được chuyển thành công'
    EMAIL_SEND_FAILED = 'Email chuyển thất bại'
    LENGTH_MIN = 'nhỏ nhất là'
    LENGTH_MAX = 'không vượt quá'
    LENGTH_EMTPY = ' không được nhập rỗng'
    INVALID_KEY = ' không đúng key'
    BOOLEAN_EMTPY = ' không bỏ trống'
    BOOLEAN_ACCEPT = ' chỉ chấp nhận 0 và 1'
    ADD_SUCCESS = 'Thêm thành công'
    ADD_FAIL = 'Thêm thất bại'
    ID_ADD_DUPLICATE = 'Sân bay trùng'
    ID_AIRPORT_DUPLICATE = 'Sân bay đi trùng với Sân bay đến'
    ID_AIRPORT_NOT_FOUND = 'Sân bay đi hoặc sân bay đến không tồn tại'
    INVALID_FOREIGN_FORMAT_VALIDATE = ' không đúng format'
    NAME_FIGHT_ROUTE_EXIST = 'Tên tuyến bay tồn tại'
    NAME_AREA_EXIST = 'Tên khu vực tồn tại'
    NAME_COUNTRY_EXIST = 'Tên quốc gia tồn tại'
    NAME_COUNTRY_NOT_EXIST = 'Tên quốc gia không tồn tại'
    ID_COUNTRY_DELETED = 'Quốc gia không tồn tại'
    ID_AREA_DELETED = 'Khu vực không tồn tại'
    NAME_PROVINCE_EXIST = 'Tên tỉnh tồn tại'
    ID_PROVINCE_DELETED = 'Tỉnh không tồn tại'
    ID_AIRPORT_GO_DELETED = 'Sân bay đi không tồn tại'
    ID_AIRPORT_ARRIVE_DELETED = 'Sân bay đến không tồn tại'
    NAME_AIRPORT_EXIST = 'Tên Sân bay đã tồn tại'
    NAME_AGENCY_OWNER_EXIST = 'Tên người đại diện đã tồn tại'
    ID_ROLE_NOT_FOUND = 'Vai trò không tồn tại'
    UN_AUTHORIZATION = 'Không xác thực'
    CHECK_TYPE_CUSTOMER = 'Đại lý đã có chủ đại lý'
    CHECK_ROLE = 'Không đủ quyền truy cập'

    @classmethod
    def message_join(self, field='', prop_message='', val='', after='ký tự'):
        msg = getattr(self, prop_message, None)
        if msg is None:
            msg = 'có lỗi xảy ra'
        return f'{field.capitalize()} {msg} {val} {after}'.strip()

    @classmethod
    def message_not_exists(self, field=''):
        return f'{field.capitalize()} không tồn tại'

    def message_range(self, field=''):
        return f'{self.capitalize()} không vượt quá {field}'

    @classmethod
    def message_not_action(self, field=''):
        return f'Không thể {field}'
    
    @classmethod
    def message_not_rename(self, field=''):
        return f'{field} không được đổi tên'
    @classmethod
    def message_free_custom(self, field=''):
        return f'{field}'
    @classmethod
    def message_not_match_exists(self, field='', field_check=''):
        return f'{field.capitalize()} không khớp {field_check.capitalize()}'

    @classmethod
    def message_exists(self, field=''):
        return f'{field.capitalize()} đã tồn tại'

    @classmethod
    def message_add_success(self, field=''):
        return f'Thêm {field.lower()} thành công'

    @classmethod
    def message_add_failed(self, field=''):
        return f'Thêm {field.lower()} thất bại'

    @classmethod
    def message_update_success(self, field=''):
        return f'Cập nhật {field.lower()} thành công'

    @classmethod
    def message_update_failed(self, field=''):
        return f'Cập nhật {field.lower()} thất bại'

    @classmethod
    def message_delete_success(self, field=''):
        return f'Xóa {field.lower()} thành công'


    
    @classmethod
    def message_delete_failed(self, field=''):
        return f'Xóa {field.lower()} thất bại'


    @classmethod
    def message_block_success(self, field=''):
        return f'Khóa {field.lower()} thành công'
    
    @classmethod
    def message_block_failed(self, field=''):
        return f'Khóa {field.lower()} thất bại'

    @classmethod
    def message_invalid_format(self, field=''):
        return f'{field.capitalize()} không đúng định dạng'

    @classmethod
    def message_custom(self, field='', message=''):
        if type(field) == list:
            return f'{"".join(field).capitalize()} {message}'.strip()
        return f'{field.capitalize()} {message}'.strip()

    @classmethod
    def message_get_success(self, field=''):
        return f'Lấy {field.lower()} thành công'

    @classmethod
    def message_get_expired(self, field=''):
        return f'{field.capitalize()} đã hết hạn'

    @classmethod
    def message_block(self, field=''):
        return f'{field.capitalize()} đã bị khóa'

    @classmethod
    def message_block_access(self, field=''):
        return f'{field.capitalize()} không thể truy cập'

    @classmethod
    def message_allow_access(self, field='', allow_message=''):
        return f'{field.capitalize()} chỉ chấp nhận {allow_message}'

    @classmethod
    def message_access_success(self, field=''):
        return f'{field.capitalize()} thành công'

    @classmethod
    def message_access_failed(self, field=''):
        return f'{field.capitalize()} thất bại'

    @classmethod
    def message_auth_failed(self, field=''):
        return f'{field.capitalize()} không thể xác thực'

    @classmethod
    def message_handle_data_failed(self, field=''):
        return f'Xử lý dữ liệu {field.lower()} thất bại'

    @classmethod
    def message_emtpy(self, field=''):
        return f'{field.capitalize()} không được bỏ trống'

    @classmethod
    def message_different(self, field=''):
        return f'{field.capitalize()} phải khác nhau'


dictory_field = {
    'ten_dang_nhap': 'Tên đăng nhập',
    'mat_khau': 'Mật khẩu',
    'ten': 'Tên',
    'ma_dai_ly': 'Mã đại lý',
    'trang_thai': 'Trạng thái',
    'dai_ly_id': 'Đại lý',
    'loai_nhan_vien_id': 'Loại nhân viên',
    'mat_khau_cu': 'Mật khẩu cũ',
    'mat_khau_moi': 'Mật khẩu mới',
    'type': 'Loại',
    'value': 'Giá trị',
    'san_bay_di_id': 'Sân bay đi',
    'san_bay_den_id': 'Sân bay đến',
    'khu_vuc_id': 'Khu vực',
    'quoc_gia_id': 'Quốc gia',
}


def get_message_translate(message=''):
    if 'is too short' in message:
        return 'không được bỏ trống'
    if 'is too long' in message:
        return 'quá dài'
    if 'is not of type' in message:
        return 'không đúng kiểu dữ liệu'

    return message


class TranslateMessageHelper:
    def message_to_vi(fields='', message=''):
        msg = ""
        fds = ""
        if len(fields) > 0:
            fds = dictory_field[fields] if fields in dictory_field else fields
        msg = get_message_translate(message)
        if 'in an uploaded file' in message:
            return 'Vui lòng chọn ảnh'
        return fds + " " + msg