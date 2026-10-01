"""
Salt Security Guardrail Integration for LiteLLM
https://salt.security
"""

from typing import TYPE_CHECKING, Final

from .salt_security import SaltSecurityGuardrail

if TYPE_CHECKING:
    from litellm.types.guardrails import Guardrail, LitellmParams


def initialize_guardrail(litellm_params: "LitellmParams", guardrail: "Guardrail"):
    import litellm

    callback = SaltSecurityGuardrail(
        guardrail_name=guardrail.get("guardrail_name"),
        api_key=litellm_params.api_key,
        api_base=litellm_params.api_base,
        event_hook=litellm_params.mode,
        default_on=litellm_params.default_on,
        fail_on_error=getattr(litellm_params, "fail_on_error", True),
        unreachable_fallback=getattr(litellm_params, "unreachable_fallback", "fail_closed"),
    )
    litellm.logging_callback_manager.add_litellm_callback(callback)
    return callback


guardrail_initializer_registry: Final = {
    "salt_security": initialize_guardrail,
}

guardrail_class_registry: Final = {
    "salt_security": SaltSecurityGuardrail,
}

__all__ = ["SaltSecurityGuardrail"]
