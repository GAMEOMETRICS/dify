from typing import Any

from core.tools.errors import ToolProviderCredentialValidationError
from core.tools.provider.builtin.latexprocess.tools.generate import LatexGenerationTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class LatexProcessProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            LatexGenerationTool().invoke(
                user_id="",
                tool_parameters={"latex_string": 'x_2'},
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))