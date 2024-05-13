/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32l0xx_it.h"
#include <math.h>

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */
//variables de protocolo MOSI
int CS_now = 0;
int CS_old = 0;
int SCLK_now = 0;
int SCLK_old = 0;

//Variables de ejecucion
int value = 0;
int bit_index = 0;
int data[32];
int response_to_rasp[32];  //este sera el vector de salida hacia la rasp siempre
int sync_in[32] = {1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0};
int sync_out[32] ={0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1};
int test = 0;
int measure = 0;
bool executing_test = false;  // esta variable es muy muy importante, porque hay muchas partes del flujo que dependen de esto,
					  // por ejemplo el comportamiento del trato que se le da al chip select, o a la toma de instrucciones
int data_ready = 0; // we use this varibale to check if we have the 32 bits from the rasp
int response_ready = 0;// we use this variable to check if we want to send something back to the rasp, or if everything is set up

//MCPs variables
//VELM
int velm_Time_variable = 0;
volatile uint32_t velm_time_old = 0;
volatile uint32_t velm_time_new = 0;
int velm_Current_variable = 0;
int velm_Voltage_variable = 0;
int velm_Power_variable = 0;
char velm_test[];

//BTM





//SAM







//int volt_measure[1080] = {0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA2,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA2,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA1,0xA1,0xA1,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA0,0xA0,0xA0,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA4,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA4,0xA4,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA4,0xA3,0xA3,0xA4,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA3,0xA3,0xA3,0xA3,0xA3,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA3,0xA4,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA3,0xA3,0xA3,0xA3,0xA3,0xA3,0xA2,0xA3,0xA3,0xA2,0xA2,0xA2,0xA2,0xA2,0xA2,0xA2,0xA2,0xA1,0xA2,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA1,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9F,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9D,0x9E,0x9E,0x9D,0x9E,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9D,0x9C,0x9C,0x9C,0x9C,0x9D,0x9D,0x9D,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9D,0x9D,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9C,0x9B,0x9C,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9B,0x9A,0x9B,0x9B,0x9B,0x9B,0x9A,0x9B,0x9B,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x99,0x9A,0x99,0x99,0x99,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x9A,0x99,0x99,0x9A,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x99,0x98,0x99,0x99,0x99,0x99,0x98,0x99,0x99,0x99,0x99,0x99,0x99,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x99,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x98,0x99,0x99,0x9C,0x9D,0x9D,0x9E,0x9E,0x9D,0x9D,0x9D,0x9D,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9E,0x9D,0x9E,0x9D,0x9D,0x9D,0x9C,0x9C,0x9B,0x9B,0x9A,0x9B,0x9B,0x9C,0x9D,0x9D,0x9E,0x9E,0x9E,0x9E,0x9F,0xA0,0xA0,0xA0,0xA0,0xA1,0xA0,0xA0,0xA0,0x9F,0x9F,0x9F,0xA0,0xA1,0xA1,0xA1,0xA2,0xA1,0xA1,0xA1,0xA1,0xA1,0xA0,0xA0,0xA0,0x9F,0x9F,0x9E,0x9D,0x9D,0x9D,0x9D,0x9E,0x9F,0x9F,0xA0,0xA1,0xA1,0xA1,0xA2,0xA1,0xA2,0xA2,0xA3,0xA3,0xA3,0xA2,0xA2,0xA2,0xA2,0xA2,0xA2,0xA3,0xA3,0xA4,0xA4,0xA4,0xA4,0xA3,0xA3,0xA3,0xA3,0xA3,0xA2,0xA2,0xA2,0xA1,0xA0,0xA0,0xA0,0xA0,0xA0,0xA1,0xA1,0xA2,0xA2,0xA3,0xA3,0xA4,0xA4,0xA4,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA4,0xA4,0xA3,0xA3,0xA3,0xA3,0xA3,0xA3,0xA3,0xA3,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA4,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5,0xA5};
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */

  while (1)
	{
    if(executing_test){
    	//Missing logic to iterate or keep generating the response throghout the test sequence

    }
    else{
      Velm_CS_handler();
      SAM_CS_handler();
      BTM_CS_handler();
	}
}
  // yo acabo de decir que voy a mandar el sync_out siempre que algo este listo

  // el otro problema es que estoy pensando solo en las intrucciones, tengo que enviar datos periodiocos de el estado de la ejecucion
  // creo que se va a necesitar una variable ahi que tambien itere, para
  // esa varible va a depender del execute_test, entonces, hasta que yo no tenga el execute test, yo no voy a enviar datos que no sean
  // como confirmaciones digamos, entonces, al principio, no hace daño eso de estar enviando el response

  void instruction_handler(unsigned int DataIn[], int lenght){
      int i;
      //check for sync in
      if (compararArrays(DataIn, sync_in,lenght)){
          response_to_rasp = sync_out;
          return;
      }
      //check for reset
      if (DataIn[30] && DataIn[29]) {
          // Se inicializan todos los valores
          response_to_rasp = sync_out;
          return;
      }
      //check for start executing
      if (DataIn[30] && !DataIn[29]) {
          // execute_test == 1
          response_to_rasp = sync_out;
          return;
      }
      //check for set parameters
      if (!DataIn[30] && DataIn[29]) {
          decomposer_for_velm(DataIn);
          response_to_rasp = sync_out;
          return;
      }
  }

  void Velm_CS_handler(){
  	//In here we check for chip select, so that if is low, we can get the bits and communicate
		CS_now = HAL_GPIO_ReadPin(GPIOB, CS); //CS FOR VELM SHOULD BE CS0 - PB6
		if (CS_now == 0 && CS_old == 1){
  		//In this first while what we want to do is get the 32 bit instruction
			while (1){
	    		SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
	    		CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					value = HAL_GPIO_ReadPin(GPIOA, MOSI);
					data[bit_index] = value;
					bit_index ++;
					if (bit_index == 31){
						data_ready=1;
						break;
					}
					SCLK_old = SCLK_now;
					CS_old = CS_now;
				}
			}
  		//In this second while we have the instruction ready to take action
  		// Would it make sense to just send 32 bit from the rasp, wait for confirmation, and after that send again and again ....
	    	while (1){
				SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
				CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					value = HAL_GPIO_ReadPin(GPIOA, MOSI);
					if (data_ready==1){
						//aca tengo que hacer primero la comprobacion de los vectores
						//si aca pongo una funcion que agarre todo data y vaya comparando con los valores de las instrucciones
						instruction_handler(data,31);
						response_ready = 1;
					//cuando se puede poner el break?
					}
					SCLK_old = SCLK_now;
					CS_old = CS_now;
				}
	   		}
        //la idea de este ultimo while seria responder a la rasp, entonces en el anterior podriamos haber seteado condiciones que se
        //van a procesar por aca
        	while (1){
				SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
				CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					if(response_ready ==1){
						write_miso(response[response_bit_index]);
						if(response_bit_index == 31){
							break;
						}
					}
				SCLK_old = SCLK_now;
				CS_old = CS_now;
        		}
	  		}

		}

  }

  void SAM_CS_handler(){
  	//In here we check for chip select, so that if is low, we can get the bits and communicate
		CS_now = HAL_GPIO_ReadPin(GPIOB, CS);  //CS FOR SAM SHOULD BE CS1 - PB5
		if (CS_now == 0 && CS_old == 1){
  		//In this first while what we want to do is get the 32 bit instruction
			while (1){
	    		SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
	    		CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					value = HAL_GPIO_ReadPin(GPIOA, MOSI);
					data[bit_index] = value;
					bit_index ++;
					if (bit_index == 31){
						data_ready=1;
						break;
					}
					SCLK_old = SCLK_now;
					CS_old = CS_now;
				}
			}
  		//In this second while we have the instruction ready to take action
  		// Would it make sense to just send 32 bit from the rasp, wait for confirmation, and after that send again and again ....
	    	while (1){
				SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
				CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					value = HAL_GPIO_ReadPin(GPIOA, MOSI);
					if (data_ready==1){
						//aca tengo que hacer primero la comprobacion de los vectores
						//si aca pongo una funcion que agarre todo data y vaya comparando con los valores de las instrucciones
						instruction_handler(data,31);
						response_ready = 1;
					//cuando se puede poner el break?
					}
					SCLK_old = SCLK_now;
					CS_old = CS_now;
				}
	   		}
        //la idea de este ultimo while seria responder a la rasp, entonces en el anterior podriamos haber seteado condiciones que se
        //van a procesar por aca
        	while (1){
				SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
				CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					if(response_ready ==1){
						write_miso(response[response_bit_index]);
						if(response_bit_index == 31){
							break;
						}
					}
				SCLK_old = SCLK_now;
				CS_old = CS_now;
        		}
	  		}

		}

  }

  void BTM_CS_handler(){
  	//In here we check for chip select, so that if is low, we can get the bits and communicate
		CS_now = HAL_GPIO_ReadPin(GPIOB, CS);  //CS FOR BTM SHOULD BE CS2 - PB4
		if (CS_now == 0 && CS_old == 1){
  		//In this first while what we want to do is get the 32 bit instruction
			while (1){
	    		SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
	    		CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					value = HAL_GPIO_ReadPin(GPIOA, MOSI);
					data[bit_index] = value;
					bit_index ++;
					if (bit_index == 31){
						data_ready=1;
						break;
					}
					SCLK_old = SCLK_now;
					CS_old = CS_now;
				}
			}
  		//In this second while we have the instruction ready to take action
  		// Would it make sense to just send 32 bit from the rasp, wait for confirmation, and after that send again and again ....
	    	while (1){
				SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
				CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					value = HAL_GPIO_ReadPin(GPIOA, MOSI);
					if (data_ready==1){
						//aca tengo que hacer primero la comprobacion de los vectores
						//si aca pongo una funcion que agarre todo data y vaya comparando con los valores de las instrucciones
						instruction_handler(data,31);
						response_ready = 1;
					//cuando se puede poner el break?
					}
					SCLK_old = SCLK_now;
					CS_old = CS_now;
				}
	   		}
        //la idea de este ultimo while seria responder a la rasp, entonces en el anterior podriamos haber seteado condiciones que se
        //van a procesar por aca
        	while (1){
				SCLK_now = HAL_GPIO_ReadPin(GPIOA, SCLK);
				CS_now = HAL_GPIO_ReadPin(GPIOB, CS);
				if(SCLK_now == 1 && SCLK_old == 0){
					if(response_ready ==1){
						write_miso(response[response_bit_index]);
						if(response_bit_index == 31){
							break;
						}
					}
				SCLK_old = SCLK_now;
				CS_old = CS_now;
        		}
	  		}

		}

  }

  void decomposer_for_velm(unsigned int InstBits[]){
      unsigned int upperBits = (InstBits[0] >> 25) & 0xF; // bits 28 a 25
      unsigned int lowerBits = InstBits[0] & 0x1F; // bits 24 a 0
      unsigned int testBits = InstBits[0] & 0xF; // bits 3 a 0

      if(upperBits == 0x1){
          velm_Time_variable = lowerBits;
      }
      if(upperBits == 0x3){
          velm_Current_variable = lowerBits;
      }
      if(upperBits == 0x4){
          velm_Voltage_variable = lowerBits;
      }
      if(upperBits == 0x5){
          velm_power_variable = lowerBits;
      }
      if(upperBits == 0x2){
          if(testBits == 0x0){
              velm_test=not_tested;
          }
          if(testBits == 0x1){
              velm_test=emulate;
          }
          if(testBits == 0x2){
              velm_test=measure_voltage;
          }
          if(testBits == 0x3){
              velm_test=measure_current;
          }
          if(testBits == 0x4){
              velm_test=measure_power;
          }
      }
  }


  // Definición de la función
  bool compararArrays(unsigned int array1[], unsigned int array2[], int longitud) {
      int i;
      for (i = 0; i < longitud; i++) {
          if (array1[i] =! array2[i]) {
              return false;
          }
      }
      return true;
  }

  double calculate_Is(double Irs, double Tc, double Tref, double q, double Eg, double n, double K) {
      double exponent = (q * Eg / (n * K)) * (1 / Tref - 1 / Tc);
      double Is = Irs * pow(Tc / Tref, 3) * exp(exponent);
      return Is;
  }
  ￼
double calculate_SAM_Current(int SAM_Temperature, int SAM_Irradiance, int SAM_Voltage){
	  //%I = sam_I_SC + sam_K_I * (sam_T_C - sam_T_Ref) * sam_Irradiance / sam_base_Irr - sam_I_S *exp(sam_V + sam_I *)


	  //int sam_exp_den =
  }





/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_MSI;
  RCC_OscInitStruct.MSIState = RCC_MSI_ON;
  RCC_OscInitStruct.MSICalibrationValue = 0;
  RCC_OscInitStruct.MSIClockRange = RCC_MSIRANGE_5;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_MSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USART2;
  PeriphClkInit.Usart2ClockSelection = RCC_USART2CLKSOURCE_PCLK1;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  huart2.Init.OneBitSampling = UART_ONE_BIT_SAMPLE_DISABLE;
  huart2.AdvancedInit.AdvFeatureInit = UART_ADVFEATURE_NO_INIT;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
/* USER CODE BEGIN MX_GPIO_Init_1 */
/* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(MISO_GPIO_Port, MISO_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : SCLK_Pin MOSI_Pin */
  GPIO_InitStruct.Pin = SCLK_Pin|MOSI_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pin : MISO_Pin */
  GPIO_InitStruct.Pin = MISO_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(MISO_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : CS_Pin */
  GPIO_InitStruct.Pin = CS_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(CS_GPIO_Port, &GPIO_InitStruct);

/* USER CODE BEGIN MX_GPIO_Init_2 */

/* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */
void int_2_array(int voltage, int current, int power)
{
	// Voltage slot
    response[15] = voltage & 0b1;
    response[14] = (voltage >> 1) & 0b1;
    response[13] = (voltage >> 2) & 0b1;
    response[12] = (voltage >> 3) & 0b1;
    response[11] = (voltage >> 4) & 0b1;
    response[10] = (voltage >> 5) & 0b1;
    response[9] = (voltage >> 6) & 0b1;
    response[8] = (voltage >> 7) & 0b1;
    // Current slot
    response[23] = current & 0b1;
    response[22] = (current >> 1) & 0b1;
    response[21] = (current >> 2) & 0b1;
    response[20] = (current >> 3) & 0b1;
    response[19] = (current >> 4) & 0b1;
    response[18] = (current >> 5) & 0b1;
    response[17] = (current >> 6) & 0b1;
    response[16] = (current >> 7) & 0b1;
    // Power slot
    response[31] = power & 0b1;
    response[30] = (power >> 1) & 0b1;
    response[29] = (power >> 2) & 0b1;
    response[28] = (power >> 3) & 0b1;
    response[27] = (power >> 4) & 0b1;
    response[26] = (power >> 5) & 0b1;
    response[25] = (power >> 6) & 0b1;
    response[24] = (power >> 7) & 0b1;
}

void write_miso(int bit_state){
  if(bit_state == 0){
	  HAL_GPIO_WritePin(GPIOA, MISO, 0);
  }
  if(bit_state == 1){
	  HAL_GPIO_WritePin(GPIOA, MISO, 1);
  }
}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
