from fastapi import FastAPI
from Comum.LLM.llm_model import LLM_Model
from Comum.LLM.llm import LLM
from Comum.Utils.utils import FileTool

app = FastAPI()
llm = LLM(LLM_Model.ChatGPT())
texto_arquivo = FileTool("Especificacao.txt").load()

@app.get("/pergunta/{pergunta}")
def get_resposta(pergunta: str):
    resposta = llm.set_prompt(f"""
                              Responda em um parágrafo de no máximo 3 linhas a seguinte pergunta: {pergunta} 

                              Tendo como base o seguinte texto:    
                              {texto_arquivo}
                              """).go()
    return {"message": f"Resposta: {resposta}"}

@app.get("/versao")
def get_versao():
    return {"Versão": "001"}