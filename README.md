# M5 Screenshot Controller

Contrôlez les screenshots de votre téléphone avec le M5 Stick C Plus 2 via WiFi !

## 📋 Description

Ce projet vous permet de :
- 📱 Prendre des screenshots sur votre téléphone depuis votre M5 Stick C Plus 2
- 🌐 Utiliser une connexion WiFi (fonctionne partout : Android, iOS, etc.)
- 🖥️ Accéder via une page web simple

## 🛠️ Composants nécessaires

- M5 Stick C Plus 2
- Téléphone (Android ou iOS)
- Ordinateur avec Python 3.7+
- Connexion WiFi

## 📦 Installation

### 1. Serveur Web (sur votre ordinateur)

```bash
# Installez Python et Flask
pip install flask

# Lancez le serveur
python app.py
```

Le serveur démarre sur `http://localhost:5000`

### 2. Code M5 Stick C Plus 2

Téléchargez le fichier `m5_stick_controller.py` et chargez-le sur votre M5 Stick via :
- Thonny (simple)
- Arduino IDE
- uPyCraft

### 3. Configuration

Modifiez le fichier `m5_stick_controller.py` avec :
- Votre SSID WiFi
- Votre mot de passe WiFi
- L'adresse IP de votre ordinateur

### 4. Utilisez via le web

1. Ouvrez `http://VOTRE_IP_ORDINATEUR:5000` sur votre téléphone
2. Cliquez sur "Prendre une screenshot"
3. Appuyez sur le bouton du M5 Stick pour envoyer la commande

## 📁 Structure du projet

```
m5-screenshot-controller/
├── README.md
├── app.py (serveur Flask)
├── m5_stick_controller.py (code M5)
└── templates/
    └── index.html (page web)
```

## 🚀 Utilisation

- **M5 Stick** : Appuyez sur le bouton pour envoyer une commande
- **Page web** : Cliquez sur le bouton pour prendre une screenshot
- **Téléphone** : Ouvrez `http://VOTRE_IP:5000` pour voir la page web

## 📝 Licence

MIT

## 🆘 Support

Si vous avez des questions, ouvrez une issue sur ce repository !