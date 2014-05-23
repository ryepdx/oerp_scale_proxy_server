# -*- coding: utf-8 -*-
import time
from helpers.usbscale.scale import Scale, ConnectionError
from helpers.usbscale.scale_manager import ScaleManager
from helpers.usbscale.tests import mocks

class ScaleController():
    def __init__(self):
        self.scale = Scale()
        self.mock_manager = ScaleManager(
            lookup=mocks.usb_ids.USB_IDS,
            usb_lib=mocks.usb_lib.MockUSBLib()
        )
        self.mock_endpoint = mocks.usb_lib.MockEndpoint(0, 0)
        self._last_weighing = None


    def weigh(self, timeout=None, test_weight=None):
        '''Get a reading from the attached USB scale.'''
        scale = self.scale

        # Try to calculate when the request will force a return, based on the
        # passed-in timeout parameter. Default to returning after first reading
        # if the timeout parameter is not either a valid number or "inf".
        try:
            end_time = time.time() + (float(timeout) if timeout else 0)
        except:
            end_time = 0

        if test_weight:
            scale = Scale(device_manager=self.mock_manager)

        try:
            weighing = self._weigh(scale, test_weight=test_weight)

            # Loop until we see a change or until the request times out.
            while time.time() < end_time and weighing == self._last_weighing:
                weighing = self._weigh(scale, test_weight=test_weight)
        except ConnectionError:
            return {'success': False, 'error': 'Could not connect to scale.'}

        if weighing:
            self._last_weighing = weighing
            return {'success': True, 'weight': weighing.weight, 'unit': weighing.unit}

        return {'success': False, 'error': "Could not read scale"}

    def _weigh(self, scale, test_weight = None):
        # Are we running an integration test...
        if test_weight:
            scale.device.set_weight(test_weight)
            weighing = scale.weigh(endpoint=self.mock_endpoint)

        # ...or are we doing an actual weighing?
        if not test_weight:
            weighing = scale.weigh()

        return weighing
