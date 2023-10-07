# CPE 027 Case Study

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tSPlloQB6cQvKJ38SaGhbbZLVMDXS-vK?usp=sharing)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1zIUO4v4JFA_SkUQraDzyLJtrM_FfM9fV?usp=sharing)

Development of Audio Voice Modulator using Python. The following script was created by the group 8 of CPE41S2 for the course CPE 027 - Digital Signal Processing and Application. The group is composed by the following members:
- Christian Ainsley Del Rosario
- Zherish Galvin Mayordo
- Azzelle Leira Rodil

## Python Libraries Used
The team uses PedalBoard for manipulating audio files by changing pitch and passing it in High Pass or Low Pass filter to accomplish the expected outcomes.

Link to PedalBoard: https://github.com/spotify/pedalboard

## Examples
For male to female conversion
```
python male_to_female.py [raw-audio-directory] --pitch -hfilter
```

For female to male conversion
```
python female_to_male.py [raw-audio-directory] --pitch -lfilter
```
