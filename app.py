import streamlit as st
import time
from pathlib import Path

st.set_page_config(page_title="For Rein ❤️", page_icon="💗", layout="wide", initial_sidebar_state="collapsed")

her_name = "Rein"
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
music_files = list_real_files(MUSIC_DIR)
music_file = music_files[0] if music_files else None

secret_videos = list_real_files(SECRET_DIR)

@st.cache_data(show_spinner=False)
def load_photo(path_str):
    """Shrink big photos once so the page loads fast."""
    try:
        from PIL import Image, ImageOps
        import io
        img = Image.open(path_str)
        img = ImageOps.exif_transpose(img)
        img.thumbnail((900, 900))
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=82)
        return buf.getvalue()
    except Exception:
        with open(path_str, "rb") as f:
            return f.read()

def unique_files(files):
    """Skip files with exactly the same content (Streamlit crashes on identical videos)."""
    import hashlib
    seen, result = set(), []
    for f in files:
        h = hashlib.md5()
        with open(f, "rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                h.update(chunk)
        digest = h.hexdigest()
        if digest not in seen:
            seen.add(digest)
            result.append(f)
    return result

def show_video(path, key, **kwargs):
    try:
        st.video(str(path), key=key, **kwargs)
    except TypeError:
        st.video(str(path), **kwargs)

@st.cache_data(show_spinner=False)
def load_bytes(path_str):
    with open(path_str, "rb") as f:
        return f.read()

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
.poem-text { color:white; text-align:center; font-size:19px; line-height:1.9; white-space:pre-line; }
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

# ================= CONFETTI + BALLOONS =================
def confetti_burst():
    st.components.v1.html("""
<script>
(function(){
const P = window.parent;
const doc = P.document;
const old = doc.getElementById("fx-canvas");
if (old) old.remove();
const canvas = doc.createElement("canvas");
canvas.id = "fx-canvas";
canvas.style.cssText = "position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:999999;";
doc.body.appendChild(canvas);
const ctx = canvas.getContext("2d");
canvas.width = P.innerWidth; canvas.height = P.innerHeight;
let pieces = [];
for (let i=0;i<250;i++){pieces.push({x:Math.random()*canvas.width,y:-20-Math.random()*400,size:Math.random()*10+4,speed:Math.random()*5+3,rotation:Math.random()*360,color:`hsl(${Math.random()*360},100%,70%)`});}
const balloonEmojis = ["🎈","❤️","💗","💖","🎈"];
let balloons = [];
for (let i=0;i<28;i++){balloons.push({x:Math.random()*canvas.width,y:canvas.height+60+Math.random()*500,speed:Math.random()*2.5+1.5,size:Math.random()*30+36,sway:Math.random()*2*Math.PI,e:balloonEmojis[Math.floor(Math.random()*balloonEmojis.length)]});}
let t = 0;
function animate(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  pieces.forEach(p=>{p.y+=p.speed;p.rotation+=5;ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.rotation*Math.PI/180);ctx.fillStyle=p.color;ctx.fillRect(-p.size/2,-p.size/2,p.size,p.size);ctx.restore();});
  balloons.forEach(b=>{b.y-=b.speed;ctx.font=b.size+"px serif";ctx.fillText(b.e,b.x+Math.sin(t/30+b.sway)*25,b.y);});
  t++;
  if (t < 420) { P.requestAnimationFrame(animate); } else { canvas.remove(); }
}
animate();
})();
</script>
""", height=0)

# ================= HERO =================
st.markdown(f"""
<div style="padding-top:30px;">
<div class="hero-title">For You, {her_name} 💗</div>
<div class="hero-subtitle">A little universe I made just for you, my love ❤️</div>
</div>
""", unsafe_allow_html=True)

if "started" not in st.session_state:
    st.session_state.started = False

if st.button("✨ Begin Our Story ✨"):
    st.session_state.started = True
    st.balloons()
    confetti_burst()
    st.success(f"Welcome, {her_name} ❤️ This whole place is yours.")

# ================= INTRO =================
st.markdown(f"""
<div class="glass-card">
<h2 style="color:white;text-align:center;font-family:'Dancing Script',cursive;font-size:42px;">To My Love, My Favorite Person 💗</h2>
<p style="color:white;text-align:center;font-size:19px;line-height:1.9;">
{her_name}, I could have sent you a simple message. Instead I built you a little world, because that's what you are to me — a whole world.<br><br>
Every poem, picture and song here is a piece of how I feel about you. Come back to it whenever you want to remember how loved you are. ❤️
</p>
</div>
""", unsafe_allow_html=True)

# ================= MUSIC =================
st.markdown('<div class="section-title">🎵 Our Little Soundtrack</div>', unsafe_allow_html=True)
if music_file:
    mime_map = {".mp3": "audio/mpeg", ".mpeg": "audio/mpeg", ".wav": "audio/wav", ".m4a": "audio/mp4", ".ogg": "audio/ogg"}
    mime = mime_map.get(music_file.suffix.lower(), "audio/mpeg")
    st.markdown('<div class="glass-card"><p style="color:white;text-align:center;font-size:19px;">🎶 Press play, this one is for us...</p></div>', unsafe_allow_html=True)
    st.audio(load_bytes(str(music_file)), format=mime, autoplay=st.session_state.started)
    size_mb = music_file.stat().st_size / (1024 * 1024)
    st.markdown(f'<div class="memory-caption">🎧 {music_file.name} ({size_mb:.1f} MB)</div>', unsafe_allow_html=True)
else:
    st.info("Put your music file in `assets/music/`")

# ================= HOW YOU CAME =================
st.markdown('<div class="section-title">🌹 How You Came Into My Life</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="glass-card">
<p style="color:white;text-align:center;font-size:19px;line-height:1.9;">
I wasn't looking for anything the day you appeared.<br>
My life was quiet, ordinary, and fine — until you.<br><br>
You didn't arrive with thunder. You arrived like morning light — slowly, softly — and then suddenly it was everywhere, and I couldn't imagine the room without it.<br><br>
Somewhere between your first smile and your first "good night," I stopped being someone who had a heart, and became someone whose heart had a home. And that home was you.<br><br>
Believe me, after meeting you I don't like to talk to anyone. Even when there are a lot of people around, my heart only wants you, jan. ❤️
</p>
</div>
""", unsafe_allow_html=True)

# ================= POEMS =================
st.markdown('<div class="section-title">📜 Poems For You</div>', unsafe_allow_html=True)

poems = [
    ("Before You", """Before you, my days were pages left unwritten,
my nights were rooms with the lights turned low.
Then you walked in, and the whole sky
learned how to glow.

You are the answer to my prayer
I never knew how to say,
the reason my heart still wakes up smiling
at the start of every day."""),

    ("Your Name", f"""I have said your name a thousand ways,
whispered, laughed, and sighed,
and every time it sounds like home,
like something kind inside.

{her_name}, {her_name}, soft as rain,
steady as the sea.
Say it once, and the whole world
turns gently back to me."""),

    ("1.5 Years", """1.5 years of mornings made brighter,
1.5 years of storms we walked through,
all this time learning the shape of a soul
and finding it fits with mine, so true.

If love is a garden, then you are the spring,
the sun, the rain, and the seed.
I'd spend a hundred lifetimes more
just being close to you, indeed."""),

    ("Your Heart", """There is a universe in the way you look at me,
a calm I never found in any other sea.
When you smile, the stars forget to shine,
because they know the brightest light is thine.

If I could only keep one thing in the end,
not the wealth, not the world, my dearest love,
I'd keep the quiet way you say my name,
and the way my whole life changed when you came."""),

    ("Always", f"""I don't promise you a perfect road,
I promise you my hand.
I don't promise you a flawless sky,
I promise you I'll stand.

Through every season, every storm,
through every changing tide,
{her_name}, I will love you still,
and thank you so much for loving me, jan,
with nothing left to hide."""),
]

for title, text in poems:
    st.markdown(f"""
<div class="glass-card">
<h2 style="color:white;text-align:center;font-family:'Dancing Script',cursive;font-size:38px;">{title}</h2>
<div class="poem-text">{text}</div>
</div>
""", unsafe_allow_html=True)

# ================= PHOTOS =================
st.markdown('<div class="section-title">📸 My Favorite View: You</div>', unsafe_allow_html=True)
if photos:
    for i in range(0, len(photos), 3):
        row = photos[i:i+3]
        cols = st.columns(len(row))
        for col, photo in zip(cols, row):
            with col:
                st.image(load_photo(str(photo)), width=320)
else:
    st.info("Add your pictures to `assets/photos/`")

# ================= VIDEOS (muted) =================
st.markdown('<div class="section-title">🎥 You, In Motion</div>', unsafe_allow_html=True)
if videos:
    for vi, video in enumerate(unique_files(videos)):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            show_video(video, f"memory_video_{vi}", autoplay=True, loop=True, muted=True)
else:
    st.info("Add your videos to `assets/videos/`")

# ================= LETTER =================
st.markdown('<div class="section-title">💌 A Letter For You</div>', unsafe_allow_html=True)

letter_text = f"""My dearest {her_name},

I don't think words will ever be enough to explain how much you mean to me.

When you stepped into my life, without even trying you changed everything. You taught me what it means to be understood without explaining, to be held without being touched, and to be loved on my worst days as much as my best.

With you, silence is comfortable, laughter comes easily, and even ordinary days feel like something worth keeping. You are my peace after a long day and my favorite reason to smile.

I love the way you care. I love the way you laugh. I love the way you make hard things feel lighter just by being there. I love you in the big moments, and even more in the small ones that nobody else sees.

Thank you for choosing me. Thank you for staying. Thank you for being exactly who you are.

I don't know what the future holds, but I know I want you in every part of it.

Always and forever yours,
{your_name} ❤️"""

if st.button("✨ Open My Heart"):
    placeholder = st.empty()
    displayed = ""
    for char in letter_text:
        displayed += char
        placeholder.markdown(f'<div class="glass-card"><div class="letter">{displayed}▌</div></div>', unsafe_allow_html=True)
        time.sleep(0.012)

# ================= REASONS =================
st.markdown('<div class="section-title">❤️ Why I Love You</div>', unsafe_allow_html=True)
reasons = [
    "Because you make me feel at home, no matter where we are or how far apart we are. You are the only person close to my heart.",
    "Because your smile can fix my whole day in a second.",
    "Because you listen, truly listen, with your whole heart.",
    "Because you believe in me even when I forget to believe in myself.",
    "Because you are gentle and strong at the same time.",
    "Because you turned ordinary moments into my favorite memories.",
    "Because with you, I am the best version of myself.",
    "Because even after all this time, my heart still skips when you say my name.",
    "Because you are my best friend, my love, and my peace.",
    "Because I can't picture my life without you in it.",
]
for n, reason in enumerate(reasons, 1):
    st.markdown(f'<div class="glass-card"><h2 style="color:white;font-family:\'Dancing Script\',cursive;font-size:32px;">{n}. {reason}</h2></div>', unsafe_allow_html=True)

# ================= PROMISES =================
st.markdown('<div class="section-title">🤍 My Promises</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
<p style="color:white;text-align:center;font-size:21px;line-height:2;">
I promise to choose you on easy days and on hard ones.<br>
I promise to listen, to learn, and to grow with you.<br>
I promise to make you laugh when the world feels heavy.<br>
I promise to hold your hand, in this life and in every one after. ❤️
</p>
</div>
""", unsafe_allow_html=True)

# ================= SECRET =================
st.markdown('<div class="section-title">🔐 Something I Hid For You</div>', unsafe_allow_html=True)
password = st.text_input("💗 Enter the secret words", type="password", placeholder="Only you know this...")
if password:
    if " ".join(password.lower().split()) == "i love u rein":
        confetti_burst()
        st.markdown(f"""
<div class="glass-card">
<h1 style="font-family:'Dancing Script',cursive;color:white;text-align:center;font-size:60px;">🔓 You Found It ❤️</h1>
<p style="color:white;text-align:center;font-size:20px;line-height:1.9;">
You knew the words, {her_name}. Of course you did.<br><br>
But honestly, the real secret is that no website, no poem, and no song could ever fully explain what you mean to me. ❤️
</p>
</div>
""", unsafe_allow_html=True)
        if secret_videos:
            for si, vid in enumerate(unique_files(secret_videos)):
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.markdown('<p style="color:white;text-align:center;font-size:18px;">One more thing... 💞</p>', unsafe_allow_html=True)
                    show_video(vid, f"secret_video_{si}", autoplay=True)
        else:
            st.info("Put your secret videos in `assets/secret/`")
    else:
        st.warning("Hmm... that's not the secret words 😏")

# ================= FINAL =================
st.markdown('<div class="section-title">🎁 One Last Thing...</div>', unsafe_allow_html=True)
if st.button("💗 Open My Final Surprise 💗"):
    st.balloons()
    confetti_burst()
    st.markdown(f"""
<div class="final-message">
<h1>{her_name} ❤️</h1>
<p>I LOVE YOU SO MUCH, more than everything in this world.</p>
<p>So much time has passed, and my heart still falls for you every single day and every second. Whatever comes next, I want to face it beside you.</p>
<p>Thank you for being my love, my light, and my home.</p>
<h1>I love you, my {her_name} ❤️</h1>
<p>Forever yours,<br>{your_name} 💌</p>
</div>
""", unsafe_allow_html=True)
