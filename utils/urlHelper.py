from itsdangerous import URLSafeSerializer
from flask import current_app
import os
class URLHelper:
    path_dir = os.getcwd()
    @classmethod
    def getInstance(self):
        return URLSafeSerializer(current_app.config['JWT_SECRET_KEY'],salt="activate")
    
