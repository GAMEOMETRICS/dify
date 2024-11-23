from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage

from typing import Any, Dict, List, Union

class LatexGenerationTool(BuiltinTool):

    def _invoke(
        self,
        user_id: str,
        tool_parameters: dict[str, Any],
    ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        """
        invoke tools
        """

        #获得latex字符串参数
        latex = tool_parameters.get('latex_string','')

        if not latex:
            return self.create_text_message('Invalid latex string')
        
        image_url  = f'https://latex.codecogs.com/svg.image?{latex}'

        return self.create_image_message(image_url)
    

