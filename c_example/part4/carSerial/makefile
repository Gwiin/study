carSerial : main.o serial.o
	cc -o carSerial main.o serial.o

main.o : main.c serial.h # main.c는 serial.h를 포함하고 있기 때문에 serial.h도 의존성에 추가해야 한다. 
	cc -c main.c

serial.o : serial.c serial.h
	cc -c serial.c

clean :
	rm main.o serial.o carSerial

	
