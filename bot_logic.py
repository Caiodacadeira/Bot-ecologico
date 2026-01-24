def rs_funcao(r):
  rs_lista = [
        '♻️ Repensar ➡️ Pensar duas vezes antes de comprar algo, levando em conta a sua necessidade, seu ciclo de vida e os impactos que pode causar na natureza. Ex: repensar sobre o uso de um canudo de plástico em lanchonetes.',
        '♻️ Reduzir ➡️ Diminuir o consumo de produtos e recursos naturais, evitando desperdícios. Ex: reduzir o uso de sacolas plásticas ao fazer compras.',
        '♻️ Reutilizar ➡️ Dar uma nova utilidade a um produto ou material, prolongando sua vida útil e evitando que ele se torne lixo. Ex: reutilizar potes de vidro como recipientes para armazenamento de alimentos.',
        '♻️ Reciclar ➡️ Transformar materiais usados em novos produtos, por meio da organização do lixo, evitando o consumo de recursos naturais e a geração de resíduos. Ex: separar o lixo reciclável do orgânico e destiná-lo corretamente.',
        '♻️ Recusar ➡️ Evitar o consumo de produtos que causam impactos negativos ao meio ambiente, optando por alternativas mais sustentáveis. Ex: recusar embalagens desnecessárias ao fazer compras.',
        '♻️ Restaurar ➡️ Recuperar ecossistemas degradados, promovendo a biodiversidade e os serviços ambientais. Ex: participar de projetos de reflorestamento ou limpeza de praias.',
        '♻️ Reparar ➡️ Consertar objetos ou equipamentos ao invés de descartá-los, reduzindo a geração de resíduos e o consumo de novos produtos. Ex: levar roupas para serem consertadas ao invés de comprar novas.',
        '♻️ Redesenhar ➡️ Criar produtos e processos que sejam mais sustentáveis, considerando todo o ciclo de vida e os impactos ambientais. Ex: desenvolver embalagens biodegradáveis ou reutilizáveis.',
        '♻️ Responsabilizar-se ➡️ Assumir a responsabilidade pelos impactos ambientais das nossas ações, adotando práticas mais conscientes e sustentáveis no dia a dia. Ex: reduzir o consumo de energia elétrica e água em casa.',
        '♻️ Reeducar ➡️ Promover a conscientização e a educação ambiental, incentivando mudanças de comportamento em prol da sustentabilidade. Ex: participar de campanhas de sensibilização sobre o consumo consciente.',
    ]
  if r > 0 and r <= 10:
    return rs_lista[r-1]
  elif r == 11:
    return '🌱 Antigamente chamados de 3 Rs, com a adição de mais 7 Rs com o passar do tempo, os Rs da sustentabilidade são: Repensar, Reduzir, Reutilizar, Reciclar, Recusar, Restaurar, Reparar, Redesenhar, Responsabilizar-se e Reeducar. Eles representam práticas e atitudes que visam promover a sustentabilidade e a preservação do meio ambiente, incentivando a redução do consumo, o reaproveitamento de materiais e a conscientização sobre os impactos ambientais das nossas ações🌳.'
  elif r == 12:
    return '\n\n'.join(rs_lista)
  else:
    return '⚠️⚠️ Número inválido. Por favor, insira um número entre 1 e 10, 11 para explicar a existência dos Rs ou 12 para mostrar todos os Rs ⚠️⚠️.'
