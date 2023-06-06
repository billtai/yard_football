from database import ma

class PGBaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instance   = True
        include_fk      = True
        ordered         = True

    # Get schema metada (need to update more)
    @classmethod
    def get_schema(cls):
        schema                      = cls()
        schema_dict                 = {}
        schema_dict["properties"]   = {}
        requied_fields              = []
        for field in dict(schema.fields):
            schema_dict["properties"][field] = {}
            type = schema.fields[field].__class__.__name__.lower()

            if type == 'datetime':
                type = 'string'
                schema_dict["properties"][field]["format"] = 'date-time'
            if type == 'nested':
                type = 'object'
                schema_dict["properties"][field]["format"] = 'object'

            if type == 'inferred':
                type = 'integer'
                schema_dict["properties"][field]["format"] = 'integer'

            schema_dict["properties"][field]["type"] = type
            if schema.fields[field].required:
                requied_fields.append(field)
        schema_dict['required'] = requied_fields
        schema_dict['type']     = 'object'

        return schema_dict
