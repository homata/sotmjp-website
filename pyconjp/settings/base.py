#:coding=utf-8:

from pycon.settings.base import *  # NOQA

INSTALLED_APPS.append('pyconjp')
INSTALLED_APPS.append('pyconjp.account')
INSTALLED_APPS.append('restcms')
INSTALLED_APPS.remove('symposion.cms')

ROOT_URLCONF = 'pyconjp.urls'

TIME_ZONE = 'Asia/Tokyo'

LANGUAGES = (
    ('en', 'English'),
    ('ja', 'Japanese'),
)

BIBLION_SECTIONS = [
    ("ja", u"Japanese/日本語"),
    ("en", u"English/英語"),
]

# Add config for Google Analytics
CONSTANCE_CONFIG["GOOGLE_ANALYTICS_TRACKING_ID"] = ("", "The site's Google Analytics Tracking ID.")

PROPOSAL_FORMS['talk'] = 'pyconjp.forms.PyConJPTalkProposalForm'
TEMPLATE_DIRS.insert(0, os.path.join(PROJECT_ROOT, "pyconjp/templates"))
