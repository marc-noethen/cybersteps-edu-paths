import os
from unittest import TestCase
from datetime import datetime
from insightlog import *


class TestInsightLog(TestCase):

    def test_get_date_filter(self):
        nginx_settings = get_service_settings('nginx')
        self.assertEqual(get_date_filter(nginx_settings, 13, 13, 16, 1, 1989),
                         '[16/Jan/1989:13:13', "get_date_filter#1")
        self.assertEqual(get_date_filter(nginx_settings, '*', '*', 16, 1, 1989),
                         '[16/Jan/1989', "get_date_filter#2")
        self.assertEqual(get_date_filter(nginx_settings, '*'), datetime.now().strftime("[%d/%b/%Y:%H"),
                         "get_date_filter#3")
        apache2_settings = get_service_settings('apache2')
        self.assertEqual(get_date_filter(apache2_settings, 13, 13, 16, 1, 1989),
                         '[16/Jan/1989:13:13', "get_date_filter#4")
        self.assertEqual(get_date_filter(apache2_settings, '*', '*', 16, 1, 1989),
                         '[16/Jan/1989', "get_date_filter#5")
        self.assertEqual(get_date_filter(apache2_settings, '*'), datetime.now().strftime("[%d/%b/%Y:%H"),
                         "get_date_filter#6")
        auth_settings = get_service_settings('auth')
        self.assertEqual(get_date_filter(auth_settings, 13, 13, 16, 1),
                         'Jan 16 13:13:', "get_date_filter#7")
        self.assertEqual(get_date_filter(auth_settings, '*', '*', 16, 1),
                         'Jan 16 ', "get_date_filter#8")

    def test_filter_data(self):
        nginx_settings = get_service_settings('nginx')
        date_filter = get_date_filter(nginx_settings, '*', '*', 27, 4, 2016)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_name = os.path.join(base_dir, 'logs-samples/nginx1.sample')
        data = filter_data('192.168.5', filepath=file_name)
        data = filter_data(date_filter, data=data)
        self.assertEqual(len(data.split("\n")), 28, "filter_data#1")
        self.assertRaises(Exception, filter_data, log_filter='192.168.5')
        apache2_settings = get_service_settings('apache2')
        date_filter = get_date_filter(apache2_settings, 27, 11, 4, 5, 2016)
        file_name = os.path.join(base_dir, 'logs-samples/apache1.sample')
        data = filter_data('127.0.0.1', filepath=file_name)
        data = filter_data(date_filter, data=data)
        self.assertEqual(len(data.split("\n")), 34, "filter_data#2")
        self.assertRaises(Exception, filter_data, log_filter='127.0.0.1')
        auth_settings = get_service_settings('auth')
        date_filter = get_date_filter(auth_settings, '*', 22, 4, 5)
        file_name = os.path.join(base_dir, 'logs-samples/auth.sample')
        data = filter_data('120.25.229.167', filepath=file_name)
        data = filter_data(date_filter, data=data)
        self.assertEqual(len(data.split("\n")), 19, "filter_data#3")
        data = filter_data('120.25.229.167', filepath=file_name, is_reverse=True)
        self.assertFalse('120.25.229.167' in data, "filter_data#4")

    def test_get_web_requests(self):
        nginx_settings = get_service_settings('nginx')
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_name = os.path.join(base_dir, 'logs-samples/nginx1.sample')
        data = filter_data('192.10.1.1', filepath=file_name)
        requests = get_web_requests(data, nginx_settings['request_model'])
        self.assertEqual(len(requests), 2, "get_web_requests#1")
        self.assertTrue('daedalu5' in requests[0].values(), "get_web_requests#2")
        requests = get_web_requests(data, nginx_settings['request_model'],
                                    nginx_settings['date_pattern'], nginx_settings['date_keys'])
        self.assertEqual(requests[0]['DATETIME'], '2016-04-24 06:26:37', "get_web_requests#3")
        apache2_settings = get_service_settings('apache2')
        file_name = os.path.join(base_dir, 'logs-samples/apache1.sample')
        data = filter_data('127.0.1.1', filepath=file_name)
        requests = get_web_requests(data, apache2_settings['request_model'])
        self.assertEqual(len(requests), 1, "get_web_requests#4")
        self.assertTrue('daedalu5' in requests[0].values(), "get_web_requests#5")
        requests = get_web_requests(data, apache2_settings['request_model'],
                                    apache2_settings['date_pattern'], apache2_settings['date_keys'])
        self.assertEqual(requests[0]['DATETIME'], '2016-05-04 11:31:39', "get_web_requests#3")

    def test_get_auth_requests(self):
        auth_settings = get_service_settings('auth')
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        date_filter = get_date_filter(auth_settings, '*', 22, 4, 5)
        file_name = os.path.join(base_dir, 'logs-samples/auth.sample')
        data = filter_data('120.25.229.167', filepath=file_name)
        data = filter_data(date_filter, data=data)
        requests = get_auth_requests(data, auth_settings['request_model'])
        self.assertEqual(len(requests), 18, "get_auth_requests#1")
        self.assertEqual(requests[17]['INVALID_PASS_USER'], 'root', "get_auth_requests#2")
        self.assertEqual(requests[15]['INVALID_USER'], 'admin', "get_auth_requests#3")
        requests = get_auth_requests(data, auth_settings['request_model'],
                                     auth_settings['date_pattern'], auth_settings['date_keys'])
        self.assertEqual(requests[0]['DATETIME'][4:], '-05-04 22:00:32', "get_auth_requests#4")

    def test_get_requests(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        auth_logfile = os.path.join(base_dir, 'logs-samples/auth.sample')
        nginx_logfile = os.path.join(base_dir, 'logs-samples/nginx1.sample')
        
        # Test auth logs with filters
        auth_settings = get_service_settings('auth')
        date_filter = get_date_filter(auth_settings, minute='*', hour=22, day=4, month=5)
        auth_filters = [
            {'filter_pattern': '120.25.229.167', 'is_casesensitive': True, 'is_regex': False, 'is_reverse': False},
            {'filter_pattern': date_filter, 'is_casesensitive': True, 'is_regex': False, 'is_reverse': False}
        ]
        requests = get_requests('auth', filepath=auth_logfile, filters=auth_filters)
        self.assertEqual(len(requests), 18, "get_requests#1")
        
        # Test nginx logs with filter
        nginx_filters = [
            {'filter_pattern': '192.10.1.1', 'is_casesensitive': True, 'is_regex': False, 'is_reverse': False}
        ]
        requests = get_requests('nginx', filepath=nginx_logfile, filters=nginx_filters)
        self.assertEqual(len(requests), 2, "get_requests#2")

# TODO: Add more tests for edge cases and error handling
    def test_ipv4_regex_only_matches_valid_ips(self):
            """Test that IPv4_REGEX only matches valid IP addresses"""
            import re
            from insightlog import IPv4_REGEX
            
            # Valid IPs - SHOULD match
            valid_ips = [
                "192.168.1.1",
                "10.0.0.1", 
                "172.16.0.1",
                "255.255.255.255"
            ]
            
            for ip in valid_ips:
                result = re.search(IPv4_REGEX, ip)
                self.assertIsNotNone(result, f"Should match valid IP: {ip}")
            
            # Invalid patterns - should NOT match
            invalid_patterns = [
                "123a456b789c012",  # letters instead of dots
                "192.168.1",        # incomplete IP
                "192.168.1.1.5",    # too many octets
                "1000.2000.3000.4000", # to many digits
                "5192.168.1.1",     # no match (diget before!)
                ".192.168.1.1",     # no match dot before
                "192.168.1"        # too less octets
            ]
            
            for pattern in invalid_patterns:
                result = re.search(IPv4_REGEX, pattern)
                self.assertIsNone(result, f"Should NOT match invalid pattern: {pattern}")


    def test_export_to_json_returns_valid_json(self):
            """Test that export_to_json produces valid JSON"""
            import json
            from insightlog import export_to_json
            
            # Sample request data
            test_requests = [
                {'DATETIME': '2024-01-01 10:00:00', 'IP': '192.168.1.1', 'METHOD': 'GET'},
                {'DATETIME': '2024-01-01 10:01:00', 'IP': '10.0.0.1', 'METHOD': 'POST'}
            ]
            
            # Export to JSON string
            json_output = export_to_json(test_requests)
            
            # Verify it's valid JSON
            parsed = json.loads(json_output)
            self.assertEqual(len(parsed), 2)
            self.assertEqual(parsed[0]['IP'], '192.168.1.1')
            self.assertEqual(parsed[1]['METHOD'], 'POST')
        
    def test_export_to_json_with_file(self):
            """Test that export_to_json can write to file"""
            import json
            import tempfile
            import os
            from insightlog import export_to_json
            
            test_requests = [
                {'DATETIME': '2024-01-01 10:00:00', 'IP': '192.168.1.1'}
            ]
            
            # Create temp file
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
                temp_path = f.name
            
            try:
                # Export to file
                result = export_to_json(test_requests, output_file=temp_path)
                
                # Should return success message
                self.assertIn('exported', result.lower())
                
                # Verify file content
                with open(temp_path, 'r') as f:
                    loaded = json.load(f)
                
                self.assertEqual(len(loaded), 1)
                self.assertEqual(loaded[0]['IP'], '192.168.1.1')
            finally:
                # Cleanup
                if os.path.exists(temp_path):
                    os.unlink(temp_path)


