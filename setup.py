from distutils.core import setup


setup(
    name='sotmjp',
    version='2014',
    packages=['sotmjp',
              'sotmjp.account',
              'sotmjp.profile',
              'sotmjp.registration',
              'sotmjp.schedule', 'sotmjp.sponsorship',
              'sotmjp.sponsorship.management',
              'sotmjp.sponsorship.management.commands',
              'sotmjp.sponsorship.templatetags',
              'sotmjp.tutorials',
              'markedit', 'symposion', 'symposion.cms', 'symposion.boxes',
              'symposion.boxes.templatetags', 'symposion.teams',
              'symposion.teams.templatetags', 'symposion.utils',
              'symposion.reviews', 'symposion.reviews.management',
              'symposion.reviews.management.commands',
              'symposion.reviews.templatetags', 'symposion.schedule',
              'symposion.speakers', 'symposion.speakers.management',
              'symposion.speakers.management.commands', 'symposion.proposals',
              'symposion.proposals.templatetags', 'symposion.conference',
              'symposion.social_auth', 'symposion.social_auth.pipeline',
              'symposion.sponsorship', 'symposion.sponsorship.templatetags'],
    url='https://github.com/caktus/pycon/',
    license='LICENSE',
    author='',
    author_email='',
    description=''
)
