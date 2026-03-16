# 💳 Sistema Bancário Python V1

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=yellow)
![License](https://img.shields.io/badge/License-MIT-green)

**Sistema bancário completo com persistência JSON, transferências, depósitos e saques validados.**

## ✨ Funcionalidades

- ✅ **Listar contas** (titular + saldo)
- ✅ **Transferência** (valida saldo, contas diferentes)
- ✅ **Depósito** (valor > 0, conta existe)  
- ✅ **Saque** (saldo suficiente)
- 💾 **Persistência automática** (banco.json)
- 🛡️ **Validação total** de entradas

## 🚀 Como Usar

```bash
git clone https://github.com/seuusuario/sistema-bancario-python
cd sistema-bancario-python
python main.py
Contas Demo:

text
1 - Rodrigo (R$500)
2 - Turao (R$2.000)  
3 - Rosineide (R$54.023)
📁 Estrutura
text
sistema-bancario-python/
├── main.py          # Código principal
├── banco.json       # Dados persistidos
└── README.md
