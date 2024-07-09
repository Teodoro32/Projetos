import pyautogui
import time
import pandas

pyautogui.PAUSE = 1.4

# Passo 1:
# Abrindo o navegador para acessar o sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2:
# Fazer login
pyautogui.click(x=723, y=378)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")

# Passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("minhasenha")

# Botão de logar
pyautogui.click(x=672, y=551)

time.sleep(3)

# Passo 3:
# Base de dados
tabela = pandas.read_csv("produtos.csv") 
print(tabela) 

# Passo 4:
# Cadastrar o produto
for linha in tabela.index:
    # Codigo   
    pyautogui.click(x=913, y=256)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # Clicar no botao enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) 