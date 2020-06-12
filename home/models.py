from django.db import models
from wagtailtrans.models import TranslatablePage

# new stuff
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(TranslatablePage):
    # new stuff
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel('body', classname='full'),]
