﻿# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os

from toolium import test_cases


class SeleniumTestCase(test_cases.SeleniumTestCase):
    """Test Case base class for Selenium tests"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'local-properties.cfg')
        super(SeleniumTestCase, self).setUp()


class AndroidTestCase(test_cases.AppiumTestCase):
    """Test Case base class for Android tests"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'android-properties.cfg',
                                                          'local-android-properties.cfg')
        super(AndroidTestCase, self).setUp()


class AndroidHybridTestCase(test_cases.AppiumTestCase):
    """Test Case base class for Android tests (hybrid app)"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'android-hybrid-properties.cfg',
                                                          'local-android-properties.cfg')
        super(AndroidHybridTestCase, self).setUp()


class AndroidWebTestCase(test_cases.AppiumTestCase):
    """Test Case base class for Android tests (web app)"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'android-web-properties.cfg',
                                                          'local-android-properties.cfg')
        super(AndroidWebTestCase, self).setUp()


class iOSTestCase(test_cases.AppiumTestCase):
    """Test Case base class for iOS tests"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'ios-properties.cfg',
                                                          'local-ios-properties.cfg')
        super(iOSTestCase, self).setUp()


class iOSHybridTestCase(test_cases.AppiumTestCase):
    """Test Case base class for iOS tests (hybrid app)"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'ios-hybrid-properties.cfg',
                                                          'local-ios-properties.cfg')
        super(iOSHybridTestCase, self).setUp()


class iOSWebTestCase(test_cases.AppiumTestCase):
    """Test Case base class for iOS tests (web app)"""

    def setUp(self):
        self.config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.config_files.set_config_properties_filenames('properties.cfg', 'ios-web-properties.cfg',
                                                          'local-ios-properties.cfg')
        super(iOSWebTestCase, self).setUp()


def get_root_path():
    """Returns absolute path of the project root folder

    :returns: root folder path
    """
    return os.path.dirname(os.path.realpath(__file__))
