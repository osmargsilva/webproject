class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.salto = 0

    def extrado(self):
        return f' seu saldo é R${self.salto:,.2f}'

    def depositar(self, deposito):
        self.salto += deposito
    
    def sacar(self, saque):
        if self.salto >= saque:
            self.salto -=  saque
            return f"Saque realizado com successo no valor R${saque:,.2f}"
        else:
            return self.extrado()
    

conta_a = ContaCorrente("osmar", "123456789")

conta_a.depositar(750.50)

print(conta_a.extrado())
print(conta_a.sacar(790))
