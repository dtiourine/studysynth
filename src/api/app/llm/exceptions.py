
class LLMError(Exception):
    """Base exception for all LLM-related errors"""
    pass


class LLMConfigurationError(LLMError):
    """Raised when LLM client is misconfigured"""
    pass


class LLMGenerationError(LLMError):
    """Raised when text generation fails"""
    def __init__(self, message: str, provider: str = None, model: str = None):
        super().__init__(message)
        self.provider = provider
        self.model = model


class LLMRateLimitError(LLMError):
    """Raised when rate limits are exceeded"""
    def __init__(self, message: str, retry_after: int = None):
        super().__init__(message)
        self.retry_after = retry_after


class LLMAuthenticationError(LLMError):
    """Raised when API authentication fails"""
    pass


