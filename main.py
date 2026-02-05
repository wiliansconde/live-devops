from fastapi import FastAPI, HTTPException
import logging


app = FastAPI(title="Calculadora API")

logger = logging.getLogger("Calc Logger")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
           )

@app.get("/")
def root():
    logger.info("v11.2 Endpoint root chamado")
    return {
        "message": "v11.2 API de Calculadora no ar",
        "operations": ["soma", "subtracao", "multiplicacao", "divisao"]
    }

@app.get("/health")
def health():
    logger.info("Chamando health... testando o logs")
    return {"status": "ok"}

@app.get("/soma")
def soma(a: float, b: float):
    logger.info("olha o valor de a:" + str(a))
    logger.info("olha o valor de b:" + str(b))
    return {"resultado": a + b}


@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": a - b}

@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": a * b}

@app.get("/divisao")
def divisao(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Divisao por zero nao permitida")
    return {"resultado": a / b}

