# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from threading import Thread, Lock
from Queue import Queue, Empty
import time
from time import sleep
import os
import json

dir_path = '/mnt/extra-addons/hdwolf/controllers/'
# dir_path = './'

class HDScanner(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.lock = Lock()
        self.barcodes = Queue()

        self.daemon = True
        self.start()


    # def lockedstart(self):
    #     with self.lock:
    #         if not self.isAlive():
    #             self.daemon = True
    #             self.start()

    def get_barcode(self):
        """
        Returns a scanned barcode. Will wait at most 5 seconds to get a barcode,
        and will return barcode scanned in the past if they are not older than 5
        seconds and have not been returned before. This is necessary to catch
        barcodes scanned while the POS is busy reading another barcode
        """

        # self.lockedstart()

        while True:
            try:
                timestamp, barcode = self.barcodes.get(True, 5)
                if timestamp > time.time() - 5:
                    return barcode
            except Empty:
                return ''

    def run(self):
        while True:
            # FIXME: thread never ending
            if 'hdwolfed.json' in os.listdir(dir_path):
                with open(dir_path + 'hdwolfed.json', 'r') as f:
                    barcodes = json.load(f)
                os.remove(dir_path + 'hdwolfed.json')

                for barcode in barcodes:
                    self.barcodes.put((time.time(), barcode))

scanner = HDScanner()

class HDWOLF(http.Controller):
    @http.route('/hdwolf', type='json', auth='none', cors='*')
    def scanner(self):
        return scanner.get_barcode()
