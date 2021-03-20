import os


def options():
  op_graphic = 0
  op_analysis = 0
  while True:
    os.system('clear') or None
    print(f'---- ANALISE FRAPI TECH CORE ----')
    print()
    print('[1] - Grafico FAR')
    print('[2] - Grafico FRR')
    print('[3] - Grafico Cruzado FAR_FRR')
    op_graphic = int(input('Digite a opcao: '))
    
    if op_graphic > 0 and op_graphic < 4:
      break

  while True:
    os.system('clear') or None
    print(f'---- TIPO DE ANALISE ----')
    print('[1] - analisa arquivo de score (2 segundos)')
    print('[2] - realizar nova analise via Api (5 minutos)')
    print('      obs: voce deve estar conectado a VPN')
    print()
    op_analysis = int(input('Digite a opcao: '))
    
    if op_analysis > 0 and op_analysis < 3:
      break
  
  return op_graphic, op_analysis
