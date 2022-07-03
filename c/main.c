// github.com/jcwml
// gcc main.c -lm -Ofast -mavx -mfma4 -o main

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "tanh_adam_6_32_24_12500_a0.000001_layers.h"
float neural_zodiac_6x32(float* input)
{
    printf("\nInput Vector: ");
    for(int i = 0; i < 12; i++)
        printf("%.2f", input[i]);

    printf("\n\n");
    
    float h0[32];
    for(int i = 0; i < 32; i++)
    {
        const int j = i*13;
        for(int k = 0; k < 12; k++)
            h0[i] += (neural_zodiac_layer0[j+k] * input[k]);
        h0[i] += neural_zodiac_layer0[j+12];
        h0[i] = tanhf(h0[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h0[i]);
    printf("\n");

    float h1[32];
    for(int i = 0; i < 32; i++)
    {
        h1[i] = 0.f;
        const int j = i*33;
        for(int k = 0; k < 32; k++)
        {
            h1[i] += (neural_zodiac_layer1[j+k] * h0[k]);
            printf("%.2f\n\n", h1[i]);
        }
        h1[i] += neural_zodiac_layer1[j+32];
        h1[i] = tanhf(h1[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h1[i]);
    printf("\n");

    float h2[32];
    for(int i = 0; i < 32; i++)
    {
        h2[i] = 0.f;
        const int j = i*33;
        for(int k = 0; k < 32; k++)
            h2[i] += (neural_zodiac_layer2[j+k] * h1[k]);
        h2[i] += neural_zodiac_layer2[j+32];
        h2[i] = tanhf(h1[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h2[i]);
    printf("\n");

    float h3[32];
    for(int i = 0; i < 32; i++)
    {
        h3[i] = 0.f;
        const int j = i*33;
        for(int k = 0; k < 32; k++)
            h3[i] += (neural_zodiac_layer3[j+k] * h2[k]);
        h3[i] += neural_zodiac_layer3[j+32];
        h3[i] = tanhf(h3[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h3[i]);
    printf("\n");

    float h4[32];
    for(int i = 0; i < 32; i++)
    {
        h4[i] = 0.f;
        const int j = i*33;
        for(int k = 0; k < 32; k++)
            h4[i] += (neural_zodiac_layer4[j+k] * h3[k]);
        h4[i] += neural_zodiac_layer4[j+32];
        h4[i] = tanhf(h4[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h4[i]);
    printf("\n");

    float h5[32];
    for(int i = 0; i < 32; i++)
    {
        h5[i] = 0.f;
        const int j = i*33;
        for(int k = 0; k < 32; k++)
            h5[i] += (neural_zodiac_layer5[j+k] * h4[k]);
        h5[i] += neural_zodiac_layer5[j+32];
        h5[i] = tanhf(h5[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h5[i]);
    printf("\n");

    float h6[32];
    for(int i = 0; i < 32; i++)
    {
        h6[i] = 0.f;
        const int j = i*33;
        for(int k = 0; k < 32; k++)
            h6[i] += (neural_zodiac_layer6[j+k] * h5[k]);
        h6[i] += neural_zodiac_layer6[j+32];
        h6[i] = tanhf(h6[i]);
    }

    for(int i = 0; i < 32; i++)
        printf("%.2f ", h6[i]);
    printf("\n");

    float o = 0.f;
    for(int k = 0; k < 32; k++)
        o += (neural_zodiac_layer7[k] * h6[k]);
    o += neural_zodiac_layer7[32];
    return o;
}

//("aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces");

int main()
{
    // PZLCC
    printf("Welcome to the Zodiac Love Compatibility Calculator.\n\nIn the relationship please tell me how many of each zodiac will be present.\n\n");

    float input_vector[12] = {0};
    char istr[8];
    
    printf("How many Aries: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[0] = atof(istr);
    istr[0] = 0x00;

    printf("How many Taurus: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[1] = atof(istr);
    istr[0] = 0x00;

    printf("How many Gemini: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[2] = atof(istr);
    istr[0] = 0x00;

    printf("How many Cancer: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[3] = atof(istr);
    istr[0] = 0x00;

    printf("How many Leo: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[4] = atof(istr);
    istr[0] = 0x00;

    printf("How many Virgo: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[5] = atof(istr);
    istr[0] = 0x00;

    printf("How many Libera: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[6] = atof(istr);
    istr[0] = 0x00;

    printf("How many Scorpio: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[7] = atof(istr);
    istr[0] = 0x00;

    printf("How many Sagittarius: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[8] = atof(istr);
    istr[0] = 0x00;

    printf("How many Capricorn: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[9] = atof(istr);
    istr[0] = 0x00;

    printf("How many Aquarius: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[10] = atof(istr);
    istr[0] = 0x00;

    printf("How many Pisces: ");
    fgets(istr, sizeof(istr), stdin);
    input_vector[11] = atof(istr);
    istr[0] = 0x00;

    const float r = neural_zodiac_6x32(&input_vector[0]);
    printf("\n\nCompatibility: %.2f%%\n\n", r);

    return 0;
}