from os.path import abspath, dirname, join

SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
PROPAGATE_EXCEPTIONS = True
# Database configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/api_erp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False
ERROR_404_HELP = False
JWT_SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
JWT_ACCESS_TOKEN_EXPIRES = 86400
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
UPLOAD_FOLDER = join(BASE_DIR, 'uploads')
