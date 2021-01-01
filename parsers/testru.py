#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-12-31 08:10:17
# Project: testru

from pyspider.libs.base_handler import *
import requests
import json


class Handler(BaseHandler):
    crawl_config = {
    }
    # 'http://testuz.ru/', 'http://testmat.ru/', 'http://testruslit.ru/', 'http://testfiz.ru/','http://testhistory.ru/'
    pages = ['http://testbiohim.ru/']

    @every(minutes=24 * 60)
    def on_start(self):
        for page in self.pages:
            self.crawl(page, callback=self.categories_page)

    @config(age=10 * 24 * 60 * 60)
    def categories_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if 'cat' in each.attr['href']:
                self.crawl(each.attr.href, callback=self.tests_page)

    def tests_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if 'id' in each.attr['href'] and 'test' in each.attr.href:
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        subjects = {
            'bio_test': 7,
            'him_test': 6
        }
        letters = ['A)', 'B)', 'C)', 'D)']
        task = response.doc('td.task').text()
        answers = response.doc('td.answer').items()
        formatted_answers = [answer.text() for answer in answers]
        form = []
        for index, answ in enumerate(formatted_answers):
            found = False
            for letter in letters:
                if letter in answ:
                    arr = answ.split(letter)
                    form.append({'answer': arr[1].strip(), 'variant': letter[:-1]})
                    found = True
                    continue
            if found:
                continue
            if (index % 2 == 0) or index == 0:
                try:
                    form.append({'answer': formatted_answers[index + 1], 'variant': answ[:-1], 'right': False})
                except IndexError:
                    right = answ
        if 'bio_test' in response.url:
            subject = subjects['bio_test']
        if 'him_test' in response.url:
            subject = subjects['him_test']
        request = {
            'task': task,
            'answers': form,
            'right': right,
            'subject': subject,
            'source': 1
        }
        data = json.dumps(request)
        print(form)
        r = requests.post('http://127.0.0.1:8000/parsers/', json=data)
