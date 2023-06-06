from utils.parserHelper import ParserHelper
from sqlalchemy import or_, and_

class BeforeQueryHelper:
    OFFSET_INDEX_DEFAULT = 1

    @classmethod
    def get_fields_search_join_multiple_exactly(self, payload={}, model=None, list_search=[]):
        search_args = []
        for col in list_search:
            if col["name"] in payload:
                field = payload[col["name"]]
                search_args.append(getattr(model, col["alias"]).like(field))
        return search_args

    @classmethod
    def get_fields_search_start_day(self, payload={}, model=None, list_search=[]):
        search_args = []
        for col in list_search:
            if col["name"] in payload:
                field = str(payload[col["name"]])
                search_args.append(getattr(model, col["alias"]) >= field)
        return search_args

    @classmethod
    def get_fields_search_end_day(self, payload={}, model=None, list_search=[]):
        search_args = []
        for col in list_search:
            if col["name"] in payload:
                field = str(payload[col["name"]])
                search_args.append(getattr(model, col["alias"]) <= field) 
        return search_args
    # Tìm theo 1 key
    @classmethod
    def get_fields_search_join_multiple(self, payload={}, model=None, list_search=[]):
        search_args = []
        for col in list_search:
            if col["name"] in payload:
                field = payload[col["name"]]
                search_args.append(getattr(model, col["alias"]).ilike(f"%{field}%"))
        return search_args

    @classmethod
    def get_fields_search_null(self, payload={}, model=None, list_search=[]):
        search_args = []
        for col in list_search:
            if col["name"] in payload:
                if int(payload[col["alias"]][0])==1:
                    search_args.append(getattr(model, col["alias"]).is_not(None))
                else:
                    search_args.append(getattr(model, col["alias"]).is_(None))
        return search_args
    @classmethod
    def get_fields_search_multiple_parser(self, payload={}, model=None, list_search=[]):
        search_args = []
        for col in list_search:
            props_parser = col["name"] + "[]"
            if props_parser in payload:
                field = payload[props_parser]
                search_child_query = []
                for value in field:
                    search_child_query.append(getattr(model, col["name"]).ilike(f"%{value}%"))
                search_args.append(or_(*search_child_query))
        return search_args
    # Tìm theo list
    @classmethod
    def get_fields_search_join_multiple_parser(self, payload={}, model=None, list_search=[]):
        """
        {"name": 'ten_san_bay_di', "alias": "ten"},
        "name": trường input
        "alias": trường trong database
        "model": lấy từ model nào trong database
        """
        search_args = []
        for col in list_search:
            props_parser_name = col["name"] + "[]"
            props_parser_alias = col["alias"]
            if props_parser_name in payload:
                field = payload[props_parser_name]
                search_child_query = []
                for value in field:
                    search_child_query.append(getattr(model, props_parser_alias).ilike(f"%{value}%"))
                search_args.append(or_(*search_child_query))
        return search_args

    @classmethod
    def get_search_model_join_multiple_parser(self, payload={}, list_search=[]):
        """
        Example:
         {"name": 'ten_san_bay_di', "alias": "ten", "model": san_bay_di},
         "name": trường input
         "alias": trường trong database
         "model": lấy từ model nào trong database
        """
        search_args = []
        for col in list_search:
            props_parser_name   = col["name"] + "[]"
            props_parser_alias  = col["alias"]
            props_parser_model  = col["model"]
            if props_parser_name in payload:
                field = payload[props_parser_name]
                search_child_query = []
                for value in field:
                    search_child_query.append(getattr(props_parser_model, props_parser_alias).ilike(f"%{value}%"))   
                search_args.append(or_(*search_child_query))
        return search_args


    # Sắp xếp
    @classmethod
    def get_fields_sort_multiple_parser(self, value, model=None, list_sort=[], default_value=""):
        """
        alias: -> lấy thuộc tính model
        name: field truyền vào.
        """
        for col in list_sort:
            if col["name"] == value:
                sap_xep = ParserHelper.getattr_parser(model, col["alias"], default_value)
                return sap_xep
        return None
    
    # Phân trang
    @classmethod
    def get_limit_and_offset(self, page, limit, query):
        start = (page - self.OFFSET_INDEX_DEFAULT) * limit
        return query.offset(start).limit(limit)
