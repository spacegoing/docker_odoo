# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from threading import Thread, Lock
from Queue import Queue, Empty
import time


class HDScanner(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.lock = Lock()
        self.barcodes = Queue()


    def lockedstart(self):
        with self.lock:
            if not self.isAlive():
                self.daemon = True
                self.start()

    def get_barcode(self):
        """
        Returns a scanned barcode. Will wait at most 5 seconds to get a barcode,
        and will return barcode scanned in the past if they are not older than 5
        seconds and have not been returned before. This is necessary to catch
        barcodes scanned while the POS is busy reading another barcode
        """
        self.lockedstart()

        while True:
            try:
                timestamp, barcode = self.barcodes.get(True, 5)
                if timestamp > time.time() - 5:
                    return barcode
            except Empty:
                return ''

    def run(self):
        self.barcodes.put((time.time(),"2100002000003"))
        # FIXME: thread never ending
        while True:
            a=1

scanner = HDScanner()

class HDWOLF(http.Controller):
    @http.route('/hdwolf', type='http', auth='none', cors='*')
    def hello(self):
        return request.make_response('hello',{
            'Cache-Control': 'no-cache',
            'Content-Type': 'text/html; charset=utf-8',
            'Access-Control-Allow-Origin':  '*',
            'Access-Control-Allow-Methods': 'POST',
            })

    @http.route('/hdwolf', type='json', auth='none', cors='*')
    def scanner(self):
        return scanner.get_barcode()
















