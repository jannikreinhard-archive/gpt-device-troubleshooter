import importlib.util
import json
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import Mock, patch

# The utility's Streamlit import is unused. Tests need no UI or network packages.
sys.modules.setdefault('streamlit', types.ModuleType('streamlit'))
sys.modules.setdefault('requests', types.ModuleType('requests'))
spec = importlib.util.spec_from_file_location('utility_under_test', Path(__file__).parents[1] / 'website/modules/utility.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ResponseTests(unittest.TestCase):
    def setUp(self):
        self.client = module.utility('fake-key', 'https://example.invalid', 'deployment', {})

    def test_invalid_history_is_removed_and_prompt_is_not_duplicated(self):
        response = Mock()
        response.json.return_value = {'choices': [{'message': {'content': 'OK'}}]}
        history = [{'role': 'assistant', 'content': None}, {'role': 'assistant', 'content': False}, {'role': 'user', 'content': 'question'}]
        with patch.object(module.requests, 'post', return_value=response, create=True) as post:
            self.assertEqual(self.client.invoke_gpt_call('question', history=history), 'OK')
        payload = json.loads(post.call_args.kwargs['data'])
        self.assertEqual(payload['messages'], [{'role': 'user', 'content': 'question'}])
        self.assertEqual(post.call_args.kwargs['timeout'], 60)
        self.assertEqual(len(history), 3)

    def test_empty_response_does_not_return_none(self):
        for content in (None, '', ' ', False):
            with self.subTest(content=content):
                response = Mock()
                response.json.return_value = {'choices': [{'message': {'content': content}}]}
                with patch.object(module.requests, 'post', return_value=response, create=True):
                    with self.assertRaises(RuntimeError): self.client.invoke_gpt_call('question')

    def test_model_http_failure_is_safe(self):
        response = Mock()
        response.raise_for_status.side_effect = ValueError('secret-response-body')
        with patch.object(module.requests, 'post', return_value=response, create=True):
            with self.assertRaises(RuntimeError) as error: self.client.invoke_gpt_call('question')
        self.assertNotIn('secret-response-body', str(error.exception))

    def test_graph_transport_failure_is_real_exception(self):
        with patch.object(module.requests, 'get', side_effect=OSError('private endpoint details'), create=True):
            with self.assertRaises(RuntimeError) as error: self.client.get_graph_call_custom('devices')
        self.assertNotIn('private endpoint details', str(error.exception))

    def test_graph_empty_collection_and_timeout(self):
        response = Mock()
        response.json.return_value = {}
        with patch.object(module.requests, 'get', return_value=response, create=True) as get:
            self.assertEqual(self.client.get_graph_call_custom('devices'), [])
        self.assertEqual(get.call_args.kwargs['timeout'], 60)

if __name__ == '__main__': unittest.main()
