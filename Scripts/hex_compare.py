from typing import List

PLAYER = [
    "B0 69 41 2A 00 00 00 00 FF FF FF FF 00 00 04 00 D0 D5 93 20 00 00 00 00 70 04 DA 20 00 00 00 00 B0 EE BB 20 00 00 00 00 40 95 A1 20 00 00 00 00 B0 B0 CF 20 00 00 00 00 00 00 00 00 00 00 00 00 70 5D FA C3 FC BC 8C 40 7E 5C F5 C3 00 00 00 00 81 3C D2 3E 00 00 00 00 38 6C 69 BF 00 00 00 00 A8 86 ED 3E D7 12 7C 3E 6F DA 59 BF 00 00 00 00 39 81 FA C3 B8 8F 5F 40 64 4F F5 C3 00 00 00 00 38 1C FA C3 7B 00 9E 40 B7 2A F6 C3 00 00 00 00 C0 11 EF 1E 00 00 00 00 70 76 DA 20 00 00 00 00 E0 B5 F3 1E 00 00 00 00 00 00 00 00 00 00 00 00 30 B2 0E 2A 00 00 00 00 FF FF FF FF 00 00 0F 00 40 46 A5 49 01 00 00 00 01 00 00 00 02 00 00 00 C0 37 BB 20 00 00 00 00 30 38 BB 20 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 12 00 07 00 00 00 55 00 70 00 5F 00 63 00 68 00 69 00 6E 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 15 00 09 00 00 00 44 00 6F 00 77 00 6E 00 5F 00 63 00 68 00 69 00 6E 00 00 00 00 00 00 00 00 00 00 00 C8 5B 0E 2A 00 00 00 00 FF FF FF FF 00 00 18 00 30 11 EF 1E 00 00 00 00 00 00 00 00 00 00 00 00",
    "B0 69 41 2A 00 00 00 00 FF FF FF FF 00 00 29 00 D0 D5 93 20 00 00 00 00 70 03 DA 20 00 00 00 00 B0 EE BB 20 00 00 00 00 40 95 A1 20 00 00 00 00 B0 B0 CF 20 00 00 00 00 00 00 00 00 00 00 00 00 F0 5A FA C3 52 D7 8C 40 4B 67 F5 C3 00 00 00 00 81 3C D2 3E 00 00 00 00 38 6C 69 BF 00 00 00 00 2B 11 E9 3E DD 5E 56 3E 6E 8C 5D BF 00 00 00 00 14 82 FA C3 53 92 60 40 C8 59 F5 C3 00 00 00 00 26 11 FA C3 3C C3 9D 40 96 3F F6 C3 00 00 00 00 20 8A D5 20 00 00 00 00 10 72 DA 20 00 00 00 00 B0 86 D5 20 00 00 00 00 00 00 00 00 00 00 00 00 30 B2 0E 2A 00 00 00 00 FF FF FF FF 00 00 34 00 40 46 A5 49 01 00 00 00 01 00 00 00 02 00 00 00 50 37 BB 20 00 00 00 00 50 37 BB 20 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 37 00 04 00 00 00 48 00 65 00 61 00 64 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF FF FF FF 00 00 39 00 04 00 00 00 48 00 65 00 61 00 64 00 00 00 00 00 C8 5B 0E 2A 00 00 00 00 FF FF FF FF 00 00 3B 00 B0 89 D5 20 00 00 00 00 00 00 00 00 00 00 00 00",
    "B0 69 41 2A 00 00 00 00 FF FF FF FF 00 00 37 00 D0 D6 93 20 00 00 00 00 60 FE BB 20 00 00 00 00 90 F0 BB 20 00 00 00 00 40 95 A1 20 00 00 00 00 B0 B0 CF 20 00 00 00 00 00 00 00 00 00 00 00 00 4A BF FA C3 54 65 B3 3F E8 2B F6 C3 00 00 00 00 81 3C D2 3E 00 00 00 00 38 6C 69 BF 00 00 00 00 C5 6F 4A 3F F9 EF 14 3F 64 DB 42 BE 00 00 00 00 E3 0C FB C3 CE 40 59 3F 48 67 F6 C3 00 00 00 00 51 F8 F9 C3 5C B7 06 40 1C B4 F6 C3 00 00 00 00 B0 F1 B1 20 00 00 00 00 90 80 DA 20 00 00 00 00 20 EE B1 20 00 00 00 00 00 00 00 00 00 00 00 00 30 B2 0E 2A 00 00 00 00 FF FF FF FF 00 00 42 00 40 46 A5 49 01 00 00 00 01 00 00 00 02 00 00 00 00 36 BB 20 00 00 00 00 00 00 00 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 45 00 0E 00 00 00 42 00 6F 00 64 00 79 00 5F 00 72 00 6F 00 74 00 61 00 74 00 69 00 6F 00 6E 00 5A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 49 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C8 5B 0E 2A 00 00 00 00 FF FF FF FF 00 00 4B 00 20 F1 B1 20 00 00 00 00 00 00 00 00 00 00 00 00",
    "B0 69 41 2A 00 00 00 00 FF FF FF FF 00 00 31 00 F0 E2 A4 20 00 00 00 00 60 FE BB 20 00 00 00 00 90 F0 BB 20 00 00 00 00 F0 DF 60 21 00 00 00 00 B0 B0 CF 20 00 00 00 00 00 00 00 00 00 00 00 00 0C EC F9 C3 5B 1B DC 3F F0 B7 F5 C3 00 00 00 00 D5 57 8A 3E 00 00 00 00 50 7A 76 BF 00 00 00 00 76 48 30 3E 08 D3 60 BE A8 D5 75 BF 00 00 00 00 D1 D5 F9 C3 12 44 D1 3F C0 68 F5 C3 00 00 00 00 67 F8 F9 C3 DA A7 07 40 E0 B3 F6 C3 00 00 00 00 D0 30 E2 1E 00 00 00 00 90 80 DA 20 00 00 00 00 20 2D E2 1E 00 00 00 00 00 00 00 00 00 00 00 00 30 B2 0E 2A 00 00 00 00 FF FF FF FF 00 00 3C 00 40 46 A5 49 01 00 00 00 01 00 00 00 02 00 00 00 00 36 BB 20 00 00 00 00 00 00 00 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 3F 00 0E 00 00 00 42 00 6F 00 64 00 79 00 5F 00 72 00 6F 00 74 00 61 00 74 00 69 00 6F 00 6E 00 5A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 43 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C8 5B 0E 2A 00 00 00 00 FF FF FF FF 00 00 45 00 40 30 E2 1E 00 00 00 00 00 00 00 00 00 00 00 00"

    "B0 69 41 2A 00 00 00 00 FF FF FF FF 00 00 58 00 D0 EE 96 25 00 00 00 00 70 07 DA 20 00 00 00 00 80 F1 BB 20 00 00 00 00 B0 25 97 1F 00 00 00 00 B0 B0 CF 20 00 00 00 00 00 00 00 00 00 00 00 00 7B 5F FB C3 13 E8 55 40 03 D6 F7 C3 00 00 00 00 05 4A 95 3E 00 00 00 00 3A E0 74 BF 00 00 00 00 FF 7A E0 3E 2B A9 D4 BD C8 8A 64 BF 00 00 00 00 CE 0D FC C3 3A E3 58 40 99 EA F7 C3 00 00 00 00 27 D4 FA C3 20 A0 6F 40 39 BB F7 C3 00 00 00 00 90 D6 9A 1F 00 00 00 00 F0 89 DA 20 00 00 00 00 00 D4 9A 1F 00 00 00 00 00 00 00 00 00 00 00 00 30 B2 0E 2A 00 00 00 00 FF FF FF FF 00 00 63 00 40 46 A5 49 01 00 00 00 01 00 00 00 02 00 00 00 B0 3B BB 20 00 00 00 00 B0 3B BB 20 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 66 00 05 00 00 00 52 00 5F 00 61 00 72 00 6D 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 B8 5D 47 2B 00 00 00 00 FF FF FF FF 00 00 68 00 05 00 00 00 52 00 5F 00 61 00 72 00 6D 00 00 00 C8 5B 0E 2A 00 00 00 00 FF FF FF FF 00 00 6A 00 20 D6 9A 1F 00 00 00 00 00 00 00 00 00 00 00 00"
]

PALAMUTE = [
    
]

PALICO = [
    "C8 DE 2D 2A 00 00 00 00 FF FF FF FF 00 00 49 00 06 00 00 00 5C 8F D6 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 41 00 00 80 40 00 00 00 00 00 00 00 00 01 00 00 00 00 00 80 3F 00 00 00 3F 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F A0 32 9C 29 00 00 00 00 FF FF FF FF 00 00 53 00 06 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 0A 00 00 00 5C 8F D6 41 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 00 00 00 41 00 00 80 40 00 00 00 00 9A 99 19 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 00 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 6B 00 00 00 FF FF FF FF 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CA 5B 4A E2 BD 71 A6 E8 43 91 5E 5C 0C F8 6E 4A F4 A5 89 34 CF 49 BC 87 6D DB 9D AE 1D D0 84 E9 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 48 1B 99 CE D4 53 31 44 C1 50 AD 48 23 DA F9 A5 72 65 D8 20 E6 2B 47 E3 EB 9A EC 9A 34 B2 0F 45",
    "C8 DE 2D 2A 00 00 00 00 FF FF FF FF 00 00 20 00 06 00 00 00 5C 8F D6 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 41 00 00 80 40 00 00 00 00 00 00 00 00 01 00 00 00 00 00 80 3F 00 00 00 3F 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F A0 32 9C 29 00 00 00 00 FF FF FF FF 00 00 2A 00 06 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 0A 00 00 00 5C 8F D6 41 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 00 00 00 41 00 00 80 40 00 00 00 00 9A 99 19 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 00 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
    "C8 DE 2D 2A 00 00 00 00 FF FF FF FF 00 00 20 00 05 00 00 00 66 66 4E 41 00 00 00 00 00 00 00 00 07 00 00 00 CD CC 54 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0 40 00 00 40 40 00 00 00 00 00 00 00 00 01 00 00 00 00 00 80 3F 00 00 80 3F 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F A0 32 9C 29 00 00 00 00 FF FF FF FF 00 00 2A 00 05 00 00 00 01 00 00 00 02 00 00 00 02 00 00 00 01 00 00 00 0A 00 00 00 66 66 4E 41 00 00 00 00 00 00 00 00 CD CC 54 41 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 00 00 C0 40 00 00 40 40 00 00 00 00 CD CC CC 3E 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
    "C8 DE 2D 2A 00 00 00 00 FF FF FF FF 00 00 54 00 06 00 00 00 5C 8F D6 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 41 00 00 80 40 00 00 00 00 00 00 00 00 01 00 00 00 00 00 80 3F 00 00 00 3F 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F A0 32 9C 29 00 00 00 00 FF FF FF FF 00 00 5E 00 06 00 00 00 01 00 00 00 02 00 00 00 02 00 00 00 01 00 00 00 0A 00 00 00 5C 8F D6 41 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 00 00 00 41 00 00 80 40 00 00 00 00 CD CC CC 3E 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 00 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0B 00 00 00 FF FF FF FF 51 84 F5 C3 00 00 00 00 00 00 00 00 00 00 80 BF 00 00 00 00 00 00 80 3F 00 00 C8 42 12 00 00 00 00 00 00 00 00 00 00 00 04 00 00 00 FF FF FF FF 00 00 80 00 00 00 00 30 A8 E1 F6 46 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF 50 0D CA 1E 00 00 00 00 04 00 00 00 FF FF FF FF 00 00 80 00 00 00 00 30 A8 E1 F6 46 01 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2C 00 00 00 00 00 00 00 00 00 80 20 00 00 00 28 08 9E 0A 47 01 00 00 00 01 00 00 00 3F 75 07 00 B0 F4 C0 BD 00 00 00 00 00 00 00 00 00 00 00 00 48 0E CA 1E 00 00 00 00 60 0E CA 1E 00 00 00 00 48 0E CA 1E 00 00 00 00 48 0E CA 1E 00 00 00 00 20 00 00 14 CF 8A 56 00 48 0E CA 1E 00 00 00 00 40 10 CA 1E 00 00 00 00 A0 10 CA 1E 00 00 00 00 D0 10 CA 1E 00 00 00 00 70 10 CA 1E 00 00 00 00 28 11 CA 1E 00 00 00 00 18 00 00 00 00 00 00 00 EF 54 4C 5B 60 BA 2F C0",

]

PLAYER_STRUCT = "A0 4E FB 2A 00 00 00 00 FF FF FF FF 00 00 ?? 00 01 00 00 00 00 00 ?? 42 00 00 ?? ?? 00 00 00 00 00 00 ?? 42 00 00 ?? ?? 00 00 ?? ?? 00 00 ?? 42 00 00 ?? ?? 00 00 ?? 41 00 00 ?? 41 00 00 ?? ?? 06 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 00 00 00 0E 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ?? ?? ?? ?? 00 00 00 00 04 00 00 00 03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 22 00 00 00 00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00 00 00 00 00"

def compare(left: str, right: str) -> str:
    left_bytes = left.split(" ")
    right_bytes = right.split(" ")
    output_str = []

    for i, lbyte in enumerate(left_bytes):
        rbyte = right_bytes[i]

        output_str.append("??" if rbyte != lbyte else lbyte)

    return " ".join(output_str)

def remove_equal_question_marks(left: str, right: str) -> str:
    left_bytes = left.split(" ")
    right_bytes = right.split(" ")
    output_str = []

    for i, lbyte in enumerate(left_bytes):
        rbyte = right_bytes[i]

        output_str.append("??" if rbyte != lbyte else "00")

    return " ".join(output_str)

def get_mask_indexes(signature: str) -> List[int]:
    return [i for i, data in enumerate(signature.split(" ")) if data == "??"]

def build_signature(arr: List[str]) -> str:
    compared = compare(arr[0], arr[1])
    for data in arr:
        compared = compare(compared, data)

    return compared

PLAYER_SIG = build_signature(PLAYER) 
PALAMUTE_SIG = build_signature(PALAMUTE)
COMMON_SIG = remove_equal_question_marks(PLAYER_SIG, PALAMUTE_SIG)
masks = get_mask_indexes(COMMON_SIG)

player_signaute = PLAYER_SIG.split(" ")
palamute_signature = PALAMUTE_SIG.split(" ")

print(PLAYER_SIG)

for i in masks:
    print(f"Value for idx: {i} -> Player: {player_signaute[i]} Palamute: {palamute_signature[i]}")