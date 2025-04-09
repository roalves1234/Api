from Comum.Models.model_base import ILLM_Model
from Comum.Utils.utils import FileTool

class LLM:
    model: ILLM_Model = None
    
    def __init__(self, model: ILLM_Model = None):
        self.set_model(model)

    def set_model(self, model: ILLM_Model) -> 'LLM':
        self.model = model
        return self

    def set_prompt(self, prompt: str) -> 'LLM':
        self.model.set_prompt(prompt)
        return self

    def go(self) -> str:
        resposta = self.model.get()
        FileTool("llm.md").save(f"{self.model.prompt}\n\n-----------------------------------------------\n\n{resposta}")
        return resposta
