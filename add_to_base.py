STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "..", "merlin", "static"),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "merlin", "media")
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "merlin", "media"),
]

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.template.TemplateFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_PRECOMPILERS = (
    ('module', 'compressor_toolkit.precompilers.ES6Compiler'),
    ('css', 'compressor_toolkit.precompilers.SCSSCompiler'),
)
COMPRESS_ROOT = os.path.join(BASE_DIR, "..", "merlin", "static")
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

EMAIL_HOST = 'smtp.mailfence.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = ''
