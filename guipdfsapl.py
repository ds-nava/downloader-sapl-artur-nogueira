import pandas as pd
import requests
import os
import re
from PyPDF2 import PdfMerger
from tkinter import messagebox
import customtkinter as ctk

# CSV SAPL
url = "https://sapl.arturnogueira.sp.leg.br/materia/pesquisar-materia?format=csv&tipo=&ementa=&numero=&numeracao__numero_materia=&numero_protocolo=&ano=&autoria__autor=&autoria__primeiro_autor=unknown&tipo_listagem=1"
df = pd.read_csv(url, sep=";", engine="python", encoding="utf-8")

# Filtro das opções/ComboBox
separadores = r'\n|,|;| e |/'
# Filtra só quem tem 1 autor (sem separadores")
df_autores_unicos = df[~df['Autorias'].str.contains(separadores, na=False)]
# Cria lista única de autores
lista_autores = sorted(df_autores_unicos['Autorias'].dropna().astype(str).unique().tolist())
# Filtra anos
df_anos = df['Ano']
# Cria lista de anos
lista_anos = sorted(df_anos.dropna().astype(int).astype(str).unique().tolist())
# Filtra tipos de matéria
df_materias = df['Tipo de Matéria Legislativa/Descrição']
# Cria lista de tipos de matéria
lista_materias = sorted(df_materias.dropna().astype(str).unique().tolist()) 

# Função para inserir logs na textbox
def inserir_log(mensagem):
    log_textbox.configure(state="normal")   
    log_textbox.insert(ctk.END,"- "+ mensagem + "\n")
    log_textbox.see(ctk.END)  # Rola para o final do texto
    log_textbox.configure(state="disabled")
    janela.update()

# Função para sanitizar nomes de arquivos/pastas
def sanitize(texto):
    return re.sub(r'[\\/*?:"<>|]', "", str(texto))

# Função que roda quando clicar no botão
def baixar_pdfs(autor_entry, ano_entry, tipo_entry):
    
    # Verifica se todos os filtros foram selecionados
    if autor_entry.get() == "Selecione" or ano_entry.get() == "Selecione" or tipo_entry.get() == "Selecione":
        messagebox.showwarning("Aviso", "Selecione todos os filtros antes de prosseguir.")
        return
        
    # Limpa logs
    log_textbox.configure(state="normal")
    log_textbox.delete("1.0", "end")
    log_textbox.configure(state="disabled")
    
    # Pega valores dos filtros
    autor = autor_entry.get()
    ano = int(ano_entry.get())
    tipo_materia = tipo_entry.get()
      
    # Filtragem
    df_filtro = df[
        (df['Autorias'].str.contains(autor, case=False, na=False)) &
        (df['Ano'] == ano) &
        (df['Tipo de Matéria Legislativa/Descrição'] == tipo_materia) &
        (df['Tipo de Matéria Legislativa/Sigla'])
    ].reset_index(drop=True)

    # Verifica se encontrou resultados
    if df_filtro.empty:
        inserir_log("Nenhum resultado encontrado para os filtros selecionados.")
        messagebox.showwarning("Aviso", "Nenhum resultado encontrado para os filtros selecionados.")
        return    

    # Cria coluna Nome dos arquivos
    df_filtro["nome_arquivo"] = df_filtro.apply(
        lambda row: f"{row['Tipo de Matéria Legislativa/Sigla']} - {row['Ano']} - {row['Número']}.pdf",
        axis=1
    )

    # Pasta para salvar PDFs
    pasta_download = sanitize(f"{tipo_materia} - {ano} - {autor}")
    os.makedirs(pasta_download, exist_ok=True)

    # Mesclador
    merger = PdfMerger()

    inserir_log(f"Iniciando download... ")

    # Loop de download e mesclagem
    for i, row in df_filtro.iterrows():
        url_pdf = row["Texto Original"]
        nome_arquivo = sanitize(row["nome_arquivo"])
        caminho_arquivo = os.path.join(pasta_download, nome_arquivo)
        inserir_log(f"Baixando {i+1}/{len(df_filtro)}: {url_pdf} -> {nome_arquivo}")
        r = requests.get(url_pdf)
        with open(caminho_arquivo, "wb") as f:
            f.write(r.content)
        merger.append(caminho_arquivo)    
       
    # PDF final
    nome_arquivo_final = sanitize(f"{tipo_materia} - {ano} - {autor}.pdf")
    arquivo_final = os.path.join(pasta_download, nome_arquivo_final)
    merger.write(arquivo_final)
    merger.close()

    # Finalizado
    inserir_log("Download e mesclagem concluídos.")
    inserir_log(f"PDF unificado salvo em: {arquivo_final}")
    messagebox.showinfo("Sucesso", f"- PDF unificado salvo em: {arquivo_final}")

# Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("Download de PDFs SAPL")
janela.iconbitmap("icon.ico")

frame = ctk.CTkFrame(janela)
frame.pack(pady=20, padx=20)

# Autor 
label_autor = ctk.CTkLabel(frame, text="Autoria:")
label_autor.grid(row=0, column=0, padx=(10,10), pady=(10,5), sticky="e")

combo_autor = ctk.CTkComboBox(frame, values=lista_autores, width=250)
combo_autor.grid(row=0, column=1, padx=(0,10), pady=(10,5), sticky="w")
combo_autor.set("Selecione") 

# Ano
label_ano = ctk.CTkLabel(frame, text="Ano:")
label_ano.grid(row=1, column=0, padx=(10,10), pady=5, sticky="e")

combo_ano = ctk.CTkComboBox(frame, values=lista_anos, width=250)
combo_ano.grid(row=1, column=1, padx=(0,10), pady=5,  sticky="w")
combo_ano.set("Selecione")

# Tipo de Matéria
label_materias = ctk.CTkLabel(frame, text="Tipo de Matéria:")
label_materias.grid(row=2, column=0, padx=(10,10), pady=5, sticky="e")

combo_materias = ctk.CTkComboBox(frame, values=lista_materias, width=250)
combo_materias.grid(row=2, column=1, padx=(0,10), pady=5,  sticky="w")
combo_materias.set("Selecione")

# Botão
botao = ctk.CTkButton(
    frame,
    text="Baixar PDFs",
    command=lambda: baixar_pdfs(combo_autor, combo_ano, combo_materias)
)
botao.grid(row=3, column=0, columnspan=2, pady=(10,0))

# Textbox para logs
label_log = ctk.CTkLabel(frame, text="Download logs:")
label_log.grid(row=4, column=0, columnspan=2, pady=(10,10))

log_textbox = ctk.CTkTextbox(frame, width=550, height=100)
log_textbox.grid(row=5, column=0, columnspan=2, pady=(0,10), padx=10)   
log_textbox.configure(state="disabled")

janela.mainloop()

