import streamlit as st
import time
from pathlib import Path

# =====================================================
#  EDIT THESE
# =====================================================
her_name = "Rein"
your_name = "Uroosa Khan"
secret_phrase = "i love u rein"   # keep this all lowercase (typing is not case sensitive)

st.set_page_config(page_title="For Rein 🌹", page_icon="🌹", layout="wide", initial_sidebar_state="collapsed")

BASE_DIR = Path(__file__).parent
PHOTO_DIR = BASE_DIR / "assets" / "photos"
VIDEO_DIR = BASE_DIR / "assets" / "videos"
MUSIC_DIR = BASE_DIR / "assets" / "music"
SECRET_DIR = BASE_DIR / "assets" / "secret"


def list_real_files(folder, exts=None):
    if not folder.exists():
        return []
    files = [f for f in folder.glob("*") if f.is_file() and not f.name.startswith(".")]
    if exts:
        files = [f for f in files if f.suffix.lower() in exts]
    return sorted(files)


photos = list_real_files(PHOTO_DIR, {".jpg", ".jpeg", ".png", ".webp", ".gif"})
videos = list_real_files(VIDEO_DIR, {".mp4", ".mov", ".webm", ".m4v"})
secret_videos = list_real_files(SECRET_DIR, {".mp4", ".mov", ".webm", ".m4v"})
music_files = list_real_files(MUSIC_DIR, {".mp3", ".mpeg", ".wav", ".m4a", ".ogg"})
music_file = music_files[0] if music_files else None

# =====================================================
#  STYLE
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Great+Vibes&family=Jost:wght@300;400;500&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Jost', sans-serif; }

.stApp {
  background:
    radial-gradient(circle at 15% 10%, rgba(214,69,110,.28), transparent 35%),
    radial-gradient(circle at 85% 90%, rgba(150,40,90,.35), transparent 40%),
    linear-gradient(160deg, #1b0a17 0%, #2c0f24 45%, #3d1230 100%);
  background-attachment: fixed;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 5rem; }

/* Hero */
.hero-title {
  font-family: 'Great Vibes', cursive;
  font-size: clamp(64px, 11vw, 140px);
  text-align: center; color: #ffe9ef; line-height: 1.05;
  text-shadow: 0 0 30px rgba(255,100,150,.55);
  margin-top: 30px;
}
.hero-sub {
  font-family: 'Cormorant Garamond', serif; font-style: italic;
  text-align: center; color: #f6c6d4; font-size: clamp(20px, 2.6vw, 28px);
  margin: 6px 0 30px 0;
}

/* Sections */
.section-title {
  font-family: 'Great Vibes', cursive; color: #ffd3df; text-align: center;
  font-size: 58px; margin: 70px 0 20px; text-shadow: 0 0 20px rgba(255,100,150,.35);
}
.glass {
  background: rgba(255,255,255,.07); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255,190,210,.22); border-radius: 22px;
  padding: 34px 38px; margin: 20px 0; box-shadow: 0 18px 50px rgba(0,0,0,.35);
}
.prose {
  font-family: 'Cormorant Garamond', serif; color: #ffeaf0;
  font-size: 23px; line-height: 1.85; text-align: center;
}
.poem {
  font-family: 'Cormorant Garamond', serif; font-style: italic; color: #ffeaf0;
  font-size: 24px; line-height: 1.9; text-align: center; white-space: pre-line;
}
.poem-title {
  font-family: 'Great Vibes', cursive; color: #ff9fba; text-align: center; font-size: 40px; margin-bottom: 8px;
}
.letter {
  font-family: 'Cormorant Garamond', serif; color: #ffeaf0; font-size: 23px;
  line-height: 1.9; white-space: pre-line;
}
.reason {
  font-family: 'Cormorant Garamond', serif; color: #ffeaf0; font-size: 24px; line-height: 1.6;
}
.reason i { color: #ff8fb0; font-style: normal; font-family: 'Great Vibes', cursive; font-size: 34px; margin-right: 10px; }
.caption { color: #f6c6d4; text-align: center; font-size: 15px; margin-top: 8px; font-style: italic; }

/* Buttons */
.stButton>button {
  width: 100%; border: none; border-radius: 50px; padding: 14px 26px;
  background: linear-gradient(90deg, #c2185b, #e0457b, #f06292); color: #fff;
  font-size: 17px; font-weight: 500; letter-spacing: .3px;
  box-shadow: 0 10px 28px rgba(224,69,123,.4); transition: .3s;
}
.stButton>button:hover { transform: translateY(-3px); box-shadow: 0 14px 34px rgba(224,69,123,.6); color:#fff; }

/* Media */
.stImage img { border-radius: 18px !important; box-shadow: 0 14px 34px rgba(0,0,0,.45); max-height: 340px; object-fit: cover; transition: transform .4s ease; }
.stImage img:hover { transform: scale(1.03); }
video { border-radius: 18px !important; box-shadow: 0 14px 34px rgba(0,0,0,.45); max-height: 420px; }

/* Input */
.stTextInput input { border-radius: 40px; text-align: center; background: rgba(255,255,255,.1); color: #fff; border: 1px solid rgba(255,190,210,.4); }
.stTextInput label p { color: #ffd3df; }

/* Final */
.final { text-align: center; color: #ffe9ef; padding: 50px 10px; }
.final h1 { font-family: 'Great Vibes', cursive; font-size: clamp(50px, 8vw, 90px); text-shadow: 0 0 30px rgba(255,100,150,.6); }
.final p { font-family: 'Cormorant Garamond', serif; font-size: 25px; line-height: 1.8; }

/* Floating petals */
.petal { position: fixed; bottom: -80px; z-index: 0; pointer-events: none; animation: rise linear infinite; }
@keyframes rise {
  0% { transform: translateY(0) rotate(0deg); opacity: 0; }
  10% { opacity: .75; }
  90% { opacity: .75; }
  100% { transform: translateY(-120vh) rotate(300deg); opacity: 0; }
}
@media (prefers-reduced-motion: reduce) { .petal { display: none; } }
</style>
<div class="petal" style="left:6%;animation-duration:11s;font-size:26px;">🌹</div>
<div class="petal" style="left:22%;animation-duration:14s;font-size:20px;">💗</div>
<div class="petal" style="left:41%;animation-duration:10s;font-size:24px;">🌸</div>
<div class="petal" style="left:58%;animation-duration:15s;font-size:22px;">🌹</div>
<div class="petal" style="left:75%;animation-duration:12s;font-size:20px;">💞</div>
<div class="petal" style="left:90%;animation-duration:13s;font-size:26px;">🌸</div>
""", unsafe_allow_html=True)


# =====================================================
#  PETAL BURST
# =====================================================
def petal_burst():
    st.components.v1.html("""
<canvas id="c" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:999999;"></canvas>
<script>
const cv=document.getElementById("c"),ctx=cv.getContext("2d");
cv.width=innerWidth;cv.height=innerHeight;
const cols=["#ff6b9a","#ff9fba","#ffd3df","#e0457b","#ffffff","#f8bbd0"];
let p=[];
for(let i=0;i<220;i++)p.push({x:Math.random()*cv.width,y:-20-Math.random()*300,s:Math.random()*9+4,v:Math.random()*3+2,r:Math.random()*360,d:(Math.random()-.5)*2,c:cols[Math.floor(Math.random()*cols.length)]});
let t=0;
function a(){ctx.clearRect(0,0,cv.width,cv.height);
p.forEach(q=>{q.y+=q.v;q.x+=q.d+Math.sin((q.y+t)/40);q.r+=3;
ctx.save();ctx.translate(q.x,q.y);ctx.rotate(q.r*Math.PI/180);ctx.fillStyle=q.c;
ctx.beginPath();ctx.ellipse(0,0,q.s,q.s/2,0,0,Math.PI*2);ctx.fill();ctx.restore();});
t++; if(t<600) requestAnimationFrame(a); else ctx.clearRect(0,0,cv.width,cv.height);}
a();
</script>
""", height=0)


# =====================================================
#  HERO
# =====================================================
st.markdown(f"""
<div class="hero-title">For {her_name}</div>
<div class="hero-sub">All this time with you, and I would choose every day again.</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if st.button("🌹 Begin Our Story 🌹"):
        st.balloons()
        petal_burst()
        st.success(f"Welcome, {her_name}. This whole place is yours. ❤️")

# =====================================================
#  INTRO
# =====================================================
st.markdown(f"""
<div class="glass">
<div class="prose">
{her_name}, I could have sent you a message. Instead I built you a small world,
because that's what you are to me, a whole world.<br><br>
Every poem, picture and song on this page is a piece of how I feel about you.
Take your time. Come back whenever you want to remember how loved you are.
</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
#  MUSIC
# =====================================================
st.markdown('<div class="section-title">Our Song</div>', unsafe_allow_html=True)
if music_file:
    st.markdown('<div class="glass"><div class="prose">Press play, and let this one be for us. 🎶</div></div>', unsafe_allow_html=True)
    with open(music_file, "rb") as audio:
        st.audio(audio.read(), format="audio/mpeg", autoplay=True)
else:
    st.info("Put your song in `assets/music/` (mp3, wav, m4a...)")

# =====================================================
#  HOW SHE CAME INTO MY LIFE
# =====================================================
st.markdown('<div class="section-title">How You Came Into My Life</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="glass">
<div class="prose">
I wasn't looking for anything the day you appeared.<br>
My life was quiet, ordinary, and fine, until you.<br><br>
You didn't arrive with thunder. You arrived like morning light,
slowly, softly, and then suddenly it was everywhere,
and I couldn't imagine the room without it.<br><br>
Somewhere between your first smile and your first "good night,"
I stopped being someone who had a heart
and became someone whose heart had a home. And that home was you.<br><br>
Believe me, after meeting you I don't like to talk to anyone.
Even when there are a lot of people around, my heart only wants you, jan.
{her_name} ❤️
</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
#  POEMS
# =====================================================
st.markdown('<div class="section-title">Poems For You</div>', unsafe_allow_html=True)

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
    st.markdown(f'<div class="glass"><div class="poem-title">{title}</div><div class="poem">{text}</div></div>', unsafe_allow_html=True)

# =====================================================
#  PHOTOS
# =====================================================
st.markdown('<div class="section-title">Our Memories</div>', unsafe_allow_html=True)
if photos:
    for i in range(0, len(photos), 3):
        row = photos[i:i + 3]
        cols = st.columns(len(row))
        for j, (col, photo) in enumerate(zip(cols, row)):
            with col:
                st.image(str(photo), use_container_width=True)
                st.markdown(f'<div class="caption">Memory {i + j + 1} 🤍</div>', unsafe_allow_html=True)
else:
    st.info("Add your pictures to `assets/photos/`")

# =====================================================
#  VIDEOS
# =====================================================
st.markdown('<div class="section-title">Us, In Motion</div>', unsafe_allow_html=True)
if videos:
    for video in videos:
        a, b, c = st.columns([1, 2, 1])
        with b:
            st.video(str(video), muted=True)
else:
    st.info("Add your videos to `assets/videos/`")

# =====================================================
#  LETTER
# =====================================================
st.markdown('<div class="section-title">A Letter For You</div>', unsafe_allow_html=True)

letter_text = f"""My dearest {her_name},

I have tried to write this letter many times, and every time the words feel too small.

When you stepped into my life, without trying you changed everything. You taught me what it means to be understood without explaining, to be held without being touched, and to be loved on my worst days as much as my best.

With you, silence is comfortable, laughter comes easily, and even ordinary days feel like something worth keeping. You are my peace after a long day and my favorite reason to smile.

I love the way you care. I love the way you laugh. I love the way you make hard things feel lighter just by being there. I love you in the big moments, and even more in the small ones that nobody else sees.

Thank you for choosing me. Thank you for staying. Thank you for being exactly who you are.

I don't know what the future holds, but I know I want you in every part of it.

Always and forever yours,
{your_name} ❤️"""

if st.button("💌 Open My Heart"):
    holder = st.empty()
    shown = ""
    for ch in letter_text:
        shown += ch
        holder.markdown(f'<div class="glass"><div class="letter">{shown}▌</div></div>', unsafe_allow_html=True)
        time.sleep(0.012)
    holder.markdown(f'<div class="glass"><div class="letter">{shown}</div></div>', unsafe_allow_html=True)

# =====================================================
#  REASONS
# =====================================================
st.markdown('<div class="section-title">Why I Love You</div>', unsafe_allow_html=True)
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
for n, r in enumerate(reasons, 1):
    st.markdown(f'<div class="glass"><div class="reason"><i>{n}</i>{r}</div></div>', unsafe_allow_html=True)

# =====================================================
#  PROMISES
# =====================================================
st.markdown('<div class="section-title">My Promises</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass">
<div class="poem">I promise to choose you on easy days and on hard ones.
I promise to listen, to learn, and to grow with you.
I promise to make you laugh when the world feels heavy.
I promise to hold your hand, in this life and in every one after.</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
#  SECRET
# =====================================================
st.markdown('<div class="section-title">Something I Hid For You</div>', unsafe_allow_html=True)
st.markdown('<div class="caption">Only you know the words. Say them to open it.</div>', unsafe_allow_html=True)

password = st.text_input("🔐 Enter the secret words", type="password", placeholder="Three little words, and your name...")
if password:
    if " ".join(password.lower().split()) == secret_phrase:
        petal_burst()
        st.markdown(f"""
<div class="glass">
<div class="poem-title" style="font-size:64px;">You found it, {her_name} 🔓</div>
<div class="prose">
You knew the words. Of course you did.<br><br>
The truth is, the real secret was never hidden:
I love you more than any page, poem or song could ever say.
</div>
</div>
""", unsafe_allow_html=True)
        if secret_videos:
            for vid in secret_videos:
                a, b, c = st.columns([1, 2, 1])
                with b:
                    st.markdown('<div class="caption" style="font-size:18px;">One more thing, just for you... 💞</div>', unsafe_allow_html=True)
                    st.video(str(vid))
        else:
            st.info("Put your secret videos in `assets/secret/`")
    else:
        st.warning("Hmm... that's not it, my love. Try again 😉")

# =====================================================
#  FINAL
# =====================================================
st.markdown('<div class="section-title">One Last Thing</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    final_click = st.button("💗 Open My Final Surprise 💗")
if final_click:
    st.balloons()
    petal_burst()
    st.markdown(f"""
<div class="final">
<h1>{her_name}</h1>
<p>I love you more than words can hold, more than time can count.</p>
<p>So much time has passed, and my heart still falls for you every single day and every second.
Whatever comes next, I want to face it beside you.</p>
<p>Thank you for being my love, my light, and my home.</p>
<h1>I love you so much, and thank you so much for everything, {her_name} ❤️</h1>
<p>Forever yours,<br>{your_name} 💌</p>
</div>
""", unsafe_allow_html=True)
