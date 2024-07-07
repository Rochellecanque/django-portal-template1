# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.template.loader import get_template, TemplateDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import logging

#Load CORE views to inherit from
from core import views as CORE_VIEWS
from restaurant import views as Restaurant_VIEWS

logger = logging.getLogger(__name__)


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    context = CORE_VIEWS.context_maker(request, context)

    html_template = loader.get_template('sample/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    context = CORE_VIEWS.context_maker(request, context)

    load_template = request.path.strip('/').split('/')[-1]
    logger.debug(f'Loading template: {load_template}')

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))
    elif load_template == "":
        return HttpResponseRedirect(reverse('home'))

    #return CORE_VIEWS.template_loader(request, context, 'sample/' + load_template)

    template_path = f'sample/{load_template}.html'
    try:
        html_template = get_template(template_path)
    except TemplateDoesNotExist:
        logger.error(f'Template not found: {template_path}')
        return HttpResponse("Template not found", status=404)
    
    return HttpResponse(html_template.render(context, request))

