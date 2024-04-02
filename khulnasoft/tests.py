import os
import unittest
from types import AsyncGeneratorType, GeneratorType
from unittest.mock import MagicMock, patch

from khulnasoft.clients import AsyncKhulnasoft, Khulnasoft
from khulnasoft.exceptions import AuthenticationError, InternalServerError


class TestKhulnasoft(unittest.TestCase):
    def setUp(self) -> None:
        # Set up a valid API key for testing
        self.valid_api_key = os.environ.get("KHULNASOFT_KEY")

    def test_invalid_api_key_raises_authentication_error(self) -> None:
        # Instantiate Khulnasoft with an invalid API key
        with self.assertRaises(AuthenticationError):
            khulnasoft = Khulnasoft(api_key="invalid_api_key")
            khulnasoft.generate("hello")

    @patch("os.environ.get", return_value=None)
    def test_missing_api_key_raises_key_error(self, mock_get: MagicMock) -> None:
        # Initializing Khulnasoft without providing API key should raise KeyError
        with self.assertRaises(KeyError):
            Khulnasoft()

    def test_incorrect_model_name_raises_internal_server_error(self) -> None:
        # Instantiate Khulnasoft with a valid API key
        khulnasoft = Khulnasoft(self.valid_api_key)
        # Provide incorrect model name to generate function
        with self.assertRaises(InternalServerError):
            khulnasoft.generate(messages="hello", model="llama-chat")

    def test_generate_returns_string_when_stream_false(self) -> None:
        # Instantiate Khulnasoft with a valid API key
        khulnasoft = Khulnasoft(api_key=self.valid_api_key)
        # Call generate with stream=False
        result = khulnasoft.generate("hello", stream=False)
        # Assert that the result is a string
        self.assertIsInstance(result, str)

    def test_generate_returns_generator_when_stream_true(self) -> None:
        # Instantiate Khulnasoft with a valid API key
        khulnasoft = Khulnasoft(api_key=self.valid_api_key)
        # Call generate with stream=True
        result = khulnasoft.generate("hello", stream=True)
        # Assert that the result is a generator
        self.assertIsInstance(result, GeneratorType)


class TestAsyncKhulnasoft(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        # Set up a valid API key for testing
        self.valid_api_key = os.environ.get("KHULNASOFT_KEY")

    async def test_invalid_api_key_raises_authentication_error(self) -> None:
        # Instantiate AsyncKhulnasoft with an invalid API key
        with self.assertRaises(AuthenticationError):
            async_khulnasoft = AsyncKhulnasoft(api_key="invalid_api_key")
            await async_khulnasoft.generate("hello")

    @patch("os.environ.get", return_value=None)
    async def test_missing_api_key_raises_key_error(self, mock_get: MagicMock) -> None:
        # Initializing AsyncKhulnasoft without providing
        # API key should raise KeyError
        with self.assertRaises(KeyError):
            async_khulnasoft = AsyncKhulnasoft()
            await async_khulnasoft.generate("hello")

    async def test_incorrect_model_name_raises_internal_server_error(self) -> None:
        # Instantiate AsyncKhulnasoft with a valid API key
        async_khulnasoft = AsyncKhulnasoft(api_key=self.valid_api_key)
        # Provide incorrect model name to generate function
        with self.assertRaises(InternalServerError):
            await async_khulnasoft.generate(messages="hello", model="llama-chat")

    async def test_generate_returns_string_when_stream_false(self) -> None:
        # Instantiate AsyncKhulnasoft with a valid API key
        async_khulnasoft = AsyncKhulnasoft(api_key=self.valid_api_key)
        # Call generate with stream=False
        result = await async_khulnasoft.generate("hello", stream=False)
        # Assert that the result is a string
        self.assertIsInstance(result, str)

    async def test_generate_returns_generator_when_stream_true(self) -> None:
        # Instantiate AsyncKhulnasoft with a valid API key
        async_khulnasoft = AsyncKhulnasoft(api_key=self.valid_api_key)
        # Call generate with stream=True
        result = await async_khulnasoft.generate("hello", stream=True)
        # Assert that the result is a generator
        self.assertIsInstance(result, AsyncGeneratorType)


if __name__ == "__main__":
    unittest.main()
