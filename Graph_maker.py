import pandas as pd
import matplotlib.pyplot as plt
import os

# Definujeme cestu k priečinku, cez ktorý budeme iterovať
output_dir = 'C:/Users/luzak/Desktop/BC/Output/'

# Iterujeme cez všetky súbory v danom priečinku
for file in os.listdir(output_dir):
    if os.path.isfile(os.path.join(output_dir, file)):
        df = pd.read_csv(os.path.join(output_dir, file))
        title = file[:-11]

        df['Start Time (min) Rounded'] = (df['Start Time (sec)'] / 600).round()*10  # Vytvoríme nový stĺpec kde zaokrúhlime sekundy na 10 minútové intervaly

        # Vykonáme agregáciu na základe vytvoreného stĺpca a spriemerujeme hodnoty
        minutes_agg = df.groupby('Start Time (min) Rounded').agg({'Sadness': 'mean', 'Joy': 'mean', 'Fear': 'mean', 'Disgust': 'mean', 'Anger': 'mean'})
        plt.figure(figsize=(10, 6))
        # Zadefinujeme cestu k súboru do ktorého sa uložia výsledné grafy
        output = 'C:/Users/luzak/Desktop/BC/Graphs/' + title
        os.makedirs(output, exist_ok=True)

        # Vykreslíme a uložíme grafy pre jednotlivé emócie
        for emotion in minutes_agg.columns:
            plt.figure(figsize=(10, 6))
            plt.plot(minutes_agg.index, minutes_agg[emotion], label=emotion, alpha=0.7)
            plt.title(title + ' - ' + emotion + ' Graph')
            plt.xlabel('Time (min)')
            plt.ylabel('Mean Emotion Score')
            plt.xticks(minutes_agg.index, rotation=45)
            plt.grid(True)
            output_path = os.path.join(output, f'{emotion}_plot.png')
            plt.savefig(output_path)
            plt.close()

        # Vykreslíme a uložíme všetky emócie v jednom grafe
        plt.figure(figsize=(10, 6))
        for emotion in minutes_agg.columns:
            plt.plot(minutes_agg.index, minutes_agg[emotion], label=emotion, alpha=0.7)
        plt.title(title + ' All Emotions')
        plt.xlabel('Time (min)')
        plt.ylabel('Mean Emotion Score')
        plt.xticks(minutes_agg.index, rotation=45)
        plt.legend()
        plt.grid(True)
        output_path = os.path.join(output, 'all_emotions_plot.png')
        plt.savefig(output_path)
        plt.close()