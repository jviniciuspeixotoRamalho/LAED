
def verificar_balanceamento(expressao):
  pilha = []
  mapeamento = {")": "(", "]": "[", "}": "{"}

  for i, char in enumerate(expressao):
    if char in "([{":
      pilha.append((char, i))
    elif char in ")]}":
      if not pilha:
        return (
            False,
            f"Erro na posição {i+1} (índice {i}): Fechador '{char}' sem abridor correspondente.",
        )

      topo_char, topo_pos = pilha.pop()
      if mapeamento[char] != topo_char:
        return (
            False,
            f"Erro na posição {i+1} (índice {i}): Incompatibilidade de tipo. Esperado fechador para '{topo_char}', mas encontrou '{char}'.",
        )

  if pilha:
    topo_char, topo_pos = pilha.pop()
    return (
        False,
        f"Erro no final da expressão: Abridor '{topo_char}' na posição {topo_pos+1} não foi fechado.",
    )

  return True, "Expressão Válida"


cadeias = ["({[]})", "({[]}]", "({[]}[()]{})"]

for c in cadeias:
  valida, msg = verificar_balanceamento(c)
  print(f"Cadeia: {c:<15} | Válida: {valida!s:<5} | Detalhes: {msg}")