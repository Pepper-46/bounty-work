#!/usr/bin/env python3
"""Build an honest, AI-narrated pitch and PNG logo for CobroSol.
This does not simulate a successful blockchain payment or impersonate a person.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess
import wave

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)
TMP = OUT / ".pitch-build"
TMP.mkdir(exist_ok=True)

WIDTH, HEIGHT = 1280, 720
BG = "#071912"
MINT = "#A7F9C0"
WHITE = "#F4FFF8"
PALE = "#B0CBBB"
DARK = "#173C2B"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def face(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)

SCENES = [
    ("01 / THE PROBLEM", "A screenshot is not a receipt.",
     "Clients can share a screenshot or a transaction hash. But neither automatically proves that the right invoice was paid.",
     "A screenshot is not proof of payment."),
    ("02 / THE SOLUTION", "Get paid. Get proof.",
     "CobroSol creates S O L payment requests with a unique reference and invoice memo, then checks matching transaction data.",
     "Build payment requests with unique references."),
    ("03 / HOW IT WORKS", "Invoice. Pay. Verify.",
     "First, create a request. Next, send the Solana Pay link. Then, check the finalized transaction, recipient, amount, reference, and memo.",
     "Checks recipient, amount, reference and memo."),
    ("04 / THE PRODUCT", "Live browser prototype.",
     "The application runs publicly on GitHub Pages, stores invoices locally, and uses Solana devnet J S O N R P C. It never holds private keys.",
     "Deployed web demo. Native SOL. No custody."),
    ("05 / THE BUILDER", "Built by Pepper-46.",
     "CobroSol is a hackathon prototype from Pepper forty six, based in Bahia Blanca, Argentina. It was developed with substantial artificial intelligence assistance. No customers or revenue are claimed.",
     "Bahía Blanca, Argentina. AI-assisted development."),
    ("06 / NEXT STEPS", "Make trust portable.",
     "Next, we plan to test live wallet compatibility, add safe U S D C support, export merchant receipts, and interview real users. We start with a transparent devnet experiment.",
     "Experimental devnet prototype. No production claims."),
]
def wrapped(draw, text, font, maxw):
    words=text.split()
    lines=[]; now=''
    for w in words:
        test=(now+" "+w).strip()
        if now and draw.textlength(test,font=font)>maxw:
            lines.append(now);now=w
        else:now=test
    if now:lines.append(now)
    return lines
def image(scene,i):
    im=Image.new("RGB",(WIDTH,HEIGHT),BG)
    d=ImageDraw.Draw(im)
    for n in range(130):
        d.line((950+n*2,0,950+n*2,650),fill=(7+int(n*.14),25+int(n*.24),18+int(n*.14)),width=2)
    for k in range(6):
        d.arc((870+k*27,40+k*12,1150+k*19,400+k*20),0,275,fill="#28583E",width=2)
    d.line((65,100,1215,100),fill="#31523F",width=2)
    d.line((65,652,1215,652),fill="#31523F",width=2)
    d.text((66,43),"cobrosol.",font=face(32,True),fill=MINT)
    d.text((988,55),"SOLANA / DEVNET",font=face(15,True),fill=PALE)
    d.text((66,675),"CRYPTO WORLD'S FAIR 2026",font=face(13,True),fill=PALE)
    d.text((952,675),"AI-ASSISTED MVP",font=face(13),fill=PALE)
    eye,title,_,sub=scene
    d.text((70,146),eye,font=face(20,True),fill=MINT)
    f=face(67,True)
    title_lines=wrapped(d,title,f,1130)
    for j,line in enumerate(title_lines):d.text((70,212+j*84),line,font=f,fill=WHITE)
    f=face(31)
    for j,line in enumerate(wrapped(d,sub,f,1050)):d.text((74,385+j*48),line,font=f,fill=PALE)
    pills=["REQUEST","REFERENCE","FINALIZED"] if i in [1,2] else (["BUILT IN ARGENTINA","NO KEYS","AI ASSISTED"] if i==4 else ["OPEN SOURCE","ON SOLANA DEVNET","NO REAL FUNDS"])
    for j,label in enumerate(pills):
        x=75+j*371
        d.rounded_rectangle((x,530,x+330,599),radius=16,fill=DARK,outline="#317552",width=2)
        d.text((x+20,551),label,font=face(17,True),fill=MINT)
    path=TMP/f"slide_{i}.png";im.save(path);return path
clips=[]
for i,scene in enumerate(SCENES):
    pic=image(scene,i)
    wav=TMP/f"speech_{i}.wav"
    subprocess.run(["espeak","-v","en-us+f3","-s","139","-p","43","-a","142","-w",str(wav),scene[2]],check=True)
    with wave.open(str(wav)) as w: sec=w.getnframes()/w.getframerate()+1.25
    clip=TMP/f"clip_{i}.mp4"
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate","12","-t",str(sec),"-i",str(pic),"-i",str(wav),"-filter_complex","[1:a]apad[a]","-map","0:v:0","-map","[a]","-c:v","libx264","-preset","fast","-crf","27","-pix_fmt","yuv420p","-c:a","aac","-b:a","96k","-ar","44100","-t",str(sec),str(clip)],check=True)
    clips.append(clip)
concat=TMP/"list.txt";concat.write_text("".join("file '"+str(p)+"'\n" for p in clips))
pitch=OUT/"cobrosol-hackathon-pitch.mp4"
subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy","-movflags","+faststart",str(pitch)],check=True)
# Directly rasterize the project's established checkmark graphic for Colosseum.
logo=Image.new("RGB",(512,512),"#0B2118")
d=ImageDraw.Draw(logo)
d.rounded_rectangle((13,13,499,499),radius=80,outline="#356B50",width=11)
d.ellipse((137,106,375,344),fill="#133D2D",outline=MINT,width=19)
d.line((193,228,239,275,322,185),fill=MINT,width=27,joint="curve")
d.text((102,398),"COBROSOL",font=face(42,True),fill=MINT)
logo_path=OUT/"cobrosol-logo.png";logo.save(logo_path)
print(f"Pitch={pitch} ({pitch.stat().st_size} bytes); Logo={logo_path} ({logo_path.stat().st_size} bytes)")
