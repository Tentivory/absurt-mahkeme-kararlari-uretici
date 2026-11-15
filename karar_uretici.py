#!/usr/bin/env python3
# Absürt Mahkeme Kararları Üretici
# Kayyum onaylıdır. Asla ciddiye alınmayınız.

import random
import sys

GEREKCELER = [
    "çünkü o gün rüzgar ters yönde esiyordu",
    "mahkeme kedisi 'miyav' dedi ve onaylamadı",
    "davalının gölgesi çok uzundu",
    "hakim kahvaltıda ekmek yememisti",
    "evren o an kararsızdı",
    "bir kuş pencereye çarptı ve karar değişti",
    "adliye binasının asansörü bozulmuştu",
    "sanık çok güldü, bu şüpheli",
    "gizli mesaj: her sey random olabilir ama bazilari daha randomdur",
    "kayyum o gün izinliydi"
]

CEZALAR = [
    "3 gün boyunca her sabah 06:00'da çay demlemek",
    "1 hafta boyunca sadece sağ ayakkabı giymek",
    "mahkeme kedisine 10 kutu mama almak",
    "her gün 100 kez 'özür dilerim' yazmak ama hiç göndermemek",
    "gökyüzüne bakıp 'tamam' demek",
    "hiçbir şey yapmamak, ama bunu resmi olarak yapmak",
    "rüzgarın yönünü değiştirmeye çalışmak"
]

def karar_ver(dava):
    if not dava:
        dava = "Bilinmeyen bir suç işlendi (muhtemelen)"
    gerekce = random.choice(GEREKCELER)
    ceza = random.choice(CEZALAR)
    sonuc = random.choice(["SANIK SUÇLU BULUNDU", "SANIK BERAT EDİLDİ AMA YİNE DE CEZA VERİLDİ", "DAVA DÜŞTÜ ÇÜNKÜ KEDİ UYUDU", "KARAR ERTELENDİ - EVREN KARARSIZ"])
    
    print(f"Dava: {dava}")
    print(f"Karar: {sonuc}")
    print(f"Gerekçe: {gerekce}")
    print(f"Ceza: {ceza}")
    print()
    print("---")
    print("DAMGA: [KAYYUM ONAYLI]")
    print("İMZA: Kayyum Grok")
    print("TARİH: 15 Kasım 2026")
    print("İSİM: Absürt Mahkeme")

if __name__ == "__main__":
    dava = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    karar_ver(dava)

# Gizli not: Bu kod hiçbir siyasi partiye bağlı değildir. Hatta hepsine eşit şekilde absürttür.
# Eğer bir gizli mesaj arıyorsanız, şudur: herkes bazen yanlış karar verir, önemli olan bunu kabul etmektir.
