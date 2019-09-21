#include <stdio.h>
#include <stdint.h>
#include <C-Problem_Libs.h>


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct next_Hop
{
	char *filename;
}next_Hop;

typedef struct Mapping
{
	uint8_t ip[4];
	uint32_t mask;
	next_Hop *file;
}Mapping;

// The mapping table that redirects the packets to files
Mapping MAPPING_TABLE[6] ={
(Mapping){.ip = {0, 0, 0, 0}, .mask = 0, .file = &(next_Hop){.filename = "not_found.txt"}},
(Mapping){.ip = {192, 168, 128, 4}, .mask = 24, .file = &(next_Hop){.filename = "eth1.txt"}},
(Mapping){.ip = {192, 168, 0, 1}, .mask = 18, .file = &(next_Hop){.filename = "eth2.txt"}},
(Mapping){.ip = {10, 0, 0, 1}, .mask = 8, .file = &(next_Hop){.filename = "eth3.txt"}},
(Mapping){.ip = {10, 0, 0, 2}, .mask = 32, .file = &(next_Hop){.filename = "eth4.txt"}},
(Mapping){.ip = {127, 0, 0, 1}, .mask = 32, .file = &(next_Hop){.filename = "loopback.txt"}}};

// Boolean if bits match up to num_bits
int bits_match(uint8_t *ip1, uint8_t *ip2, int num_bits){
	// Check which group needs bitwise operations
	int section = num_bits / 8;

	// Check numbers up to the number
	for(int i = 0; i < section; i++){
		if(ip1[i] != ip2[i]){
			return 0;
		}
	}

	// Check bits
	int bits = num_bits - section * 8;
	int bitwise = 0x0;
	// Check case
	switch(bits){
		case 0:
			return 1;
			break;
		case 1:
			bitwise = 0x80;
			break;
		case 2:
			bitwise = 0xC0;
			break;
		case 3:
			bitwise = 0xE0;
			break;
		case 4:
			bitwise = 0xF0;
			break;
		case 5:
			bitwise = 0xF8;
			break;
		case 6:
			bitwise = 0xFC;
			break;
		case 7:
			bitwise = 0xFE;
			break;
	}

	// Check if bits match
	if((ip1[section] & bitwise) != (ip2[section] & bitwise)){
		return 0;
	}

	// Return true if nothing fails
	return 1;
}

// returns the index which matches the most to a given IP
int redirect_to_Mapping(uint8_t *ip){
	// This method might be useful to impliment
}

// Sends output a mapping
void decode_String(char* input,  uint8_t *output_ip, char *output_str){
	// This method might be useful to impliment
}

// Send data to file
void transfer_Data(uint8_t *ip, char *data){
	// This method might be useful to impliment
}

// Parses through packet data file
void decode_File(char *filename){
	// This method might be useful to impliment
}


int main(){
	printf("Start coding!\n");
}