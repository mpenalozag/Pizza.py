from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATHS import COMBO_FAMILIAR, BOTON_ARMA_TU_PIZZA, SUPER_PEPPERONI, MASA_DELGADA, BOTON_SIGUIENTE, \
	PALITOS_DE_AJO, COCA_ZERO, INPUT_DIRECCION, SELECCIONAR_DIRECCION, NUMERO_DEPTO, BOTON_CONFIRMAR, CONTINUAR_PAGO, \
	INPUT_NOMBRE, INPUT_MAIL, INPUT_TELEFONO, WEB_PAY, CONFIRMACION_FINAL, TARJETA_DEBITO, SELECCION_BANCO, SANTANDER, \
	INPUT_TARJETA, INPUT_4D, BOTON_CONTINUAR_FINAL, BOTON_ACEPTAR_FINAL, C1, C2, C3, INPUT_C1, INPUT_C2, INPUT_C3, TERMINAR_PEDIDO
from datos_personales import DIRECCION, NUMERO_HOGAR, NOMBRE, MAIL, TELEFONO, NUMERO_TARJETA, NUM_4, MATRIZ, \
								A ,B, C, D, E, F, G, H, I, J
import time
# EL CODIGO POR AHORA ES SOLO PARA PEDIR PROMOCION DE SUPPER PEPPERONI CON PALITOS DE AJ Y COCA ZERO


class CompraPizza:
	def __init__(self, url):
		self.driver = webdriver.Chrome('chromedriver.exe')
		self.driver.get(url)
		self.driver.wait = WebDriverWait(self.driver, 10)

	def usar_boton(self, xpath):
		boton = self.driver.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
		boton.click()

	def rellenar_form(self, xpath, keys):
		rellenamiento = self.driver.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
		rellenamiento.send_keys(keys)

	def conseguir_texto(self, xpath):
		elemento = self.driver.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
		return elemento.text

	def rellenar_coordenada(self, xpath, texto):
		if texto[0] == 'A':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][A])
			print(MATRIZ[int(texto[1])-1][A])
		if texto[0] == 'B':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][B])
			print(MATRIZ[int(texto[1])-1][B])
		if texto[0] == 'C':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][C])
			print(MATRIZ[int(texto[1])-1][C])
		if texto[0] == 'D':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][D])
			print(MATRIZ[int(texto[1])-1][D])
		if texto[0] == 'E':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][E])
			print(MATRIZ[int(texto[1])-1][E])
		if texto[0] == 'F':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][F])
			print(MATRIZ[int(texto[1])-1][F])
		if texto[0] == 'G':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][G])
			print(MATRIZ[int(texto[1])-1][G])
		if texto[0] == 'H':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][H])
			print(MATRIZ[int(texto[1])-1][H])
		if texto[0] == 'I':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][I])
			print(MATRIZ[int(texto[1])-1][I])
		if texto[0] == 'J':
			self.rellenar_form(xpath, MATRIZ[int(texto[1])-1][J])
			print(MATRIZ[int(texto[1])-1][J])

	def comprar_promocion_familiar_pepperoni(self, xpath):
		boton_pizza = self.driver.wait.until(
			EC.presence_of_element_located((By.XPATH, xpath)))
		boton_pizza.click()
		self.usar_boton(BOTON_ARMA_TU_PIZZA)
		self.usar_boton(SUPER_PEPPERONI)
		self.usar_boton(MASA_DELGADA)
		self.usar_boton(BOTON_SIGUIENTE)
		self.usar_boton(PALITOS_DE_AJO)
		self.usar_boton(BOTON_SIGUIENTE)
		self.usar_boton(COCA_ZERO)
		self.usar_boton(BOTON_SIGUIENTE)
		self.rellenar_form(INPUT_DIRECCION, DIRECCION)
		self.usar_boton(SELECCIONAR_DIRECCION)
		self.rellenar_form(NUMERO_DEPTO, NUMERO_HOGAR)
		self.usar_boton(BOTON_CONFIRMAR)
		boton_confirmar_pago = self.driver.wait.until(EC.presence_of_element_located((By.XPATH, CONTINUAR_PAGO)))
		time.sleep(1)
		boton_confirmar_pago.click()
		self.rellenar_form(INPUT_NOMBRE, NOMBRE)
		self.rellenar_form(INPUT_MAIL, MAIL)
		self.rellenar_form(INPUT_TELEFONO, TELEFONO)
		self.usar_boton(WEB_PAY)
		self.usar_boton(CONFIRMACION_FINAL)
		self.driver.wait = WebDriverWait(self.driver, 20)
		self.usar_boton(TARJETA_DEBITO)
		self.usar_boton(SELECCION_BANCO)
		self.usar_boton(SANTANDER)
		self.rellenar_form(INPUT_TARJETA, NUMERO_TARJETA)
		self.usar_boton(BOTON_CONTINUAR_FINAL)
		self.rellenar_form(INPUT_4D, NUM_4)
		self.usar_boton(BOTON_ACEPTAR_FINAL)
		texto_c1 = self.conseguir_texto(C1)
		texto_c2 = self.conseguir_texto(C2)
		texto_c3 = self.conseguir_texto(C3)
		self.rellenar_coordenada(INPUT_C1, texto_c1)
		self.rellenar_coordenada(INPUT_C2, texto_c2)
		self.rellenar_coordenada(INPUT_C3, texto_c3)
		self.usar_boton(TERMINAR_PEDIDO)
		



comprador_pizza = CompraPizza('http://papajohns.cl')
comprador_pizza.comprar_promocion_familiar_pepperoni(COMBO_FAMILIAR)
