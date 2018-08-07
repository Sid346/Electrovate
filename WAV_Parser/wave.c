#include<stdio.h>
#include<stdlib.h>

typedef struct{
	char fileformat[4];
	int file_size;
	char subformat[4];
	char subformat_id[4];
	int chunk_bits;     		// 16 or 18 or 40 due to pcm it is 16 here
	short int audio_format;    	// little or big endian
	short int num_channels;     	// 2 here for left and right
	int sample_rate;		// sample_rate denotes the sampling rate.
	int byte_rate;           	// bytes  per second
	short int bytes_per_frame;
	short int bits_per_sample; 
	char data_id[4];    		// "data" written in ascii
	int data_size;
}head;

head *d;

int main(int argc, char *argv[]){
	printf("************************** Welcome to the WAVE file parser ************************\n");
	printf("*********************************** Version 1.0 ***********************************\n");
	printf("\n               Please Provide the name of the file to be parsed    -----  \n");
	char a[100];
	printf("                                  -- ");scanf("%s",a);
	int i=0;
	FILE *ptr_file;
	ptr_file = fopen(a,"r");
	d=(head*)malloc(sizeof(head));
	if (!ptr_file)
		return 1;
	fread(d,1,sizeof(head),ptr_file);
	printf("\nThe header details are as follows  -----\n");
	printf("File Format      : %c",d->fileformat[0]);
	printf("%c",d->fileformat[1]);
	printf("%c",d->fileformat[2]);
	printf("%c",d->fileformat[3]);
	printf("\nFile Size        : %d bytes\n",d->file_size);
	printf("Sub Format       : %c",d->subformat[0]);
	printf("%c",d->subformat[1]);
	printf("%c",d->subformat[2]);
	printf("%c",d->subformat[3]);
	printf("\nSub Format ID    : %c",d->subformat_id[0]);
	printf("%c",d->subformat_id[1]);
	printf("%c",d->subformat_id[2]);
	printf("%c",d->subformat_id[3]);
	printf("\nChunk Bits       : %d\n",d->chunk_bits);
	printf("Audio Format     : %d\n",d->audio_format);
	printf("No. of Channels  : %d\n",d->num_channels);
	printf("Sample Rate      : %d Hz\n",d->sample_rate);
	printf("Byte Rate        : %d Hz\n",d->byte_rate);
	printf("Bytes Per Frame  : %d\n",d->bytes_per_frame);
	printf("Bits Per Sample  : %d\n",d->bits_per_sample);
	printf("Data ID          : %c",d->data_id[0]);
	printf("%c",d->data_id[1]);
	printf("%c",d->data_id[2]);
	printf("%c",d->data_id[3]);
	printf("\nData Size        : %d\n",d->data_size);
	fclose(ptr_file);

	return 0;
}
