<!-- Header Banner -->
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&amp;color=0:8839ef,100:ea76cb&amp;height=120&amp;section=header" />
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:cba6f7,100:f5c2e7&amp;height=120&amp;section=header" width="100%" alt="" />
</picture>

<div align="center">

  <h1>Hi there, I'm Lê Hoàng Long (<code>@longurara</code>) 🌙</h1>

  <!-- Typing Subtitle -->
  <a href="https://github.com/longurara">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1200&amp;color=8839EF&amp;center=true&amp;vCenter=true&amp;width=750&amp;lines=Building+cozy+experiences+%26+low-level+tools+after+midnight+%E2%98%95;Unity+WebGL+%2F+WebAssembly+ports+%26+3D+browser+games+%F0%9F%8E%AE;Compilers%2C+C%2B%2B+search+engines+%26+Manifest+V3+extensions+%F0%9F%9B%A0%EF%B8%8F;Local-first+apps%2C+audiophile+players+%26+light+novel+readers+%F0%9F%8E%A7" />
      <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1200&amp;color=CBA6F7&amp;center=true&amp;vCenter=true&amp;width=750&amp;lines=Building+cozy+experiences+%26+low-level+tools+after+midnight+%E2%98%95;Unity+WebGL+%2F+WebAssembly+ports+%26+3D+browser+games+%F0%9F%8E%AE;Compilers%2C+C%2B%2B+search+engines+%26+Manifest+V3+extensions+%F0%9F%9B%A0%EF%B8%8F;Local-first+apps%2C+audiophile+players+%26+light+novel+readers+%F0%9F%8E%A7" alt="Typing SVG" />
    </picture>
  </a>

  <br />

  <!-- Minimal Cozy Badges -->
  <a href="https://github.com/longurara?tab=repositories">
    <img src="https://img.shields.io/badge/repos-35%2B%20public-cba6f7?style=flat-square&amp;labelColor=1e1e2e&amp;logo=github&amp;logoColor=cdd6f4" alt="Public Repositories" />
  </a>
  <a href="https://github.com/longurara">
    <img src="https://img.shields.io/github/stars/longurara?affiliations=OWNER&amp;label=stars&amp;style=flat-square&amp;color=f9e2af&amp;labelColor=1e1e2e&amp;logo=github&amp;logoColor=cdd6f4" alt="Total Stars" />
  </a>
  <a href="https://github.com/longurara?tab=followers">
    <img src="https://img.shields.io/github/followers/longurara?label=followers&amp;style=flat-square&amp;color=89b4fa&amp;labelColor=1e1e2e&amp;logo=github&amp;logoColor=cdd6f4" alt="Followers" />
  </a>
  <a href="mailto:hikarilong@gmail.com">
    <img src="https://img.shields.io/badge/email-hikarilong%40gmail.com-f5c2e7?style=flat-square&amp;labelColor=1e1e2e&amp;logo=gmail&amp;logoColor=cdd6f4" alt="Email" />
  </a>

</div>

<br />

### 🌙 `~/about-me`

Hey, I'm **Long** (`@longurara`) — a Software Engineering student at **FPT University** who loves taking apart software to see how it ticks, then rebuilding it into something fast, local-first, and pleasant to use.

Most of my evenings go into porting desktop/Unity/C++ games to **WebAssembly**, writing **C++ interpreters & search tools**, crafting **zero-backend Chrome extensions**, and building cozy media utilities for music and light novels.

```yaml
name: Lê Hoàng Long (@longurara)
education: Software Engineering @ FPT University
vibe: lo-fi playlists, late-night debugging, light novels & rhythm/cozy games

what_i_build:
  webassembly_and_3d: [C++/Emscripten & Unity WebGL2 ports, ShaderLab SM3.5, Babylon.js 3D web games]
  systems_and_langs:  [C++17/20, Lua 5.1, C#, Java, Python, custom AST interpreters, Trie/fuzzy indexing]
  browser_and_local:  [Manifest V3 extensions, Chrome DevTools Protocol, IndexedDB, CacheStorage, WebRTC]
  desktop_and_mobile: [Flutter (WASAPI Exclusive audio), SwiftUI (iOS), Windows winget tooling]

philosophy: "No unnecessary servers. Fast startup, offline-friendly, built to actually be used."
```

<br />

### 🗂️ `~/project-index`

<details open>
<summary><b>🎮 WebAssembly, 3D Web & Cozy Games</b></summary>
<br />

| Project | What it is | Stack |
| :--- | :--- | :--- |
| **[DontStarveWasm](https://github.com/longurara/DontStarveWasm)** | Browser-native **WebAssembly** port of *Don't Starve Together* — C++17 + Lua 5.1 across 3 WASM Workers, WebGL2 `OffscreenCanvas` asset decoding, `IndexedDB` checkpoints & **WebRTC** multiplayer. | `C++17` `Lua` `Wasm` `WebGL2` `WebRTC` |
| **[ChillWithYou_Wasm](https://github.com/longurara/ChillWithYou_Wasm)** | **Unity WebGL2** port of *Chill with You: Lo-Fi Story* — custom SM4.5 → SM3.5 shader pipeline, 3-tier `CacheStorage` preloader, 152 lo-fi tracks & ambient mixer. | `C#` `Unity` `Wasm` `ShaderLab` |
| **[LASTLIGHT](https://github.com/longurara/Gun_game)**<br /><sub>[Live demo ↗](https://gun-game-fawn.vercel.app)</sub> | 3D third-person **Battle Royale** in the browser — `4×4 km` island, **100 AI bots**, vehicles, shrinking zone, mobile touch & gyro aiming, zero game server. | `TypeScript` `Babylon.js` `Vite` |

</details>

<details>
<summary><b>⚙️ Compilers, Languages & Systems Tooling</b></summary>
<br />

| Project | What it is | Stack |
| :--- | :--- | :--- |
| **[Omni-Lang](https://github.com/longurara/Omni-Lang)** | Object-oriented language & interpreter in **C++** (`Lexer` → `Parser` → `Runtime`) with a rich stdlib and a **VS Code IntelliSense extension**. | `C++` `CMake` `VS Code API` |
| **[Searching-Software](https://github.com/longurara/Searching-Software)** | CLI source-code search engine with **Trie prefix indexing**, typo-tolerant fuzzy matching & live autocomplete. | `C++` `Trie` |
| **[AutoGradeJava](https://github.com/longurara/AutoGradeJava)** | GUI & CLI runner that compiles, executes and scores Java OOP student submissions. | `Python` `Java` `Tkinter` |
| **[WinUtilities-Pro](https://github.com/longurara/WinUtilities-Pro)** | Categorized batch app installer for Windows powered by `winget`, with live log streaming. | `Windows` `Winget` |

</details>

<details>
<summary><b>🧩 Chrome Extensions & Local-First Web Apps</b></summary>
<br />

| Project | What it is | Stack |
| :--- | :--- | :--- |
| **[tudienoffline](https://github.com/longurara/tudienoffline)**<br /><sub>★ 48 stars</sub> | Zero-backend **English ↔ Vietnamese offline dictionary** with an 8-shard chunked dataset and instant local search. | `JavaScript` `Offline-First` |
| **[FAP-GPA-Viewer](https://github.com/longurara/FAP-GPA-Viewer)**<br /><sub>[Web ↗](https://fap-gpa-viewer.vercel.app) · [Chrome Store ↗](https://chromewebstore.google.com/detail/fpt-academic-portal-dashb/pkfcnophcekokdfobdkbliaainejbdhn)</sub> | **FAP Dashboard** for FPT University students — GPA simulation, smart timetable, exam countdowns & study analytics. | `Manifest V3` `JavaScript` |
| **[FAP-Auto-Move-Class](https://github.com/longurara/FAP-Auto-Move-Class)**<br /><sub>[Chrome Store ↗](https://chromewebstore.google.com/detail/fap-auto-move-class/ghigbogpfhpgcogmbjehjpfigpgcalof)</sub> | Maps open classes onto a visual week grid, flags timetable clashes and grabs open seats automatically. | `Manifest V3` `Zero-Backend` |
| **[recall_extension](https://github.com/longurara/recall_extension)** | **Recall** — offline web-page time machine: CDP DOM snapshots, `gzip` into `IndexedDB`, visual DOM diff & full-text search. | `JavaScript` `CDP` `IndexedDB` |
| **[Search-docx-pdf-pptx](https://github.com/longurara/Search-docx-pdf-pptx)**<br /><sub>[Live ↗](https://search-docx-pdf-pptx.vercel.app)</sub> | Client-side search inside `.docx`, `.pdf` and `.pptx` files, fully in the browser. | `HTML5` `JavaScript` |
| **[CapturetoChatGPT](https://github.com/longurara/CapturetoChatGPT)** · **[Presentation_Random](https://github.com/longurara/Presentation_Random)** · **[FuOverflowAutoDownload](https://github.com/longurara/FuOverflowAutoDownload)** | Workflow micro-extensions: slide cropper → ChatGPT, Google Slides random jumper, batch attachment downloader. | `Manifest V3` |

</details>

<details>
<summary><b>🎧 Cozy Media, Audio Players & Light Novel Readers</b></summary>
<br />

| Project | What it is | Stack |
| :--- | :--- | :--- |
| **[Flutter_music_app](https://github.com/longurara/Flutter_music_app)** | Audiophile player with **vinyl & CD deck themes**, Hi-Res playback, **WASAPI Exclusive** bit-perfect output, 5-band EQ & synced lyrics. | `Flutter` `Dart` `C++` |
| **[Swift-music-app](https://github.com/longurara/Swift-music-app)** | **MusicGlass** — iOS SwiftUI player concept with animated liquid-glass gradient blobs. | `Swift` `SwiftUI` |
| **[otonariNoTenshi](https://github.com/longurara/otonariNoTenshi)**<br /><sub>[Live ↗](https://otonari-no-tenshi.vercel.app)</sub> | Light novel reader & EPUB/PDF/DOCX pipeline with flashcards, TTS and **MediaPipe** hand-gesture navigation. | `Node.js` `MediaPipe` |
| **[hako_downloader](https://github.com/longurara/hako_downloader)** | Web UI + CLI downloader for Hako / DocLN light novels with clean `EPUB` / `TXT` output. | `Node.js` `Express` |
| **[Sports Center MS](https://github.com/longurara/demo_Sports-Center-Management-System)**<br /><sub>[Live ↗](https://frontend-eta-ruddy-61.vercel.app)</sub> | Multi-role management frontend prototype (Manager, Receptionist, Coach, Member) for `SWP391`. | `React` `TypeScript` `Ant Design` |

</details>

<br />

### 🛠️ `~/toolbox`

| Domain | Stack, Tooling & Internals |
| :--- | :--- |
| **🎮 Wasm & 3D Web** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/wasm/wasm-original.svg" width="32" height="32" alt="WebAssembly" title="WebAssembly" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/unity/9399b2" width="32" height="32" alt="Unity" title="Unity" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/babylonjs/babylonjs-original.svg" width="32" height="32" alt="Babylon.js" title="Babylon.js" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/webgl/f38ba8" width="32" height="32" alt="WebGL2" title="WebGL2" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg" width="32" height="32" alt="C++" title="C++" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg" width="32" height="32" alt="C#" title="C#" /><br /><sub>`Emscripten` · `ShaderLab SM3.5` · `OffscreenCanvas` · `LZ4 AssetPacks` · `KTEX / ANIM4`</sub> |
| **⚙️ Systems & Langs** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg" width="32" height="32" alt="C" title="C" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/lua/lua-original.svg" width="32" height="32" alt="Lua" title="Lua 5.1" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="32" height="32" alt="Python" title="Python" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" width="32" height="32" alt="Java" title="Java" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cmake/cmake-original.svg" width="32" height="32" alt="CMake" title="CMake" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/junit/junit-original.svg" width="32" height="32" alt="JUnit" title="JUnit" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/powershell/powershell-original.svg" width="32" height="32" alt="PowerShell" title="PowerShell" /><br /><sub>`Custom AST Interpreters` · `Trie & Fuzzy Indexing` · `Ninja` · `TDD / DDT` · `Winget CLI`</sub> |
| **🧩 Browser & Web** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" width="32" height="32" alt="TypeScript" title="TypeScript" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="32" height="32" alt="JavaScript" title="JavaScript" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" width="32" height="32" alt="React" title="React 18" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vitejs/vitejs-original.svg" width="32" height="32" alt="Vite" title="Vite" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original.svg" width="32" height="32" alt="Chrome" title="Chrome Extensions" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/webrtc/f9e2af" width="32" height="32" alt="WebRTC" title="WebRTC" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/antdesign/antdesign-original.svg" width="32" height="32" alt="Ant Design" title="Ant Design" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" width="32" height="32" alt="HTML5" title="HTML5" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" width="32" height="32" alt="CSS3" title="CSS3" /><br /><sub>`Manifest V3` · `Chrome DevTools Protocol` · `IndexedDB` · `CacheStorage` · `Gzip DOM Diff`</sub> |
| **🎧 Apps, Audio & Dev** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg" width="32" height="32" alt="Flutter" title="Flutter" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/dart/dart-original.svg" width="32" height="32" alt="Dart" title="Dart" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swift/swift-original.svg" width="32" height="32" alt="Swift" title="Swift / SwiftUI" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nodejs/nodejs-original.svg" width="32" height="32" alt="Node.js" title="Node.js" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="32" height="32" alt="Git" title="Git" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" width="32" height="32" alt="VS Code" title="VS Code" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/visualstudio/visualstudio-original.svg" width="32" height="32" alt="Visual Studio" title="Visual Studio" /><br /><sub>`WASAPI Exclusive` · `5-Band EQ DSP` · `MediaPipe Vision` · `Express` · `GitHub Actions` · `EPUB / TTS`</sub> |

<br />

### 📊 `~/stats`

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=longurara&amp;show_icons=true&amp;hide_border=true&amp;bg_color=eff1f5&amp;title_color=8839ef&amp;text_color=4c4f69&amp;icon_color=ea76cb&amp;ring_color=8839ef" />
    <img src="https://github-readme-stats.vercel.app/api?username=longurara&amp;show_icons=true&amp;theme=catppuccin_mocha&amp;hide_border=true&amp;bg_color=1e1e2e&amp;title_color=cba6f7&amp;text_color=cdd6f4&amp;icon_color=f5c2e7&amp;ring_color=cba6f7" height="165" alt="GitHub Stats" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=longurara&amp;layout=compact&amp;hide_border=true&amp;bg_color=eff1f5&amp;title_color=8839ef&amp;text_color=4c4f69&amp;langs_count=8" />
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=longurara&amp;layout=compact&amp;theme=catppuccin_mocha&amp;hide_border=true&amp;bg_color=1e1e2e&amp;title_color=cba6f7&amp;text_color=cdd6f4&amp;langs_count=8" height="165" alt="Top Languages" />
  </picture>
  <br />
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=longurara&amp;hide_border=true&amp;background=EFF1F5&amp;ring=8839EF&amp;fire=EA76CB&amp;currStreakNum=4C4F69&amp;sideNums=4C4F69&amp;currStreakLabel=8839EF&amp;sideLabels=4C4F69&amp;dates=6C6F85&amp;stroke=CCD0DA" />
    <img src="https://streak-stats.demolab.com?user=longurara&amp;theme=catppuccin-mocha&amp;hide_border=true&amp;background=1E1E2E&amp;ring=CBA6F7&amp;fire=F5C2E7&amp;currStreakLabel=CBA6F7" height="165" alt="GitHub Streak" />
  </picture>
</div>

<br />

<div align="center">
  <sub><i>"Quiet nights, warm coffee, lo-fi beats, and code that runs where it shouldn't."</i> ☕✨</sub>
</div>

<!-- Footer Banner -->
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&amp;color=0:ea76cb,100:8839ef&amp;height=90&amp;section=footer" />
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:f5c2e7,100:cba6f7&amp;height=90&amp;section=footer" width="100%" alt="" />
</picture>
