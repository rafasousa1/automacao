import pyautogui
import time
import pandas as pd

tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=842, y=360)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste")
pyautogui.press("tab")
pyautogui.press("enter")

for linha in tabela.index:
    pyautogui.click(x=818, y=240)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(-5000)
    time.sleep(1.5)
    pyautogui.scroll(5000)