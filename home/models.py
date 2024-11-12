from django.db import models

from django.utils.translation import gettext_lazy as _
from wagtail.fields import RichTextField
from wagtail.models import Page

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)

class HomePage(Page):
    pass

class InitiativePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
        ]
    )


class InitiativeDetails(Page):
    always_open = models.BooleanField(
        default=False, verbose_name=_("Always open"), help_text=_("Open 24/7")
    )
    area = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("City district"),
        help_text=_("City district"),
    )
    city = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("City")
    )
    description = RichTextField(
        max_length=32767, blank=True, verbose_name=_("Description")
    )
    email = models.CharField(
        max_length=127, null=True, blank=True, verbose_name=_("Email")
    )
    facebook = models.CharField(
        max_length=1023,
        null=True,
        blank=True,
        verbose_name="Facebook",
        help_text=_("Link to Facebook page"),
    )
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Main image",
    )
    phone = models.CharField(
        max_length=127, null=True, blank=True, verbose_name=_("Phone number")
    )
    short_description = models.CharField(
        max_length=100, blank=True, verbose_name=_("Short description")
    )
    website = models.URLField(
        max_length=1023, null=True, blank=True, verbose_name=_("Website")
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("city"),
                FieldPanel("main_image"),
                FieldPanel("short_description"),
                FieldPanel("description"),
            ],
            heading=_("Basic details"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("email"),
                FieldPanel("phone"),
                FieldPanel("website"),
                FieldPanel("facebook"),
            ],
            heading=_("Contact details"),
        ),
    ]
