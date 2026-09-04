import streamlit as st
import time
from pathlib import Path

st.set_page_config(page_title="For Sado ❤️", page_icon="💗", layout="wide", initial_sidebar_state="collapsed")

friend_name = "Sado"
your_name = "Uroosa Khan"

BASE_DIR = Path(__file__).parent
PHOTO_DIR = BASE_DIR / "assets" / "photos"
VIDEO_DIR = BASE_DIR / "assets" / "videos"
MUSIC_DIR = BASE_DIR / "assets" / "music"
SECRET_DIR = BASE_DIR / "assets" / "secret"

def list_real_files(folder):
    if not folder.exists():
        return []
    return sorted(f for f in folder.glob("*") if f.is_file() and not f.name.startswith("."))

photos = list_real_files(PHOTO_DIR)
videos = list_real_files(VIDEO_DIR)
music_file = MUSIC_DIR / "birthday.mp3.mpeg"

secret_videos = list_real_files(SECRET_DIR)

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp {
background: radial-gradient(circle at 10% 20%, rgba(255,255,255,0.3), transparent 20%),
radial-gradient(circle at 90% 80%, rgba(255,255,255,0.25), transparent 25%),
linear-gradient(-45deg, #ff758c, #ff7eb3, #ff9a9e, #fad0c4, #fbc2eb);
background-size: 200% 200%;
animation: bgMove 15s ease infinite;
}
@keyframes bgMove { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
#MainMenu, footer { visibility: hidden; }
.block-container { max-width: 1100px; padding-top: 2rem; padding-bottom: 4rem; }
.hero-title { font-family:'Dancing Script',cursive; font-size:clamp(50px,8vw,100px); font-weight:700; color:white; text-align:center; text-shadow:0 0 10px rgba(255,255,255,.5),0 0 25px rgba(255,80,130,.7),0 5px 20px rgba(0,0,0,.2); }
.hero-subtitle { text-align:center; color:white; font-size:19px; margin-bottom:30px; }
.glass-card { background:rgba(255,255,255,.2); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border:1px solid rgba(255,255,255,.35); border-radius:26px; padding:32px; margin:22px 0; box-shadow:0 15px 40px rgba(0,0,0,.15); }
.section-title { font-family:'Dancing Script',cursive; color:white; text-align:center; font-size:50px; margin-top:60px; margin-bottom:25px; text-shadow:0 4px 15px rgba(0,0,0,.2); }
.stButton>button { width:100%; border:none; border-radius:50px; padding:14px 25px; background:linear-gradient(90deg,#ff416c,#ff4b8b,#ff758c); color:white; font-size:17px; font-weight:600; box-shadow:0 10px 25px rgba(255,65,108,.35); transition:.3s; }
.stButton>button:hover { transform:translateY(-4px) scale(1.02); box-shadow:0 15px 35px rgba(255,65,108,.5); }
.stImage img { border-radius:20px !important; box-shadow:0 12px 30px rgba(0,0,0,.25); transition: transform .35s ease; max-height: 320px; object-fit: cover; }
.stImage img:hover { transform: scale(1.03); }
video { border-radius:20px !important; box-shadow:0 12px 30px rgba(0,0,0,.25); max-height: 400px; }
.memory-caption { color:white; text-align:center; font-size:15px; margin-top:8px; opacity:.9; }
.letter { color:white; font-size:19px; line-height:1.9; white-space:pre-line; }
.final-message { text-align:center; color:white; padding:60px 20px; }
.final-message h1 { font-family:'Dancing Script',cursive; font-size:70px; }
.final-message p { font-size:20px; }
.heart { position:fixed; bottom:-80px; z-index:0; pointer-events:none; animation:floatHeart linear infinite; }
@keyframes floatHeart { 0%{transform:translateY(0) rotate(0deg); opacity:0} 10%{opacity:.8} 90%{opacity:.8} 100%{transform:translateY(-120vh) rotate(360deg); opacity:0} }
</style>
<div class="heart" style="left:5%;animation-duration:9s;">❤️</div>
<div class="heart" style="left:20%;animation-duration:12s;">💗</div>
<div class="heart" style="left:38%;animation-duration:8s;">💕</div>
<div class="heart" style="left:55%;animation-duration:13s;">💖</div>
<div class="heart" style="left:72%;animation-duration:10s;">❤️</div>
<div class="heart" style="left:88%;animation-duration:11s;">💗</div>
""", unsafe_allow_html=True)

# ================= CONFETTI =================
def confetti_burst():
    st.components.v1.html("""
<canvas id="confetti" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:999999;"></canvas>
<script>
const canvas=document.getElementById("confetti");const ctx=canvas.getContext("2d");
canvas.width=window.innerWidth;canvas.height=window.innerHeight;
let pieces=[];
for(let i=0;i<250;i++){pieces.push({x:Math.random()*canvas.width,y:-20,size:Math.random()*10+4,speed:Math.random()*5+3,rotation:Math.random()*360,color:`hsl(${Math.random()*360},100%,70%)`});}
function animate(){ctx.clearRect(0,0,canvas.width,canvas.height);pieces.forEach(p=>{p.y+=p.speed;p.rotation+=5;ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.rotation*Math.PI/180);ctx.fillStyle=p.color;ctx.fillRect(-p.size/2,-p.size/2,p.size,p.size);ctx.restore();});requestAnimationFrame(animate);}
animate();
</script>
""", height=0)

# ================= HERO =================
st.markdown(f"""
<div style="padding-top:30px;">
<div class="hero-title">Happy Birthday, {friend_name} 🎂</div>
<div class="hero-subtitle">A little universe I made just for you, sis ❤️</div>
</div>
""", unsafe_allow_html=True)

if st.button("✨ Begin Your Birthday Journey ✨"):
    st.balloons()
    confetti_burst()
    st.success(f"Welcome to your special day, {friend_name} ❤️")

# ================= INTRO =================
st.markdown("""
<div class="glass-card">
<h2 style="color:white;text-align:center;font-family:'Dancing Script',cursive;font-size:42px;">To My Sister, My Favorite Person 💗</h2>
<p style="color:white;text-align:center;font-size:19px;line-height:1.9;">
Today isn't just another day. It's the day the world got lucky enough to have you in it — and I got the extra luck of getting to grow up with you.<br><br>
So instead of just a birthday message, I wanted to give you a collection of memories, words, and feelings — something you can come back to whenever you miss me. ❤️
</p>
</div>
""", unsafe_allow_html=True)

# ================= MUSIC (autoplay) =================
st.markdown('<div class="section-title">🎵 Our Little Soundtrack</div>', unsafe_allow_html=True)
if music_file.exists():
    st.markdown('<div class="glass-card"><p style="color:white;text-align:center;font-size:19px;">🎶 Playing our song for you...</p></div>', unsafe_allow_html=True)
    with open(music_file, "rb") as audio:
        st.audio(audio.read(), format="audio/mpeg", autoplay=True)
else:
    st.info("Put your music file at `assets/music/birthday.mp3.mpeg`")

# ================= PHOTOS =================
st.markdown('<div class="section-title">📸 Our Memories</div>', unsafe_allow_html=True)
if photos:
    for i in range(0, len(photos), 3):
        row = photos[i:i+3]
        cols = st.columns(len(row))
        for col, photo in zip(cols, row):
            with col:
                st.image(str(photo), width=320)
                st.markdown(f'<div class="memory-caption">Memory #{photos.index(photo)+1} ❤️</div>', unsafe_allow_html=True)
else:
    st.info("Add your pictures to `assets/photos/`")

# ================= VIDEOS (muted) =================
st.markdown('<div class="section-title">🎥 Our Memories In Motion</div>', unsafe_allow_html=True)
if videos:
    for video in videos:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video(str(video), muted=True)
else:
    st.info("Add your videos to `assets/videos/`")

# ================= LETTER =================
st.markdown('<div class="section-title">💌 A Letter For You</div>', unsafe_allow_html=True)

letter_text = """My Sado Jan,

I don't think words will ever be enough to explain how much you mean to me.

Growing up with you feels different from anything else — calmer, warmer, more like home. You're the person I think of first and last, every single day.

If sisterhood were made of memories, I'd choose every single one with you — the laughter we couldn't stop, the fights that never really counted, and the times when the whole world seemed to disappear and it was simply you and me.

Some people are just relatives. But you became my person — the place where everything feels right.

Happy Birthday, Sado. Thank you for being one of the most beautiful chapters of my life.

Forever your sister,
Uroosa Khan ❤️"""

if st.button("✨ Open My Heart"):
    placeholder = st.empty()
    displayed = ""
    for char in letter_text:
        displayed += char
        placeholder.markdown(f'<div class="glass-card"><div class="letter">{displayed}▌</div></div>', unsafe_allow_html=True)
        time.sleep(0.012)

# ================= REASONS =================
st.markdown('<div class="section-title">❤️ Why You Are Special</div>', unsafe_allow_html=True)
reasons = [
    "You've looked out for me like a second mother — with so much love, care, and warmth.",
    "You took care of me, protected me, and made sure I was okay, even when I didn't know how to say I needed it.",
    "Ahahah, somehow you even scolded me like a mother does, but those scoldings taught me so much and made me a better person.",
    "You taught me things I will carry with me for the rest of my life.",
    "You gave me a kind of protection and comfort that made me feel safe and loved.",
    "Thank you for giving me some of the best memories of my entire life.",
    "I will always be grateful to you — for the memories, and for making our family feel even more like home.",
    "Because of you, I've felt a warmth of love that I had never felt so deeply before.",
    "Thank you for making me feel cared for, protected, and loved in a way I will never forget.",
    "I really, really love you so much, and no matter where life takes us, I will always be grateful for everything you've given me.",
    "Thank you for being my sister, my friend, and one of the biggest reasons home feels like home."
]
for n, reason in enumerate(reasons, 1):
    st.markdown(f'<div class="glass-card"><h2 style="color:white;font-family:\'Dancing Script\',cursive;font-size:32px;">{n}. {reason}</h2></div>', unsafe_allow_html=True)

# ================= SPECIAL DAY MESSAGE =================
st.markdown('<div class="section-title">🎂 Your Special Day</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
<p style="color:white;text-align:center;font-size:26px;font-family:'Dancing Script',cursive;">Today is my favorite day. Happy Birthday again, Sado 🎂❤️</p>
</div>
""", unsafe_allow_html=True)

# ================= SECRET =================
st.markdown('<div class="section-title">🔐 Something I Hid For You</div>', unsafe_allow_html=True)
password = st.text_input("💗 Enter the secret word", type="password", placeholder="Only you know this...")
if password:
    if password.lower() == "love u":
        confetti_burst()
        st.markdown("""
<div class="glass-card">
<h1 style="font-family:'Dancing Script',cursive;color:white;text-align:center;font-size:60px;">🔓 You Found It ❤️</h1>
<p style="color:white;text-align:center;font-size:20px;line-height:1.9;">
If you're reading this, congratulations — you found the secret message.<br><br>
But honestly, the real secret is that no website, no poem, and no birthday present could ever fully explain what you mean to me. ❤️
</p>
</div>
""", unsafe_allow_html=True)
        if secret_videos:
            for vid in secret_videos:
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.markdown('<p style="color:white;text-align:center;font-size:18px;">One more thing... 🐱❤️</p>', unsafe_allow_html=True)
                    st.video(str(vid))  # unmuted by default
        else:
            st.info("Put your secret videos in `assets/secret/`")
    else:
        st.warning("Hmm... that's not the secret word 😏")

# ================= FINAL =================
st.markdown('<div class="section-title">🎁 One Last Thing...</div>', unsafe_allow_html=True)
if st.button("💗 Open My Final Surprise 💗"):
    st.balloons()
    confetti_burst()
    st.markdown(f"""
<div class="final-message">
<h1>Sado ❤️</h1>
<p>I LOVE YOU SO MUCH more than Everything in this world.</p>
<p>No matter how much distance comes between us, no matter how much life changes, I hope you always remember that you are deeply loved, deeply valued, and incredibly special to me.</p>
<p>Thank you for being you.</p>
<h1>Happy Birthday, My Sister Sado 🎂❤️</h1>
<p>Forever yours,<br>{your_name} 💌</p>
</div>
""", unsafe_allow_html=True)