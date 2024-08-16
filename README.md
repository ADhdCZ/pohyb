# posun je nutný
Po spuštění pohybuje kurzorem myši a periodicky stlačuje klávesu (shift), což zamezí úspání systému a vypnutí obrazovky.

## Požadavky
Pro spuštění programu je nutné nainstalovat **Python** a doplněk **pyautogui**

 **Python** poskytuje programovací jazykovou sadu pro spouštění a interpretaci Python skriptů s koncovkou .py.
 **pyautogui** dovoluje Pythonu využívat gui (graphical user interface) počítače.

Pokud se jedná o firemní počítač je nutné získat **Admin práva**, aby bylo možné spustit instalační soubor.

Pokud spouští stažení a instalace **pyautogui** v cmd.exe, je nutné mít neblokovaný síťový přístup. Je vhodné využít vlastního mobilního hotspotu nebo domácího připojení pro obejití těchto síťových omezení ve firemní síti.

### Stručný seznam požadavků
- **Python**
- **pyautogui**
- **Admin práva**
- **Povolit síťové připojení**

## Návod INSTALACE
Pokud jsou k dispozici **Admin práva** a **neblokované síťové připojení**, postupujte následovně:

#### Python

Stažení [Python](https://www.python.org/downloads/) - instalaci lze ponechat ve výchozím nastavení.

Pokud je vše správně nainstalováno, lze ověřit spuštěním cmd.exe a příkazem:

>python --version

#### pyautogui

**pyautogui** se stáhne a nainstaluje příkazem:

>pip install pyautogui

Poté lze spustit program pomocí START.bat

## Přehled programu

- **START.bat**
Slouží pro spouštění skriptu bez nutnosti spouětění příkazového řádku a volání příslušného příkazu spuštění skriptu.

- **config.ini**
Slouží pro konfiguraci cesty ke složce na počítači a název skriptu, který má být spuštěn.
**!! Po stažení je nutné nastavit správnou cestu ve vašem počítači !!**

- **main.py**
Obsahuje kód skriptu, který se spouští.