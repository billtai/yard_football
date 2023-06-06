import math


class AfterQueryHelper:
    PAGE_CURRENT = 0
    INCREASE_CURRENT = 1
    OFFSET_INDEX_DEFAULT = 1

    @classmethod
    def get_model_to_json(self, list_dump={
        "model": [],
        "model_name": [],
        "schemas": [],
        "res_key": [],
    }, main_model=None):
        """
            (model,model) => (model_main,[key]:model)
        """
        model_json = {}
        for index, value in enumerate(list_dump['model']):
            # for để lấy danh sách schema theo index của các model khi lấy danh sách
            # gán các schema theo danh sách các model trong câu truy vấn, cần sắp xếp theo đúng thứ tự
            schemas = list_dump['schemas'][index]
            if type(value).__name__ == list_dump['model_name'][index]:
                if type(value).__name__ == main_model:
                    model_json.update(schemas.dump(value))
                else:
                    if len(list_dump['res_key']) > 0:
                        res_key = list_dump['res_key'][index-1]
                        model_json[res_key] = schemas.dump(value)

        return model_json

    @classmethod
    def get_remove_dup_dict(self, list_duplicate=[]):
        return list(dict.fromkeys(list_duplicate))

    @classmethod
    def create_response_paging(self, page=0, limit=25, data=[], count=0):
        """
            data => paging
        """

        number_page = math.floor(count / limit) + (self.PAGE_CURRENT if count %
                                                   limit == self.PAGE_CURRENT else self.INCREASE_CURRENT)

        return {
            "content": data,
            "total_records": count,
            "total_pages": number_page,
            "page": page,
            "has_next": page < number_page,
            "has_prev": page > 1,
        }
