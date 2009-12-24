##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope.i18n import translate
from zope import interface, component
from zope.schema.interfaces import ITitledTokenizedTerm
from zope.component import getMultiAdapter, queryMultiAdapter

from z3c.form.widget import FieldWidget
from z3c.form.browser import text, widget
from z3c.form.interfaces import IFormLayer, IFieldWidget
from zojax.layout.interfaces import IPagelet
from zojax.resourcepackage import library

from interfaces import IMediaTypeChoice, IMediaTypeWidget


class MediaTypeWidget(text.TextWidget):
    interface.implements(IMediaTypeWidget)

    def update(self):
        super(MediaTypeWidget, self).update()
        library.include('jquery-plugins')


@interface.implementer(IFieldWidget)
@component.adapter(IMediaTypeChoice, IFormLayer)
def MediaTypeWidgetFactory(field, request):
    return FieldWidget(field, MediaTypeWidget(request))
