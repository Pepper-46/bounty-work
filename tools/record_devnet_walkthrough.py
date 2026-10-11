#!/usr/bin/env python3
"""Record a real browser walkthrough of CobroSol's LOCAL UI (no blockchain payment).

The demonstration never sends SOL, never simulates a successful on-chain
transaction, and ends with the expected failure for a bogus signature.
"""
from pathlib import Path
import subprocess
import sys
import time
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[1]
CAPTURE = ROOT / ".capture"
DEST = ROOT / "assets" / "cobrosol-devnet-walkthrough.mp4"
CAPTURE.mkdir(parents=True, exist_ok=True)
DEST.parent.mkdir(parents=True, exist_ok=True)

server = subprocess.Popen(
    [sys.executable, "-m", "http.server", "8765", "--bind", "127.0.0.1"],
    cwd=ROOT,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
try:
    time.sleep(1.5)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir=str(CAPTURE),
            record_video_size={"width": 1280, "height": 720},
            reduced_motion="reduce",
        )
        page = context.new_page()
        video = page.video
        page.goto("http://127.0.0.1:8765/", wait_until="load")
        page.wait_for_timeout(2200)

        # A PUBLIC demonstration placeholder, not an owned payout address.
        page.locator("#recipient").fill("11111111111111111111111111111111")
        page.locator("#amount").fill("0.025")
        page.locator("#client").fill("Demo only — no real funds")
        page.locator("#description").fill("Test invoice: design service")
        page.wait_for_timeout(1800)

        page.locator("#form button[type='submit']").click()
        page.locator("#details").wait_for(state="visible")
        invoice = page.locator("#invreference").inner_text()
        assert len(invoice) >= 32, "A unique reference was not generated"
        page.wait_for_timeout(2200)

        page.locator("#confirmedDevnet").check()
        page.locator("#paybox").wait_for(state="visible")
        page.wait_for_timeout(1600)

        page.locator("#signature").fill("NOT_A_REAL_SOLANA_SIGNATURE")
        page.locator("#verify").click()
        page.wait_for_timeout(2000)
        status = page.locator("#invstatus").inner_text()
        assert status == "PENDING", "Bogus signature must never verify"
        message = page.locator("#alert").inner_text()
        assert "Invalid Solana signature" in message, message
        page.wait_for_timeout(1700)
        page.close()
        video.save_as(str(CAPTURE / "walkthrough.webm"))
        context.close()
        browser.close()
    cmd = [
        imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(CAPTURE / "walkthrough.webm"),
        "-vf", "fps=18,scale=1280:720:flags=lanczos",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "29",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-an", str(DEST)
    ]
    subprocess.run(cmd, check=True)
    assert DEST.exists() and DEST.stat().st_size > 10000
    print(f"OK: {DEST}, {DEST.stat().st_size} bytes; invalid transaction correctly rejected")
finally:
    server.terminate()
    server.wait(timeout=10)
