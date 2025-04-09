from fastapi import FastAPI
from Comum.LLM.llm_model import LLM_Model
from Comum.LLM.llm import LLM

app = FastAPI()
llm = LLM(LLM_Model.ChatGPT())

@app.get("/pergunta/{pergunta}")
def read_root(pergunta: str):
    resposta = llm.set_prompt(f"{pergunta}").go()
    return {"message": f"Resposta:, {resposta}!"}
