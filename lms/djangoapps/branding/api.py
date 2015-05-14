"""Edx branding API
"""
import logging
import os
from django.conf import settings
from django.utils.translation import ugettext as _
from microsite_configuration import microsite
from edxmako.shortcuts import marketing_link
from staticfiles.storage import staticfiles_storage

log = logging.getLogger("edx.footer")


def get_footer():
    """ Get the footer links json

    Returns:
        Dict of footer links
    """

    site_name = microsite.get_value('SITE_NAME', settings.SITE_NAME)
    context = dict()
    context["copy_right"] = copy_right()
    context["heading"] = heading()
    context["logo_img"] = get_footer_logo(site_name)
    context["social_links"] = social_links()
    context["about_links"] = about_edx_link(site_name)

    return {"footer": context}


def copy_right():
    """ Returns the copy rights text
    """
    if settings.FEATURES.get('IS_EDX_DOMAIN', False):
        data = _(
            "(c) 2015 edX Inc. EdX, Open edX, and the edX and Open edX logos "
            "are registered trademarks or trademarks of edX Inc."
        )
    else:
        data = _(
            "EdX, Open edX, and the edX and Open edX logos are registered trademarks or "
            "trademarks of {link_start}edX Inc.{link_end}"
        ).format(
            link_start=u"<a href='https://www.edx.org/'>",
            link_end=u"</a>"
        )

    return data


def heading():
    """ Returns the heading text
    """
    if settings.FEATURES.get('IS_EDX_DOMAIN', False):
        data = _("EdX offers interactive online classes and MOOCs from the world's best universities, "
                 "colleges and organizations. Online courses from MITx, HarvardX, BerkeleyX, UTx and "
                 "many other universities can be taken here. Topics include biology, business, chemistry,"
                 " computer science, economics, finance, electronics, engineering, food and nutrition,"
                 " history, humanities, law, literature, math, medicine, music, philosophy, physics, science,"
                 " statistics and more. EdX is a non-profit online initiative created by founding partners"
                 " Harvard and MIT.")
    else:
        data = _("EdX offers interactive online classes and MOOCs from the world's best universities, "
                 "colleges and organizations. Online courses from MITx, HarvardX, BerkeleyX, UTx and "
                 "many other universities can be taken here. Topics include biology, business, chemistry,"
                 " computer science, economics, finance, electronics, engineering, food and nutrition,"
                 " history, humanities, law, literature, math, medicine, music, philosophy, physics, science,"
                 " statistics and more. EdX is a non-profit online initiative created by founding partners"
                 " Harvard and MIT.")
    return data


def social_links():
    """ Returns the list of social link of footer
    """
    links = []
    for social_name in settings.SOCIAL_MEDIA_FOOTER_NAMES:
        links.append(
            {
                "provider": social_name,
                "title": unicode(settings.SOCIAL_MEDIA_FOOTER_DISPLAY.get(social_name, {}).get("title", "")),
                "url": settings.SOCIAL_MEDIA_FOOTER_URLS.get(social_name, "#")
            }
        )
    return links


def about_edx_link(site_name):
    """ Returns the list of marketing links of footer
    """

    return dict(
        [
            (_(key), marketing_link(key))
            for key in (
                settings.MKTG_URL_LINK_MAP.viewkeys() |
                settings.MKTG_URLS.viewkeys()
            )
        ]
    )


def get_footer_logo(site_name):
    if settings.FEATURES.get('IS_EDX_DOMAIN', False):
        logo_file = 'images/edx-theme/edx-header-logo.png'
    else:
        logo_file = 'images/default-theme/logo.png'
    try:
        url = site_name + staticfiles_storage.url(logo_file)
    except:
        url = site_name + logo_file
    return url


def get_footer_static(file_name):
    """ Returns the static js/css contents as a string

    Args:
        file_name(str): path to the static file name under static folder

    Raises:
        I/O Error if file not found
    Returns:
        Contents of static file

    """
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, "static/{}".format(file_name))
    with open(file_path, "r") as _file:
        contents = _file.read()
    return contents
