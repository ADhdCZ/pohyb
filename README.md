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

Je-li instalace v pořádku, ověřte ji v příkazovém řádku (cmd.exe) pomocí příkazu:

>python --version

Výstup v příkazovém řádku by měl vypadat takto (verze může být odlišná):

![Python verze](/assets/Python_verze.png "Python verze")

### 2. pyautogui

**pyautogui** se stáhne a nainstaluje příkazem:

>pip install pyautogui

Úspěšná instalace vypadá následovně:

![Instalace pyautogui](/assets/Python_pyautogui.png "Instalace pyautogui")

### 3. program

Program lze stáhnout jako .zip nebo pomocí gitu. Umístěte jej do libovolné složky na disku a podle umístění zadejte vaši cestu k programu do konfiguračního souboru config.ini.

Chcete-li ve Windows vybrat cestu ke složce, postupujte následovně:

>Otevřete složku: V Průzkumníku souborů otevřete složku, jejíž cestu chcete získat.
>
>Klikněte do adresního řádku: Klikněte do adresního řádku v horní části okna, kde se zobrazuje cesta ke složce. Celá cesta se automaticky označí.
>
>![adresa](/assets/adresa.png "adresa")
>
>Zkopírujte cestu: Stiskněte Ctrl+C nebo pravým tlačítkem myši vyberte možnost „Kopírovat“.
>
>Vložte cestu: Nyní můžete cestu vložit tam, kde je potřeba, například do konfiguračního souboru, pomocí Ctrl+V.

Po úspěšném stažení, instalaci a konfiguraci cesty lze spustit program pomocí START.bat.

## Přehled programu

- **START.bat**

>Spustí skript.
>
>Slouží pro spouštění skriptu bez nutnosti spouštění příkazového řádku a volání příslušného příkazu spuštění skriptu. Zkratkou Ctrl+C se skript vypne.

- **config.ini**

>Slouží pro konfiguraci cesty ke složce na počítači a název skriptu, který má být spuštěn.
>
>**!! Po stažení je nutné nastavit správnou cestu ve vašem počítači !!**

- **main.py**

>Obsahuje kód skriptu, který se spouští. Zkratkou Ctrl+C se skript vypne.