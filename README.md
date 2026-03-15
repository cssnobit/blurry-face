# CCTV Video Anonymizer

## 🇧🇷 Descrição

Ferramenta em Python para anonimizar automaticamente pessoas em vídeos de câmeras de segurança.

O sistema analisa o vídeo quadro a quadro, detecta pessoas e aplica um desfoque na região da cabeça para evitar a identificação dos indivíduos.

Foi desenvolvido para facilitar o tratamento de gravações de vigilância (CFTV) de forma automática.

---

## 🇺🇸 Description

A Python tool that automatically anonymizes people in security camera footage.

The system processes the video frame by frame, detects people, and applies blur to the head region to prevent identification.

Designed to simplify the processing of surveillance (CCTV) recordings.

---

## Requisitos / Requirements

* Python 3.9+
* FFmpeg instalado
* Dependências do `requirements.txt`

---

## Instalação / Installation

Clone o repositório (ou baixe o arquivo ZIP):

```bash
git clone https://github.com/cssnobit/blurry-face.git
```


Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Uso / Usage

```bash
python main.py <input_video.mp4> <output_video.mp4>
```

Exemplo / Example:

```bash
python main.py video.mp4 anonymized.mp4
```

---

## O que ele faz / What it does

* Detecta pessoas no vídeo / 🇺🇸 Detect peoples on video
* Identifica a região da cabeça / 🇺🇸 Identify the head area
* Aplica blur automaticamente / 🇺🇸 Apply the blur automatically
* Gera um novo vídeo anonimizado / 🇺🇸 Output a new anonymized video
