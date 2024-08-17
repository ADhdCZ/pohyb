# POSUN je nutný

Po spuštění pohybuje kurzorem myši a periodicky stlačuje klávesu (shift), což zamezí úspání systému a vypnutí obrazovky.

## Stručný seznam požadavků

- **Python**
- **pyautogui**
- **Admin práva**
- **Povolit síťové připojení**

## Popis požadavků

Pro spuštění programu je nutné nainstalovat **Python** a doplněk **pyautogui**.

 **Python** poskytuje programovací jazykovou sadu pro spouštění a interpretaci Python skriptů s koncovkou .py.
 
 **pyautogui** dovoluje Pythonu využívat gui (graphical user interface) počítače.

Pokud se jedná o firemní počítač je nutné získat **Admin práva**, aby bylo možné spustit instalační soubor pro Python.

Při spouštění stažení a instalace **pyautogui** v cmd.exe, je nutné mít **neblokovaný síťový přístup**. 

Pokud firemní síť omezuje přístup, využijte mobilní hotspot nebo domácí připojení.

## Návod INSTALACE

Pokud máte k dispozici **Admin práva** a **neblokované síťové připojení**, postupujte následovně:

### 1. Python

Stažení [Python](https://www.python.org/downloads/) - instalaci lze ponechat ve výchozím nastavení.

Pokud je vše správně nainstalováno, lze ověřit pomocí cmd.exe příkazem:

>python --version

Výstup z příkazového řádku by měl vypadat následovně (nezáleží na konkrétní verzi):

![Python verze](/assets/Python_verze.png "Python verze")

### 2. pyautogui

**pyautogui** se stáhne a nainstaluje příkazem:

>pip install pyautogui

Úspěšná instalace vypadá následovně:

![Instalace pyautogui](/assets/Python_pyautogui.png "Instalace pyautogui")

### 3. program

Program lze stáhnout jako .zip nebo pomocí gitu. Umístěte jej do libovolné složky na disku a podle umístění zadejte vaši cestu k programu do konfiguračního souboru config.ini.

Po úspěšném stažení a instalaci lze spustit program pomocí START.bat.

## Přehled programu

- **START.bat**

>Slouží pro spouštění skriptu bez nutnosti spouštění příkazového řádku a volání příslušného příkazu spuštění skriptu. Zkratkou Ctrl+C se skript vypne.

- **config.ini**

>Slouží pro konfiguraci cesty ke složce na počítači a název skriptu, který má být spuštěn.
>
>**!! Po stažení je nutné nastavit správnou cestu ve vašem počítači !!**

- **main.py**

>Obsahuje kód skriptu, který se spouští. Zkratkou Ctrl+C se skript vypne.