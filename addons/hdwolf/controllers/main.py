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
DelProdBarcodes = Queue()
DiscountProdBarcodes = Queue()


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

def get_del_prod_barcode():
    """
    Returns a scanned barcode. Will wait at most 5 seconds to get a barcode,
    and will return barcode scanned in the past if they are not older than 5
    seconds and have not been returned before. This is necessary to catch
    barcodes scanned while the POS is busy reading another barcode
    """

    # self.lockedstart()

    while True:
        try:
            timestamp, prod_barcode = DelProdBarcodes.get(True, 5)
            # print barcode
            return prod_barcode
        except Empty:
            # print id(Barcodes)
            return ''


def put_del_prod_barcode(del_prod_barcode):
    DelProdBarcodes.put((time.time(), del_prod_barcode))
    # print id(Barcodes)

def get_discount_barcodes():
    """
    Returns a scanned barcode. Will wait at most 5 seconds to get a barcode,
    and will return barcode scanned in the past if they are not older than 5
    seconds and have not been returned before. This is necessary to catch
    barcodes scanned while the POS is busy reading another barcode
    """

    # self.lockedstart()

    while True:
        try:
            timestamp, prod_barcode = DiscountProdBarcodes.get(True, 5)
            # print barcode
            return prod_barcode
        except Empty:
            # print id(Barcodes)
            return ''


def put_discount_barcodes(discount_barcodes):
    DiscountProdBarcodes.put((time.time(), discount_barcodes))
    print id(discount_barcodes)


class HDWOLF(http.Controller):
    @http.route('/hdwolf', type='json', auth='none', cors='*')
    def scanner(self):
        return get_barcode()

    @http.route('/hdwolf/put', type='json', auth='none', cors='*')
    def wolf(self, barcodes):
        put_barcode(barcodes)
        return 'hdwolf_app_success!'

    @http.route('/hdwolf/go_deduct', type='json', auth='none', cors='*')
    def go_deduct(self):
        return get_del_prod_barcode()

    @http.route('/hdwolf/put_go_deduct', type='json', auth='none', cors='*')
    def put_go(self, del_prod_barcode):
        put_del_prod_barcode(del_prod_barcode)
        return 'Go_deduct_success!'

    @http.route('/hdwolf/go_discount', type='json', auth='none', cors='*')
    def go_discount(self):
        return get_discount_barcodes()

    @http.route('/hdwolf/put_go_discount', type='json', auth='none', cors='*')
    def put_go_discount(self, discount_barcodes):
        put_discount_barcodes(discount_barcodes)
        return 'Go_discount_success!'
