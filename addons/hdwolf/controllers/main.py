# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from threading import Thread, Lock
from Queue import Queue, Empty
import time
from time import sleep
import os
import json

lock = Lock()
Barcodes = Queue()
DelProdNames = Queue()


def get_barcode():
    """
    Returns a scanned barcode. Will wait at most 5 seconds to get a barcode,
    and will return barcode scanned in the past if they are not older than 5
    seconds and have not been returned before. This is necessary to catch
    barcodes scanned while the POS is busy reading another barcode
    """

    # self.lockedstart()

    while True:
        try:
            timestamp, barcode = Barcodes.get(True, 5)
            # print barcode
            return barcode
        except Empty:
            # print id(Barcodes)
            return ''


def put_barcode(barcodes):
    for barcode in barcodes:
        Barcodes.put((time.time(), barcode))

    # print id(Barcodes)

def get_del_prod_name():
    """
    Returns a scanned barcode. Will wait at most 5 seconds to get a barcode,
    and will return barcode scanned in the past if they are not older than 5
    seconds and have not been returned before. This is necessary to catch
    barcodes scanned while the POS is busy reading another barcode
    """

    # self.lockedstart()

    while True:
        try:
            timestamp, prod_name = DelProdNames.get(True, 5)
            # print barcode
            return prod_name
        except Empty:
            # print id(Barcodes)
            return ''


def put_del_prod_name(del_prod_name):
    DelProdNames.put((time.time(), del_prod_name))
    # print id(Barcodes)


class HDWOLF(http.Controller):
    @http.route('/hdwolf', type='json', auth='none', cors='*')
    def scanner(self):
        return get_barcode()

    @http.route('/hdwolf/put', type='json', auth='none', cors='*')
    def wolf(self, barcodes):
        put_barcode(barcodes)
        return 'hdwolf_app_success!'

    @http.route('/hdwolf/go', type='json', auth='none', cors='*')
    def go(self):
        return get_del_prod_name()

    @http.route('/hdwolf/put_go', type='json', auth='none', cors='*')
    def put_go(self, del_prod_name):
        put_del_prod_name(del_prod_name)
        return 'Go_success!'
