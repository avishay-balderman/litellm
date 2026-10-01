# +-------------------------------------------------------------+
#
#           Salt Security Guardrail Integration for LiteLLM
#                       https://salt.security
#
# +-------------------------------------------------------------+

import os
from typing import TYPE_CHECKING

from litellm.proxy.guardrails.guardrail_hooks.generic_guardrail_api.generic_guardrail_api import (
    GenericGuardrailAPI,
)

if TYPE_CHECKING:
    from litellm.types.proxy.guardrails.guardrail_hooks.base import GuardrailConfigModel


class SaltSecurityGuardrail(GenericGuardrailAPI):
    """
    Salt Security AI Guardrail for LiteLLM.
    https://salt.security

    Implements the Generic Guardrail API contract. All security logic runs in the
    Salt-hosted endpoint. LiteLLM calls it synchronously before the LLM is invoked
    and enforces the BLOCKED / NONE / GUARDRAIL_INTERVENED verdict.

    Configuration:
        guardrails:
          - guardrail_name: salt-security
            litellm_params:
              guardrail: salt_security
              api_key: os.environ/SALT_API_KEY
              mode: pre_call
              default_on: true
    """

    _DEFAULT_API_BASE = "https://guardrail.salt.security"

    def __init__(
        self,
        api_key: str | None = None,
        api_base: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            api_base=api_base or os.environ.get("SALT_API_BASE") or self._DEFAULT_API_BASE,
            api_key=api_key or os.environ.get("SALT_API_KEY"),
            **kwargs,
        )
