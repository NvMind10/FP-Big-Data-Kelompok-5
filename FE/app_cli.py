# app_cli.py
import time
from datetime import datetime
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Definisikan warna tema sesuai request: Royal Blue & Peach (diwakili warna SandyBrown/Orange di terminal)
THEME_BLUE = "bold royal_blue1"
THEME_PEACH = "bold sandy_brown"

def tampilkan_log_scamshield(waktu, pengirim, grup, teks, status):
    """
    Fungsi Utama UI Terminal. 
    Fungsi ini yang nantinya akan ditempel di bagian akhir file spark_pipeline teman Anda.
    """
    # Menentukan dekorasi berdasarkan status deteksi AI
    if status == "🚨 SCAM":
        # PERBAIKAN: Menggunakan tag huruf kecil [blink]...[/blink]
        status_print = f"[bold red]{status} [blink](BAHAYA)[/blink][/bold red]"
        border_color = "red"
        action_text = f"[{THEME_PEACH}]Tindakan:[/{THEME_PEACH}] [bold red]Auto-Append ke dataset_2026.csv (Continuous Learning)[/bold red]"
    else:
        status_print = f"[bold green]{status} (AMAN)[/bold green]"
        border_color = "green"
        action_text = f"[{THEME_PEACH}]Tindakan:[/{THEME_PEACH}] [dim green]Abaikan / Teruskan pesan[/dim green]"

    # Membuat layout tabel mini yang rapi di terminal
    table = Table(title=f"🛡️ [bold white]ScamShield V2 - Live Stream Ingestion[/bold white]", title_style="on blue", box=None)
    table.add_column("Komponen Data", style=THEME_BLUE, width=18)
    table.add_column("Nilai / Isi Teks", style="white")

    table.add_row("🕒 Waktu Sistem", waktu)
    table.add_row("👤 Akun Pengirim", pengirim)
    table.add_row("💬 Grup Telegram", grup)
    table.add_row("📝 Isi Teks / OCR", f"[italic]\"{teks}\"[/italic]")
    table.add_row("🤖 Hasil Analisis AI", status_print)

    # Cetak ke layar terminal menggunakan Panel agar terlihat seperti software profesional
    console.print(Panel(table, border_style=border_color, expand=False))
    console.print(action_text)
    console.print("-" * 60)

if __name__ == "__main__":
    console.print(Panel(f"[{THEME_BLUE}]ScamShield V2 - Terminal UI Module Started[/{THEME_BLUE}]\n[💡] Menjalankan mode simulasi mandiri...", border_style="blue"))
    
    # Kumpulan data simulasi (Mock Data) untuk uji coba mandiri Anda
    mock_senders = ["@loker_cepat_cuan", "@crypto_indonesia_bot", "@budi_santoso", "@siska_hrd_palsu", "@riki_wibowo"]
    mock_groups = ["Grup Lowongan Kerja JKT", "Komunitas Pencari Cuan", "Obrolan Santai Alumni", "Info Investasi 2026"]
    mock_texts = [
        "Tugas mudah cuma like dan subscribe youtube dapat 50rb per menit. Hubungi WA ini.",
        "Halo bro, besok jadinya kumpul jam berapa ya?",
        "Investasi modal 100k balik 10jt dalam 2 jam tanpa risiko! Slot terbatas gan.",
        "Selamat pagi, apakah berkas lamaran saya sudah diterima perusahaan?",
        "Butuh admin ketik rumahan, jaminan gaji 5jt per minggu tapi bayar biaya pendaftaran 50rb."
    ]
    mock_statuses = ["🚨 SCAM", "✅ AMAN", "🚨 SCAM", "✅ AMAN", "🚨 SCAM"]

    # Jalankan simulasi loop otomatis di terminal Anda
    try:
        for i in range(len(mock_texts)):
            waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tampilkan_log_scamshield(
                waktu=waktu_sekarang,
                pengirim=mock_senders[i],
                grup=mock_groups[i],
                teks=mock_texts[i],
                status=mock_statuses[i]
            )
            time.sleep(3) # Jeda waktu seolah-olah data streaming masuk secara real-time
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Simulasi terminal dihentikan.[/bold yellow]")