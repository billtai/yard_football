class DescriptionSwagger:
    """
    Gôm các mô tả swagger

    """
    @classmethod
    def get_ct_cs_description(self):
        return """
        `ten_hang_nay*: max:255`
        `ten_nha_cung_cap*:  max:255`
        """

    @classmethod
    def get_dl_description(self):
        return """
        `ten_dai_ly*: max:255`
        `ma_dai_ly*:  max:20`
        `nhan_vien_quan_ly_id*: mã nhân viên TH`
        `ten_chu_dai_ly*: max:50`
        `ten_dang_nhap*: max:50`
        `gioi_tinh*: 1:Nam , 2 Nữ`
        `mat_khau*:max:50`
        `email*:max:255`
        `dien_thoai*:max:20`
        `sdt_dai_ly*: max:20`
        `danh_sach_sdt*: max20`
        `email_ke_toan*: max255`
        `email_giao_dich* : ma255`
        `Loai_han_muc: 0: không hạn mức, 1: tính theo lũy kế, 2: hạn mức bảo lãnh`
        """

    @classmethod
    def get_dl_edit_description(self):
        return """
        `ten_dai_ly_edit: max:255`
        `email_1_edit:  max:20`
        `email_2_edit: mã nhân viên TH`
        `sdt_edit:max:20`
        `dia_chi_edit : max:255`
        """
    
    @classmethod
    def get_hb_description(self):
        return """
        `ten_hang_bay*: max:255`
        `ma_hang_bay*:  max:20`
        `ten_tat: max:20 là IATA https://vietmoon-travel.com/bang-ma-viet-tat-cac-hang-hang-khong.html`
        `logo:  max:2000`
        """
    
    @classmethod
    def get_chinh_sach_description(self):
        return """
        `ten_chinh_sach: max:255`
        `tap_tin: tập tin`
        """
    
    @classmethod
    def get_thong_bao_description(self):
        return """
        `tieu_de: tieu de`
        `noi_dung: noi dung`
        `hinh_anh: hinh anh`
        """


    @classmethod
    def get_tb_description(self):
        return """
        `san_bay_di*:`
        `san_bay_den*: (Không được trùng sân bay đi)`
        `hai_chieu: 0 (mặc định 1 chiều) | 1 (hai chiều)`
        """

    @classmethod
    def get_upload_image(self):
        return """
        `file:*`
        `Vui lòng test bằng postman`

        """

    @classmethod
    def get_dat_ve_description(self):
        return """
            `tổng hành khách : nguoi_lon + tre_em <= 9`
            `số em bé: em_be <= nguoi_lon`
            ` *ma_dat_cho : lấy từ API tìm vé `
            ` *loai_hanh_khach: 1: người lớn, 2: trẻ em.`
            ` *gioi_tinh: 1: nam, 2: nữ`
            ` *hanh_khach_id: hành khách một id: 1 hành khách hai id: 2`
            ` ngay_sinh: người lớn có thể có hoặc không(ngay_sinh=""),* trẻ em bắt buộc phải có ngày sinh`
            ` em_be: nếu không có em bé không cần truyền hoặc truyền = []`
            ` cho_ngoi = [] | tt_dat_cho = {} | tt_thanh_toan = [] | tien_t = []`
            `____________`
            `1. Phải có mã đặt chỗ`
            `2. Ghế phải có sẵn ["co_san": true] `
            `3. Phụ trợ có thể trùng hành khách nhưng phải đúng theo chiều hanh_trinh_id`
            `4. Booking nhiều hành khách, thì nhớ thêm id hành khách vào id hành khách trong hành trình, như mẫu bên dưới`
            `5. Chú ý phần thời gian giữ vé -> khi hết thời gian vé sẽ tự động hủy`
            `6. Khi thanh toán vé rồi sẽ không còn thời gian giữ vé`.
            `7. Nếu có thêm bảo hiểm và thì nó sẽ thanh toán luôn(thoi_gian_giu_ve:null) chứ không còn giữ chỗ nữa.`
            `8. Mã đặt chỗ 1 chiều/ khứ hồi có thể khác nhau các hạng vé.`
            `9. Province VJ CODE: https://uat-vietjetapi.vietjetair.com/api/countries/VNM/provinces`
            `10. ma_dat_cho từ API tìm vé nó có time nên nó có khi sẽ expires nên phải lấy lại mã booking mới.`
            `11. BookingKey phải đúng với số lượng hành khách nhập vào: VD: tìm vé có em bé -> khi đặt chỗ cũng phải điền thông tin em bé nếu không sẽ không có data`
            `______`
            `Danh xưng`
            `Ông 	1`
            `Bà 	2`
            `Cô 	3`
            `Em trai	4`
            `Em gái	5`
            `Bé trai	6`
            `Bé gái	7`
            `Loại hành khách`
            `Người lớn	1`
            `Trẻ em 	2`
            `Em bé (db.em_be)`
            `Hành khách (db.hành khách) (người lớn, trẻ em)`

            `______`
            `____________`

            `____________`
            `-------Ví dụ booking 2 chiều thì mẫu:-------`
            `Phần hành trình:[
            {
                "hanh_khach": [
                    {"hanh_khach_id":1,"ma_dat_cho": "Mã booking 1 chiều",},
                    {"hanh_khach_id":2,"ma_dat_cho": "Mã booking 1 chiều",}
                ]
               },
               {
                "hanh_khach": [
                    {"hanh_khach_id":1, "ma_dat_cho": "Mã booking 2 chiều",},
                    {"hanh_khach_id":2, "ma_dat_cho": "Mã booking 2 chiều",}
                ]
               }
            ]
            `-------Nếu như booking nhiều hành khách thì mẫu-------:
            "hanh_khach":[
                {},
                {},
            ],
            "hanh_trinh":[
                "hanh_khach":[
                    {"hanh_khach_id":1,"ma_dat_cho": 'Mã booking 1 chiều'},
                    {"hanh_khach_id":2,"ma_dat_cho": 'Mã booking 1 chiều'}
                ],
            ]

            `
        """

    @classmethod
    def get_ma_dat_cho_description(self):
        return """
        `ma_dat_cho: lấy từ API tìm vé`
        `nhớ check xem package đó đã mua chưa: ("co_san": true)`
        `phi_cho_ngoi: nếu vé YPPass2 tiền sẽ = 0`
        `phụ trợ group theo nhóm lại`
        """

    @classmethod
    def get_ma_dat_cho_dat_ve_description(self):
        return """
        `ma_dat_cho: lấy từ API đặt vé`
        
        """

    @classmethod
    def get_ma_pnr_dat_ve_description(self):
        return """
        `ma_pnr: lấy từ API đặt vé`
        
        """

    @classmethod
    def get_ma_dat_ve_dat_ve_description(self):
        return """
        `ma_dat_cho: lấy từ API đặt chỗ`
        
        """

    @classmethod
    def get_dc_description(self):
        return """
        ``
        
        """

    @classmethod
    def get_tim_ve_description(self):
        return """
        `diem_di | diem_den: dựa theo mã (ICAO/IATA) không được trùng nhau`
        `ngay_di: lớn hơn >= now | mặc định: now | một chiều` 
        `ngay_ve: lớn hơn ngày về | bắt buộc nhập ngày đi | khứ hồi ` 
        `tổng hành khách : nguoi_lon + tre_em = 10`
        `số em bé: em_be <= nguoi_lon`
        `hang_ve: Y: economic , C: Bussiness... mặc định: Y`
        `ma_khuyen_mai: ...`
        `loai_tien: VND | USD ... | mặc định: VND (Hiện tại chỉ web mình chỉ dùng VND) `

        `____`
        - Các phần phí vé sẽ được lấy từ phần vé máy bay khi tìm, theo một chiều hoặc khứ hồi.
        `____`
       
        - Các mã code sân bay IATA VJ hỗ trợ. 
         https://uat-vietjetapi.vietjetair.com/api/Airports?applicabilityDescriptor=All&includeInactive=true
        `____`
        - Danh sách cabinClass VJ hỗ trợ
         https://uat-vietjetapi.vietjetair.com/api/CabinClasses
        `____`
        """

    @classmethod
    def get_tinh_phi_giao_dich_description(self):
        """
        - Lưu ý: mã tiền tệ trong Giao dịch thanh toán [] phải giống với đơn vị tiền tệ đặt trước.
        - Tất cả trạng thái tính phí 'hiện đang hoạt động: true, đang chờ xử lý: true. Các khoản phí đang chờ xử lý vì chúng chưa được thêm vào đặt phòng.
        - Khi đặt phòng đã được thực hiện, các khoản phí sẽ hiển thị là đang hoạt động: true, pending: false.
        - response: Lưu ý PaymentTransactions.currencyAmounts.totalAmount Thêm tổng số tiền vào phần giao dịch thanh toán của thanh toán POS
        """

        return """
           ` - Sử dụng cho cập nhật`
           ` - Bắt buộc booking này phải thanh toán rồi.`

        """

    @classmethod
    def get_tinh_phi_truoc_dat_cho_description(self):
        """ """

        return """
        `- Cập nhật hành khách:`
        `- hanh khách: mot_chieu/hanh_khach cần truyền`
        `- Cập nhật hành trình`
        `- hanh trình: mot_chieu/phi_ve cần truyền`
        `- Khả năng áp dụng: nguoi_lon: true, tre_em:true em_be:false [quy về cho người lớn]`
        `- Khả năng áp dụng: nguoi_lon: false, tre_em:true em_be:false [quy về cho trẻ em]`
        `- Khả năng áp dụng: nguoi_lon: false, tre_em:false em_be:true [quy về cho em bé]`
        `- Phi chỗ ngồi:`
        `- hanh_khach_ap_dung: nếu phí chỗ ngồi -> null`
        `- mota trong phụ phí của BAMBOO thì để là phu_phi cho các dịch vụ khách đặt thêm`
        `- mota trong phụ phí của BAMBOO thì để là SEAT cho chỗ ngồi`
        `- Request`
        `  + is_save:False(Không lưu lại) -> Khi kết thúc đặt vé thì cho is_save:True(Lưu lại)`
        """

    @classmethod
    def get_cap_nhat_hanh_trinh_description(self):
        return """
        `Báo giá sẽ được lấy khi tìm kiếm hành trình mới.`
        `request:`
        `- hanh_trinh_id: mã hành trình cũ`
        `- dat_cho_id: mã đặt chỗ cũ`
        `payload:`
        `- ma_dat_cho: mã đặt chỗ mới.`
        """

    @classmethod
    def get_them_phu_tro_dat_ve_description(self):
        return """
        `payload:`
        `+ ma_dat_cho: mã đặt chỗ lấy từ api chi tiết ma_dat_cho`
            `- khoa_phu_tro: khóa phụ trợ  mới lấy api danh sách phụ trợ khoa_phu_tro`
            `- ma_hanh_khach: mã hành khách lấy api chi tiết đặt chỗ hanh_khach/[]ma_hanh_khach`
            `- ma_hanh_trinh: mã hành trình lấy api chi tiết đặt chỗ hanh_trinh/[]ma_hanh_trinh`
        """

    @classmethod
    def get_them_cho_ngoi_dat_ve_description(self):
        return """
        `payload:`
        `+ ma_dat_cho: mã đặt chỗ lấy từ api chi tiết ma_dat_cho`
            `- khoa_cho_ngoi: khóa chỗ ngồi mới lấy api danh sách chỗ ngồi khoa_cho_ngoi`
            `- ma_hanh_khach: mã hành khách lấy api chi tiết đặt chỗ hanh_khach/[]ma_hanh_khach`
            `- ma_hanh_trinh: mã hành trình lấy api chi tiết đặt chỗ hanh_trinh/[]ma_hanh_trinh`
            `- ma_phan_khuc: mã phân khúc lấy api chi tiết đặt chỗ từ hanh_trinh/[]phan_khuc/ma_phan_khuc`
        """

    @classmethod
    def get_them_bao_hiem_dat_ve_description(self):
        return """
        `payload:`
        `+ ma_dat_cho: mã đặt chỗ lấy từ api chi tiết ma_dat_cho`
            `- khoa_bao_hiem: khóa bảo hiểm mới lấy api danh sách bảo hiểm khoa_bao_hiem`
            `- tong_tien: tổng tiền bảo hiểm`
           
        """

    @classmethod
    def get_tim_ve_hanh_trinh_description(self):
        """ """
        return """
        `diem_di | diem_den: dựa theo mã (ICAO/IATA) không được trùng nhau`
        `ngay_di: lớn hơn >= now | mặc định: now | một chiều` 
        `hang_ve: ... mặc định: Y`
        `*dat_cho_id: lấy từ API ds đặt chỗ`
        `hanh_trinh_id: lấy từ API ds đặt chỗ/ hành trình`
        `lưu ý: không điền hành trình id thì sẽ lấy danh sách chặng bay dùng cho thêm chặng`
        """

    @classmethod
    def get_dat_ve_cap_nhat_hanh_khach_description(self):
        return """
        `Cập nhật trước hoặc sau khi thanh toán điều được`
        `*dat_cho_id:`
        `*hanh_khach_id:`
        `request:`
        `- Nếu không cập nhật em bé thì em_be = []`
        `- Call API cập nhật -> is_bao_gia:True (Lấy phí báo giá)-> call API cập nhật tính giá trước đặt chỗ(Cập nhật lại thông tin cho cái bảng thanh toán) -> call api cập nhật is_bao_gia:false (Cập nhật lên hãng).`
        """

    @classmethod
    def get_hop_dong_bao_hiem_description(self):
        return """
        `Cần truyền lại form đặt vé cho API bảo hiểm`
        """

    @classmethod
    def get_chi_tiet_tim_ve_description(self):
        return """
        `ma_du_lich: lấy từ API tìm vé`
        `ma_dat_cho: Lấy từ API tìm vé`
        """

    @classmethod
    def get_xuat_ve_description(self):
        """
        - Điểm cuối Báo giá sẽ trả lại tất cả các khoản phí áp dụng cho đặt phòng.
        - Ở cuối phản hồi, tổng số tiền sẽ được trả lại theo payTransactions.currencyAmounts.totalAmount.
        - Thêm tổng số tiền vào phần giao dịch thanh toán của yêu cầu hành khách POST.
        - Đây sẽ là số tiền được gửi cùng với hành khách POST
        ____ Chú ý____
        - Có thể thanh toán nhiều lần: paymentTransactions:[{lần 1},{lần 2},...] đến khi phần currencyAmounts[0].totalAmount: = 0 thì
        thêm thanh toán tiếp nó sẽ không trừ tiền đại lý nữa và không có cộng vào payment Transaction.
        - Trước khi thanh toán phải check qua API: calculateTransactionFee -> Nó sẽ paymentTransactions:[]
        ______Các thanh toán________________
        `call API: /reservationLocator="" -> check balance`
        `- charge.totalAmount - payment.totalAmount`
        `- if balance = 0 Đã thanh toán đủ`
        `- if balance < 0 Hầu như không rơi vào trường hợp này`
        `- if balance > 0 Phải thanh toán tiếp cho đến khi nó = 0`
        """
        return """
        `- thoi_gian_giu_ve: null -> PNR active`
        `- loai_thanh_toan: PL : paylater , AG: Agency Credit`
        `PL: giữ chỗ -> charge vẫn còn/ thời gian giữ vé vẫn còn) -> khi thanh toán thì về bảng đặt chỗ thanh toán sau -> (0)`
        `AG: thoi_gian_giu_ve:null -> giữ chỗ -> charge về 0 và số tiền đại lý trừ tiền xuống -> chuyến trạng thái sang đã xuất (1)`
        `xac_nhan: y -> thanh toán, '' -> hiện message`
        `Lưu ý: Vé "YPPass2" không thanh toán được -> lý do chưa tìm ra : (Payment attempt failed res validation. RES #106344161 METHOD 5 AmeliaFlexiRes/CResParser/FlexiAddResPayment (-6977))`
        `- Trạng thái:  GIU_CHO = 0
                        DA_XUAT = 1
                        HUY_DI_XUAT_VE = 2
                        HUY_VE_XUAT_DI = 3
                        DA_HUY = 4
        `
        """

    @classmethod
    def get_ds_dc_description(self):
        return """
        `sap_xep: ma_dat_cho,ma_pnr,ma_dat_cho,ma_pnr,ho,ten,ma_hang_khong,so_chuyen_bay,`
        `san_bay_di,hang_bay,so_ghe,ngay_bay,ngay_tao_dat_cho,trang_thai,ten_day_du,ten_nhan_vien,ten_dai_ly`
        `ten_nguoi_dai_dien`
        `asc: 1: tăng dần (asc default) | 0 giảm dần (desc)`
        `Response:`
        `- Trạng thái:  GIU_CHO = HOLD
                        DA_XUAT = PAID
                        HUY_DI_XUAT_VE = None
                        HUY_VE_XUAT_DI = None
                        DA_HUY = None
        `

        """

    @classmethod
    def get_bao_gia_hanh_khach_description(self):
        return """
        `Báo giá sau khi sửa hành khách /thêm/sửa em bé`
        `*ma_dat_cho:`
        `*ma_hanh_khach:`
        """

    @classmethod
    def get_bao_gia_hanh_trinh_description(self):
        return """
        `Báo giá sau khi sửa hành trình`
        `*ma_dat_cho:`
        `*ma_hanh_trinh:`
        """

    @classmethod
    def get_them_chang_description(self):
        return """
        `Thêm chặng`
        `*ma_dat_cho:`
        `*ma_hanh_trinh:`
        """

    @classmethod
    def get_th_dat_ve_description(self):
        return """
            `CÁC TRƯỜNG BẮT BUỘC THEO TỪNG HÃNG SẼ CÓ TÊN TRƯỚC VD: BB_hanh_trinh là dùng cho BamBoo nếu cho VJ thì BB_hanh_trinh = []`
            `tổng hành khách : nguoi_lon + tre_em <= 9`
            `số em bé: em_be <= nguoi_lon`
            ` *ma_dat_cho : lấy từ API tìm vé `
            ` *loai_hanh_khach: 1: người lớn, 2: trẻ em.`
            ` *gioi_tinh: 1: nam, 2: nữ`
            ` *hanh_khach_id: hành khách một id: 1 hành khách hai id: 2`
            ` ngay_sinh: người lớn có thể có hoặc không(ngay_sinh=""),* trẻ em bắt buộc phải có ngày sinh`
            ` em_be: nếu không có em bé không cần truyền hoặc truyền = []`
            ` cho_ngoi = [] | tt_dat_cho = {} | tt_thanh_toan = [] | tien_t = []`
            `____________`
            `1. Phải có mã đặt chỗ - cho đặt vé vj`
            `2. Ghế phải có sẵn ["co_san": true] `
            `3. Phụ trợ có thể trùng hành khách nhưng phải đúng theo chiều hanh_trinh_id`
            `4. Booking nhiều hành khách, thì nhớ thêm id hành khách vào id hành khách trong hành trình, như mẫu bên dưới`
            `5. Chú ý phần thời gian giữ vé -> khi hết thời gian vé sẽ tự động hủy`
            `6. Khi thanh toán vé rồi sẽ không còn thời gian giữ vé`.
            `7. Nếu có thêm bảo hiểm và thì nó sẽ thanh toán luôn(thoi_gian_giu_ve:null) chứ không còn giữ chỗ nữa.`
            `8. Mã đặt chỗ 1 chiều/ khứ hồi có thể khác nhau các hạng vé.`
            `9. Province VJ CODE: https://uat-vietjetapi.vietjetair.com/api/countries/VNM/provinces`
            `10. ma_dat_cho từ API tìm vé nó có time nên nó có khi sẽ expires nên phải lấy lại mã booking mới.`
            `11. BookingKey phải đúng với số lượng hành khách nhập vào: VD: tìm vé có em bé -> khi đặt chỗ cũng phải điền thông tin em bé nếu không sẽ không có data`
            `______`
            `Danh xưng`
            `Ông 	1`
            `Bà 	2`
            `Cô 	3`
            `Em trai	4`
            `Em gái	6`
            `Bé trai	7`
            `Bé gái	8`
            `Loại hành khách`
            `Người lớn	1`
            `Trẻ em 	2`
            `Em bé (db.em_be)`
            `Hành khách (db.hành khách) (người lớn, trẻ em)`
        """

class DescriptionSwaggerVN:
    @classmethod
    def get_tim_ve_description(self):
        return f"""
        `(2) Tìm vé`
        `tổng hành khách : nguoi_lon + tre_em <= 9`
        `diem_di | diem_den: dựa theo mã (ICAO/IATA) không được trùng nhau`
        `ngay_di: lớn hơn >= now | mặc định: now | một chiều` 
        `ngay_ve: lớn hơn ngày về | bắt buộc nhập ngày đi | khứ hồi ` 
        `nguoi_lon: 1-> 9`
        `tre_em: 0-> 9`
        """

    @classmethod
    def get_dat_ve_description(self):
        return """
            `Vui lòng gọi api tính phí vé trước khi gọi api đặt vé`
            `(5) Thêm hành khách vào session`
            `tổng hành khách : nguoi_lon + tre_em <= 9`
            `số em bé: em_be <= nguoi_lon`
            ` *ma_dat_cho : lấy từ API tìm vé `
            ` *loai_hanh_khach: 1: người lớn, 2: trẻ em.`
            ` *gioi_tinh: 1: nam, 2: nữ`
            ` *hanh_khach_id: hành khách một id: 1 hành khách hai id: 2`
            ` ngay_sinh: người lớn có thể có hoặc không(ngay_sinh=""),* trẻ em bắt buộc phải có ngày sinh`
            ` em_be: nếu không có em bé không cần truyền hoặc truyền = []`
            `____________`
            Response:
            - RPH: nó như ID dùng nó để tìm hành khách: VD: Phone RPH của phone = RPH của customer
            `____________`
            `Thêm Em bé hiện tại đang hold* lại xử lý sau`.
            `Tên không được nhập số`
            `
        """

    @classmethod
    def get_chi_tiet_ve_description(self):
        return """
        `(6) Lấy PNR`
        """

    @classmethod
    def get_tinh_gia_ve_description(self):
        return """
        `(4) Tính giá vé`
        - Response:
        - Tổng tiền sau thuế: tổng thuế + tổng vé
        - Tổng số tiền vế: (2 tổng tiền vé cả chiều + 2 hành khách) * 2
        - Thành tiền (Số tiền final): Tổng vé + và tổng phí + tổng chiều chuyến bay
        - Chi tiết:
        `https://www.vietnamairlines.com/vn/vi/destinations/thanh-pho-ho-chi-minh`
        `* Tính giá có thêm em bé hiện tại đang lỗi`
        """

    @classmethod
    def get_book_ve_description(self):
        return """
        `(3) Book hành trình`
        `- One Way: {"hanh_trinh":[{}]}"`
        `- Two Way: {"hanh_trinh":[{},{}]}"`
        """

    @classmethod
    def get_xac_thuc_description(self):
        return """
        `(1) Tạo session`
        `- session tồn tại trong 10p hết session hủy phiên giao dịch`
        """

    @classmethod
    def get_thanh_toan_description(self):
        return """
        `(7) Thanh toán đặt chỗ và kết thúc session`
        """

    @classmethod
    def get_phu_tro_description(self):
        return """
        `Phụ trợ`
        - Do nhập nhiều field nên dùng POST thay vì dùng GET để lấy ds bên hãng.
        """
    
    @classmethod
    def get_void_ticketing_description(self):
        return """
        `(1) Tạo session`
        `- session tồn tại trong 10p hết session hủy phiên giao dịch`
        """

    @classmethod
    def get_huy_ve_description(self):
        return """
        `dat_cho_id: lấy từ API ql đặt chỗ`
        `ma_hang_bay: Lấy mã IATA`
        `xac_nhan: y hủy luôn`
        """


class DescriptionSwaggerGeneral:
    @classmethod
    def get_tim_ve_description(self):
        return """
        `diem_di | diem_den: dựa theo mã (IATA) không được trùng nhau`
        `ngay_di: lớn hơn >= ngày hiện tại | mặc định: ngày hiện tại | một chiều` 
        `ngay_ve: lớn hơn ngày về | bắt buộc nhập ngày đi | khứ hồi ` 
        `loai_dinh_dang: 1 -> 1 chuyến bay nhiều dòng_ theo hạng chỗ(default) | 2-> 1 chuyến bay 1 dòng_ theo chuyến bay`
        `nguoi_lon + tre_em  <= 9`
        `em_be = nguoi_lon`
        `sap_xep: `
        ` - so_hieu_chuyen_bay(nó sẽ sắp xếp theo số hiệu chuyến bay),ten_hang_bay(A->Z),tong_thoi_gian_bay(HH:MM),ngay_di(mặc định),ngay_den`
        ` - gia_ve (nếu là giá chưa tính thuế + phí),`
        ` - tong_cong (đã tính thuế + phí),`
        ` - so_ghe_trong:(Sắp theo ghế)
        `asc: sắp xếp theo ngày đi default 1: tăng dần, 0 giảm dần`

        ---- response---
        `[1 tuyến bay gồm rất nhiều chặng bay] nhưng điều chung 1 giá vé`
        `tổng thời gian bay: (điểm đến - điểm đi)(tất cả chặng bay)`
        `thời gian bay: thời gian bay của từng chuyến(theo 1 chặng bay)`
        `gia_tien_co_ban: dùng đổ lên list. (Chưa thuế gia_ve đổ lên | Đã có thế lấy tong_tien)`
        `gia_tien: dùng đổ lên thông tin vé bên phải. (Chưa thuế gia_ve đổ lên | Đã có thế lấy tong_tien)`
        `phi_ve: dùng đổ lên list chi tiết trước khi xuất vé`
        """

class DescriptionSwaggerBB:
    @classmethod
    def bb_xac_nhan_gia_ve_description(self):
        return """
        `https://documenter.getpostman.com/view/4267803/TVmMfxDL#b3932de3-6766-45fd-b5a3-9169691ab392`
        `----------------------------------------------------------------------------------`
        `Dịch vụ thêm hành lý hoặc mua phụ trợ thêm vào request mảng tt_dich_vu_mua`
        "tt_dich_vu_mua": [
            {
            "ma_dich_vu": "VOUC|PRCI|INSR|XBAG" Mã dịch vụ: PRCI(Ưu tiên checkin và boarding); VOUC(Phòng chờ thương gia); INSR(Bảo hiểm); XBAG(Hành lý); 
            (lấy dữ liệu: dich_vu_phu_tro/danh_sach_phu_tro#ma_dich_vu),
            "ghi_chu": "comment",
            `"so_kg: 12/20/... nếu mã là XBAG thì phải có không thì xóa bỏ khỏi request`
            "id_chang_bay": 1, nếu là nối chặng thì lấy mã segment id chặng xuất phát
            "id_khach": 1,
            }
        ]`
        """

    @classmethod
    def bb_dat_ve_description(self):
        return """
        `is_through_flight lấy dữ liệu từ tim-ve#stops nếu stops == 1 -> is_through_flight = true; nếu không có điền false `
        `----------------------------------------------------------------------------------`
        `tt_hanh_khach:`
        'Ngày sinh của hành khách: đối với hành khách là trẻ em hoặc em bé bắt buộc phải điền ngày sinh'
        'Nhóm hành khách: mỗi gia đình là 1 Id duy nhất; nhom_hanh_khach > 0'
        'id_cua_cha_me bắt buộc đối với hành khách là em bé(INFANT) và giá trị của trường này phải là id_hanh_khach của hành khách người lớn(ADULT) mà em bé(INFANT) được liên kết.'
        `----------------------------------------------------------------------------------`
        `tt_thanh_toan[][id_hanh_khach] - lấy dự liệu từ xac_nhan_gia_ve#tong_tien_phai_tra#tien_khach_phai_tra#id_khach`
        `tt_thanh_toan[][so_tien] - lấy dự liệu từ xac_nhan_gia_ve#tong_tien_phai_tra#tien_khach_phai_tra#so_tien`
        `tt_thanh_toan[][loai_tien] - lấy dự liệu từ xac_nhan_gia_ve#tong_tien_phai_tra#tien_te`
        `Dịch vụ chọn ghế thêm vào request mảng tt_ghe_chon_mua`
        - so_ghe_chon lấy từ dịch vụ chọn chỗ ngồi #chi_tiet_so_do_cho_ngoi#chi_tiet_boong#chi_tiet_cabin#chi_tiet_khoang#chi_tiet_ghe#so_ghe
          với thuoc_tinh_kiem_tra = Available
        `https://documenter.getpostman.com/view/4267803/TVmMfxDL#b3932de3-6766-45fd-b5a3-9169691ab392`
        `----------------------------------------------------------------------------------`
        `Dịch vụ thêm hành lý hoặc mua phụ trợ thêm vào request mảng tt_dich_vu_mua`
        "tt_dich_vu_mua": [
            {
            "ma_dich_vu": "VOUC|PRCI|INSR|XBAG" Mã dịch vụ: PRCI(Ưu tiên checkin và boarding); VOUC(Phòng chờ thương gia); INSR(Bảo hiểm); XBAG(Hành lý); 
            (lấy dữ liệu: dich_vu_phu_tro/danh_sach_phu_tro#ma_dich_vu),
            "ghi_chu": "comment",
            "id_chuyen_bay": 1,
            "id_khach": 1,
            "thong_tin_hanh_ly": [ # bắt buộc khi chọn mua thêm hành lý
                {
                "ten_dich_vu": "WEIGHT", #mặc định
                "khoi_luong_can_mua": "20" lấy dữ liệu: dich_vu_phu_tro#chi_tiet_goi_hanh_ly#chi_tiet#trong_luong_them
                },
                { # mặc định phải có khi thêm hành lý
                "ten_dich_vu": "UNITS [KG/LB]",
                "khoi_luong_can_mua": "KG"
                },
            ]
            }
        ]`
        """

    @classmethod
    def bb_doi_ghe_description(self):
        return """
        `ADD: Thêm ghế mới; DELETE: Huỷ ghế cũ;`
        `Thông tin ghế chọn mua: mỗi chuyến bay khai báo 1 mảng`
        """

    @classmethod
    def bb_doi_dv_description(self):
        return """
            `Vui lòng chạy api danh sách dịch vụ trước để chọn dịch vụ`
            `Mã dịch vụ: PRCI(Ưu tiên checkin và boarding); VOUC(Phòng chờ thương gia); INSR(Bảo hiểm); XBAG(Hành lý)`
            `xoa_dich_vu: bắt buộc nếu muốn đổi dịch vụ -> không điền vào param `
            `id chặng bay: lấy id của bảng chặng bay trong database`
            `id dich vụ cần đổi: lấy id của bảng dịch vụ trong database`
            `Số kg khi chọn dịch vụ XBAG nếu không thì k cần điền vào param`
        """
    