#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, make_response
import pdfkit

api = Blueprint('api', __name__)

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'footer-center': '[page]',
    'footer-font-size': 8,
    'quiet': '',
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}


@api.route('/report', methods=['post'])
def report_index():
    try:
        data = request.get_json()
        html = render_template('baogao.html',data=data)
        student = render_template('student.html',data=data)
        if data['operation'] == 'preview':
            return html+student
        if data['operation'] == 'download':
            pdf = pdfkit.from_string(html+student, None, options=options)
            return pdf
    except:
        return '数据错误',400

