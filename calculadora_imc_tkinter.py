import tkinter as tk
from tkinter import messagebox

def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 39.9:
        return "Obesidade"
    else:
        return "Obesidade grave"

def calcular_e_exibir_resultado():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if peso <= 0 or altura <= 0:
            raise ValueError("Valores devem ser maiores que zero.")
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida! {e}")

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x200")

label_titulo = tk.Label(janela, text="Calculadora de IMC", font=("Arial", 16))
label_titulo.pack(pady=10)

frame_inputs = tk.Frame(janela)
frame_inputs.pack(pady=10)

label_peso = tk.Label(frame_inputs, text="Peso (kg):")
label_peso.grid(row=0, column=0, padx=5, pady=5)
entry_peso = tk.Entry(frame_inputs)
entry_peso.grid(row=0, column=1, padx=5, pady=5)

label_altura = tk.Label(frame_inputs, text="Altura (m):")
label_altura.grid(row=1, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame_inputs)
entry_altura.grid(row=1, column=1, padx=5, pady=5)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular_e_exibir_resultado)
btn_calcular.pack(pady=10)

janela.mainloop()
