# ATmega128 학습 정리

## 저장소 구성

- `src`: LED, switch, FND, timer, interrupt, PWM, UART, sensor, motor 실습
- `lib/lcd`: LCD 제어 library
- `lib/uart0`: UART0 송수신 helper
- `lib/at25`: external EEPROM 제어
- `lib/sht20`: I2C 온습도 센서 제어
- `CMakeLists.txt`, `Makefile`, `avr-toolchain.cmake`: AVR cross compile 설정

## MCU 프로그램을 읽는 관점

ATmega128 코드는 PC에서 바로 실행하는 프로그램이 아니라 보드에 올라가는 firmware임. 일반 C와 문법은 같지만, 결과가 화면 출력이 아니라 register 값 변경과 pin 출력으로 나타남.

```text
C source -> avr-gcc cross compile -> firmware -> board upload -> hardware 동작
```

그래서 코드를 읽을 때는 “변수 값이 어떻게 바뀌는가”뿐 아니라 “어떤 register bit가 어떤 하드웨어 기능을 켜는가”를 같이 봐야 함.

## GPIO: DDR, PORT, PIN

GPIO는 거의 모든 임베디드 제어의 출발점임.

- `DDRx`: 해당 port의 pin 방향을 정함. `1`이면 출력, `0`이면 입력임.
- `PORTx`: 출력 pin에서는 HIGH/LOW 값을 씀. 입력 pin에서는 pull-up 설정과 연결됨.
- `PINx`: 실제 입력 pin의 상태를 읽음.

[led2.c](./src/led2.c)는 가장 기본적인 출력 예제임.

```c
DDRC = 0x0f;
while(1)
{
    PORTC = 0x0F;
    _delay_ms(500);

    PORTC = 0x00;
    _delay_ms(500);
}
```

`DDRC = 0x0f`는 PORTC 하위 4bit를 출력으로 설정함. `PORTC`에 값을 쓰면 LED가 켜지거나 꺼짐. 임베디드에서 `while(1)`은 프로그램을 끝내지 않고 계속 장치를 제어하기 위한 기본 구조임.

## 입력과 pull-up 사고

switch 실습에서는 `PINx`를 읽어 외부 입력 상태를 판단함. 입력 pin은 아무것도 연결되지 않으면 floating 상태가 될 수 있어서 pull-up 또는 pull-down을 고려해야 함.

스위치 회로에서는 눌렀을 때 0이 되는 active-low 구조도 흔함. 그래서 코드에서 `if (!(PIND & ...))` 같은 형태가 나오면 “눌림을 0으로 판단하는 회로”인지 확인해야 함.

## FND와 bit pattern

FND는 숫자를 보여주기 위해 여러 segment를 동시에 제어함. 숫자 하나를 표시하려면 각 segment에 대응하는 bit pattern이 필요함.

`fnd1.c`, `fnd2.c`, `switch_fnd.c`, `interrupt_fnd.c`는 숫자와 bit pattern을 연결하는 실습임. 여기서 중요한 개념은 숫자 계산이 아니라 “하나의 값이 여러 출력 pin의 조합으로 표현된다”는 점임.

## delay와 polling

`_delay_ms()`는 일정 시간 동안 CPU를 기다리게 함. LED를 깜빡이는 간단한 실습에는 편하지만, 기다리는 동안 다른 일을 처리하기 어려움. switch 상태를 계속 확인하는 polling 방식도 구조가 단순하지만 CPU가 계속 상태를 물어봐야 함.

이 한계를 넘기 위해 timer와 interrupt를 배움.

## Timer

timer는 MCU 내부 clock을 기준으로 일정 주기마다 flag를 만들거나 compare match를 발생시킴. `timer0led.c`, `timer1com.c`, `timer2ledleftright.c`는 delay 없이 시간 기반 동작을 만드는 감각을 익히기 위한 예제임.

timer 코드는 보통 다음 요소를 함께 봄.

- clock source
- prescaler
- counter 시작값
- overflow 또는 compare match
- interrupt enable 여부

timer 주기가 맞지 않으면 LED 깜빡임, PWM 주파수, sensor sampling 간격이 모두 달라짐.

## Interrupt

interrupt는 특정 사건이 생겼을 때 main loop 흐름을 잠깐 멈추고 ISR로 이동하는 방식임. `interrupt1.c`, `interrupt_fnd.c`는 외부 입력이나 timer event에 반응하는 예제임.

```c
ISR(INT0_vect)
{
    // event가 발생했을 때 실행되는 코드
}
```

ISR에서는 오래 걸리는 작업을 피하고 flag 변경처럼 짧은 처리를 하는 것이 좋음. main loop와 ISR이 같은 변수를 공유하면 compiler 최적화를 막기 위해 `volatile`이 필요할 수 있음.

## PWM

PWM은 analog 전압을 직접 출력하는 것이 아니라 HIGH/LOW의 비율을 빠르게 바꾸어 평균 출력처럼 보이게 만드는 방식임.

- duty cycle이 낮으면 평균 출력이 낮음.
- duty cycle이 높으면 평균 출력이 높음.
- LED 밝기, DC motor 속도, buzzer 음, servo 각도 제어에 연결됨.

`pwmled.c`, `pwmservo.c`, `pwmServoSwitch.c`, `pwmbuzzer.c`, `dc_pwm.c`, `dc_pwm_vr.c`는 모두 이 관점을 공유함. servo는 일반 DC motor처럼 단순 속도 제어가 아니라 pulse 폭을 각도 명령으로 해석한다는 차이가 있음.

## UART

UART는 두 장치가 정해진 속도와 frame 규칙으로 byte를 주고받는 직렬 통신임.

- baud rate
- data bit
- parity
- stop bit
- TX/RX pin 연결

`uart1.c`, `uart2.c`, `uart3.c`에서는 baud rate register, control register, data register를 설정함. 수신한 문자를 LED나 FND 출력으로 연결하면 “통신 data가 hardware 출력으로 바뀌는 흐름”을 볼 수 있음.

## ADC와 sensor

CDS는 밝기, PIR은 움직임, SHT20은 온습도, variable resistor는 analog 입력을 제공함. sensor 코드는 보통 아래 흐름임.

```text
raw value 읽기 -> 의미 있는 단위로 변환 -> threshold 판단 -> LED/FND/LCD/motor 출력
```

`cds.c`, `cds2.c`, `cds_fnd.c`, `pir.c`, `i2c_tempHumi.c`는 입력을 읽고 조건에 따라 출력 장치를 제어하는 연습임.

## I2C, EEPROM, LCD

I2C나 EEPROM, LCD는 단순 GPIO보다 통신 절차가 중요함. 장치 주소, register 주소, read/write 순서, ACK/NACK 같은 protocol 흐름을 따라야 함.

`lib/sht20`, `lib/at25`, `lib/lcd`는 반복되는 장치 제어 코드를 library로 분리한 예임. `src`의 실습 코드가 직접 모든 bit를 다루지 않고 library 함수를 호출하면, C에서 배운 header/source 분리가 embedded에서도 그대로 쓰인다는 점을 확인할 수 있음.

## actuator 제어

DC motor, servo, buzzer는 모두 출력 장치지만 제어 의미가 다름.

- DC motor: 방향과 속도
- servo: pulse 폭에 따른 각도
- buzzer: 주파수와 duty에 따른 소리

임베디드 실습에서는 “입력 sensor → 판단 → actuator 출력” 흐름이 자주 반복됨. 이 흐름을 잡으면 개별 파일 이름이 달라도 코드를 읽는 기준이 생김.
