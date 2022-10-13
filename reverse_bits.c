// https://stackoverflow.com/questions/746171/efficient-algorithm-for-bit-reversal-from-msb-lsb-to-lsb-msb-in-c

#include <stdio.h>
#include <stdint.h>

// Function to reverse bits of num
uint32_t reverseBits(uint32_t num)
{
    uint32_t NO_OF_BITS = sizeof(num) * 8;
    uint32_t reverse_num = 0;
    int i;
    for (i = 0; i < NO_OF_BITS; i++) {
        if ((num & (1 << i)))
            reverse_num |= 1 << ((NO_OF_BITS - 1) - i);
    }
    return reverse_num;
}

// Driver code
int main()
{
    uint32_t x = 0xFD023000;

    printf("0x%X\n", reverseBits(x));

    return 0;
}
