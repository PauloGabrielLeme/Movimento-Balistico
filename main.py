#RA:24.223.081-1 Gianluca Rabesquini Marcelino da Silva
#RA:24.223.085-2 Lorenzo Colonnese Chiganças 
#RA:24.123.075-4 Paulo Gabriel Gonçalves Leme

import math
print("\n")
print("Movimento Balístico")
print("\n")


def menu():
  print("1. Calcular a velocidade inicial de X e Y")
  print("2. Calcular o tempo que permanece no ar")
  print("3. Posição no instante")
  print("4. Velocidade instantanea")
  print("5. Altura Maxima")
  print("6. Alcance Horizontal")
  print("7. Velocidade antes alcancar o solo")
  print("8. Velocidade no instante da altura maxima")
  print("9. Distancia Horizontal de Objeto Em Queda Livre")
  print("10. Velocidade de um objeto arremessado sem angulo")
  print("11. Sair")

def vel_inicial():
  L = input("O V0 está em KM/H ou em M/S: ")
  if L == "KM/H" or L == "km/h":
    v0 = float(input("Digite o Valor de V0 em km/h: "))
    a = math.radians(float(input("Digite o valor do ângulo em graus: ")))
    v0x = v0 * math.cos(a) / 3.6  
    v0y = v0 * math.sin(a) / 3.6  
    print("\n")
    print("A velocidade inicial de X é: ", v0x)
    print("A velocidade inicial de Y é: ", v0y)
    print("\n")
  if L == "M/S" or L == "m/s":
    v0 = float(input("Digite o Valor de V0 em m/s: "))
    a = math.radians(float(input("Digite o valor do ângulo em graus: ")))
    v0x = v0 * math.cos(a)
    v0y = v0 * math.sin(a)
    print("\n")
    print("A velocidade inicial de X é: ", v0x)
    print("A velocidade inicial de Y é: ", v0y)
    print("\n")
  else:
    print("Digite uma opção válida")
    print("\n")
    vel_inicial()


def kph_to_mps(speed_kph):
  return speed_kph / 3.6
def tempo_ar():
  y = float(input("Digite a posição vertical final da Bola: "))
  y0 = float(input("Digite a posição vertical inicial da Bola: "))
  L = input("O V0 está em KM/H ou em M/S: ")
  if L == 'm/s' or L == "M/S":
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))
  elif L == 'km/h' or L == "KM/H":
      v0_kph = float(input("Insira a velocidade inicial da bola (em km/h): "))
      v0 = kph_to_mps(v0_kph)
  else:
      print("Opção inválida. Utilizando m/s como padrão.")
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))

  a = float(input("Digite o ângulo de lançamento da Bola em graus: "))
  a_rad = math.radians(a)
  v0y = v0 * math.sin(a_rad)
  g = 9.8
  a_quad = -0.5 * g
  b_quad = v0y
  c_quad = y0 - y
  delta = b_quad**2 - 4*a_quad*c_quad
  if delta < 0:
      print("A bola não chegou na posição final.")
      return None
  else:
      t1 = (-b_quad + math.sqrt(delta)) / (2*a_quad)
      t2 = (-b_quad - math.sqrt(delta)) / (2*a_quad)
      tempo_total = max(t1, t2)
      print("\n")
      print("O tempo que a bola fica no ar é aproximadamente", tempo_total, "segundos.")
      print("\n")
      return tempo_total




def mps_to_kph(speed_mps):
    return speed_mps * 3.6
def posicao_instante():
    y0 = float(input("Posição vertical inicial da bola (em metros): "))
    L = input("O V0 está em KM/H ou em M/S:  ")
    if L == 'm/s' or L == "M/S":
        v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))
        v0_kph = mps_to_kph(v0)
    elif L == 'km/h' or L == "KM/H":
        v0_kph = float(input("Insira a velocidade inicial da bola (em km/h): "))
        v0 = v0_kph / 3.6
    else:
        print("Opção inválida. Utilizando m/s como padrão.")
        v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))
        v0_kph = mps_to_kph(v0)
    a = float(input("Ângulo de lançamento da bola (em graus): "))
    t = float(input("Tempo no instante desejado (em segundos): "))
    a_rad = math.radians(a)
    v0x = v0 * math.cos(a_rad)
    x = v0x * t
    v0y = v0 * math.sin(a_rad)
    g = 9.8
    y = y0 + v0y * t - 0.5 * g * t**2
    print("\n")
    print("A posição horizontal da bola no instante", t,"segundos é mais ou menos:", x, "metros.")
    print("A posição vertical da bola no instante", t,"segundos é mais ou menos:", y, "metros.")
    print("A velocidade inicial da bola é de aproximadamente", v0_kph, "km/h.")
    print("\n")
    return x, y


def vel_instantanea():
  L = input("O V0 está em KM/H ou em M/S:  ")
  if L == 'm/s' or L == "M/S":
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))
  elif L == 'km/h' or L == "KM/H":
      v0_kph = float(input("Insira a velocidade inicial da bola (em km/h): "))
      v0 = kph_to_mps(v0_kph)
  else:
      print("Opção inválida. Utilizando m/s como padrão.")
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))

  a = float(input("Digite o ângulo de lançamento da Bola em graus: "))
  t = float(input("Digite o instante de tempo em segundos: "))
  a_rad = math.radians(a)
  v0x = v0 * math.cos(a_rad)
  v0y = v0 * math.sin(a_rad) - 9.8 * t
  v_resultante = math.sqrt(v0x**2 + v0y**2)
  print("\n")
  print("Velocidade resultante:", v_resultante, "m/s")
  print("Componente da velocidade no eixo x:", v0x, "m/s")
  print("Componente da velocidade no eixo y:", v0y, "m/s")
  print("\n")

def alt_maxima():
  y0 = float(input("Digite a posição vertical inicial da Bola (em metros): "))
  L = input("O V0 está em KM/H ou em M/S:  ")
  if L.upper() == 'M/S':
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))
  elif L.upper() == 'KM/H':
      v0_kph = float(input("Insira a velocidade inicial da bola (em km/h): "))
      v0 = kph_to_mps(v0_kph)
  else:
      print("Opção inválida. Utilizando m/s como padrão.")
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))

  a = float(input("Digite o ângulo de lançamento da Bola em graus: "))
  a_rad = math.radians(a)
  v0y = v0 * math.sin(a_rad)
  t_max = v0y / 9.8
  y_max = y0 + v0y * t_max - 0.5 * 9.8 * t_max**2
  print("\n")
  print("A altura máxima atingida pela bola é:", y_max, "metros.")
  print("\n")

def alc_horizontal():
    y0 = float(input("Digite a posição vertical inicial da Bola (em metros): "))
    L = input("O V0 está em KM/H ou em M/S:  ")
    if L.upper() == 'M/S':
        v0 = float(input("Digite a velocidade inicial da Bola (em m/s): "))
    elif L.upper() == 'KM/H':
        v0_kph = float(input("Digite a velocidade inicial da Bola (em km/h): "))
        v0 = kph_to_mps(v0_kph)
    else:
        print("Opção inválida. Utilizando m/s como padrão.")
        v0 = float(input("Digite a velocidade inicial da Bola (em m/s): "))

    a = float(input("Digite o ângulo de lançamento da Bola em graus: "))
    a_rad = math.radians(a)

    v0x = v0 * math.cos(a_rad)

    v0y = v0 * math.sin(a_rad)
    t_total = (-v0y - math.sqrt(v0y**2 - 4*(-4.9)*y0)) / (-9.8)

    alcance = v0x * t_total

    print("\n")
    print("O alcance horizontal da bola é aproximadamente", alcance, "metros.")
    print("\n")

def vel_solo():
  y0 = float(input("Digite a posição vertical inicial da Bola (em metros): "))
  L = input("O V0 está em KM/H ou em M/S:  ")
  if L.upper() == 'M/S':
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))
  elif L.upper() == 'KM/H':
      v0_kph = float(input("Insira a velocidade inicial da bola (em km/h): "))
      v0 = kph_to_mps(v0_kph)
  else:
      print("Opção inválida. Utilizando m/s como padrão.")
      v0 = float(input("Insira a velocidade inicial da bola (em m/s): "))

  a = float(input("Digite o ângulo de lançamento da Bola em graus: "))
  a_rad = math.radians(a)

  v0x = v0 * math.cos(a_rad)
  v0y = v0 * math.sin(a_rad)

  t_total = (-v0y - math.sqrt(v0y**2 - 4*(-4.9)*y0)) / (-9.8)
  v_solo_x = v0x
  v_solo_y = v0y - 9.8 * t_total
  v_solo = math.sqrt(v_solo_x**2 + v_solo_y**2)

  print("\n")
  print("Componente da velocidade no eixo x:", v_solo_x, "m/s")
  print("Componente da velocidade no eixo y:", v_solo_y, "m/s")
  print("Magnitude da velocidade:", v_solo, "m/s")
  print("\n")


def vel_alt_max():
  y0 = float(input("Digite a posição vertical inicial da Bola (em metros): "))
  L = input("O V0 está em KM/H ou em M/S:  ")
  if L.upper() == 'M/S':
      v0 = float(input("Digite a velocidade inicial da Bola (em m/s): "))
  elif L.upper() == 'KM/H':
      v0_kph = float(input("Digite a velocidade inicial da Bola (em km/h): "))
      v0 = kph_to_mps(v0_kph)
  else:
      print("Opção inválida. Utilizando m/s como padrão.")
      v0 = float(input("Digite a velocidade inicial da Bola (em m/s): "))

  a = float(input("Digite o ângulo de lançamento da Bola em graus: "))
  a_rad = math.radians(a)
  v0y = v0 * math.sin(a_rad)
  t_max = v0y / 9.8
  y_max = y0 + v0y * t_max - 0.5 * 9.8 * t_max**2

  v_max_x = v0 * math.cos(a_rad)
  v_max_y = v0y - 9.8 * t_max

  v_resultante = math.sqrt(v_max_x**2 + v_max_y**2)

  print("\n")
  print("A velocidade da bola no instante da altura máxima é:", v_resultante, "m/s")
  print("Componente da velocidade no eixo x:", v_max_x, "m/s")
  print("Componente da velocidade no eixo y:", v_max_y, "m/s")
  print("\n")


def dh():
   print("-------------------------------------------")

   d=float(input("Digite A Altura Do Objeto: "))
   v=float(input("Digite A Velocidade do Objeto: "))

   t=((2*d)/9.8)**(1/2)
   d_h = v * (t/3600)

   print("A Distância Horizontal E: %.2f m"%(d_h*1000))

   print("-------------------------------------------")

def arremeso_sem_ang():
    v0 = float(input("Digite a Velocidade Inicial: "))
    altura_alvo = float(input("Digite A Altura Do Alvo: "))
    tempo_voo = float(input("Digite O Tempo No Ar Do Objeto: "))
    v0y = 0
    v0x = v0
    g = -9.8
    y = altura_alvo + (v0y * tempo_voo) + (0.5 * g * tempo_voo ** 2)
    x = v0x * tempo_voo

    print("A Altura do Ponto E %.2f"%(y*100))
    print ("A Distancia do Arremesso foi %.2f"%x)
    print("\n")

while(True):
  menu()
  print("\n")
  opcao = int(input("Digite a opção desejada: "))
  if opcao == 1:
    vel_inicial()
  elif opcao == 2:
    tempo_ar()
  elif opcao == 3:
    posicao_instante()
  elif opcao == 4:
    vel_instantanea()
  elif opcao == 5:
    alt_maxima()
  elif opcao == 6:
    alc_horizontal()
  elif opcao == 7:
    vel_solo()
  elif opcao == 8:
    vel_alt_max()
  elif opcao == 9:
    dh()
  elif opcao == 10:
    arremeso_sem_ang()
  elif opcao == 11:
    break
