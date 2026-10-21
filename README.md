<div align="center">

  <h1>Hi there, I'm Lê Hoàng Long (<code>@longurara</code>) 🌙</h1>

  <!-- Typing Subtitle -->
  <a href="https://github.com/longurara">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1200&amp;color=CBA6F7&amp;center=true&amp;vCenter=true&amp;width=750&amp;lines=Building+cozy+experiences+%26+low-level+tools+after+midnight+%E2%98%95;Unity+WebGL+%2F+WebAssembly+ports+%26+3D+browser+games+%F0%9F%8E%AE;Compilers%2C+C%2B%2B+search+engines+%26+Manifest+V3+extensions+%F0%9F%9B%A0%EF%B8%8F;Local-first+apps%2C+audiophile+players+%26+light+novel+readers+%F0%9F%8E%A7" alt="Typing SVG" />
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

#### 🎮 WebAssembly, 3D Web & Cozy Games
| Project | What it is | Stack & Links |
| :--- | :--- | :--- |
| **[DontStarveWasm](https://github.com/longurara/DontStarveWasm)** | Browser-native **WebAssembly** engine & verification port of *Don't Starve Together*. Compiles **C++17 + Lua 5.1.5** (`Emscripten`) across 3 isolated WASM Workers (`Client`, `Master`, `Caves`), packs 4,030 Lua scripts into 16 SHA-256 verified bundles, decodes `KTEX`/`BILD6`/`ANIM4` via WebGL2 `OffscreenCanvas`, commits atomic 2-shard checkpoints to `IndexedDB`, and links peers over `RTCDataChannel` (**WebRTC**). | `C++17` `Lua 5.1` `Wasm` `Emscripten` `WebGL2` `WebRTC` |
| **[ChillWithYou_Wasm](https://github.com/longurara/ChillWithYou_Wasm)** | Standalone **Unity WebGL2 / WebAssembly** port of *Chill with You: Lo-Fi Story*. Features a custom `lilToon` SM4.5 → SM3.5 shader pipeline, unbatched static room meshes, 233 LZ4 AssetPacks with a 3-tier `CacheStorage` preloader (`0ms` RAM-pinned outfit/decor swaps), 152 Lo-Fi tracks, 30-channel ambient mixer, Pomodoro/Diary suite, and C# native uGUI bindings. | `C#` `Unity WebGL` `Wasm` `Python` `ShaderLab` |
| **[LASTLIGHT (`Gun_game`)](https://github.com/longurara/Gun_game)** | Browser-native 3D third-person **Battle Royale survival shooter**. Drop onto a `4×4 km` island with **100 AI bots** (or a `200m` blitz arena), loot weapons/armor, drive vehicles, and survive the shrinking zone. Supports desktop KB/M + mobile touch & HTTPS gyroscope aiming with zero game server. | `TypeScript` `Babylon.js` `Vite` · [**Live Demo ↗**](https://gun-game-fawn.vercel.app) |

#### ⚙️ Compilers, Languages & Systems Tooling
| Project | What it is | Stack & Links |
| :--- | :--- | :--- |
| **[Omni-Lang](https://github.com/longurara/Omni-Lang)** | Custom object-oriented programming language & interpreter written in **C++** (`Lexer` → `Parser` → `Runtime`). Ships with a rich standard library (`Math`, `JSON`, `Regex`, `CSV`, `File I/O`), a dedicated **VS Code IntelliSense extension** (`vscode-omni`), and multilingual docs (`EN` / `VI` / `RU`). | `C++` `CMake` `VS Code API` |
| **[Searching-Software](https://github.com/longurara/Searching-Software)** | **C++ Intelli-Search** — interactive CLI source-code search engine built with **Trie prefix indexing**, typo-tolerant fuzzy matching, frequency ranking, and real-time autocomplete. | `C++` `Trie` `Algorithms` |
| **[AutoGradeJava](https://github.com/longurara/AutoGradeJava)** | Desktop GUI & CLI automated grading runner in Python for compiling, executing, and scoring Java OOP student submissions. | `Python` `Java` `Tkinter` |
| **[WinUtilities-Pro](https://github.com/longurara/WinUtilities-Pro)** | Categorized batch application installer for Windows powered by `winget` and custom automation scripts with live log streaming. | `Windows` `Winget` `Automation` |

#### 🧩 Chrome Extensions & Local-First Web Apps
| Project | What it is | Stack & Links |
| :--- | :--- | :--- |
| **[tudienoffline](https://github.com/longurara/tudienoffline)** | **★ 48 Stars** · Zero-backend, 100% client-side **English ↔ Vietnamese Offline Dictionary**. Runs directly in the browser with a multi-tier dataset architecture (`2.2 MB+` 8-shard chunked manifest) and instant local search. | `JavaScript` `Offline-First` `HTML/CSS` |
| **[FAP-GPA-Viewer](https://github.com/longurara/FAP-GPA-Viewer)** | **FAP Dashboard v6.2** — Chrome Web Store extension for FPT University students: GPA calculation & simulation, smart timetable scheduling, exam countdowns, and study analytics. | `Manifest V3` `JavaScript` · [**Web ↗**](https://fap-gpa-viewer.vercel.app) · [**Chrome Store ↗**](https://chromewebstore.google.com/detail/fpt-academic-portal-dashb/pkfcnophcekokdfobdkbliaainejbdhn) |
| **[FAP-Auto-Move-Class](https://github.com/longurara/FAP-Auto-Move-Class)** | Zero-dependency Chrome Web Store extension that maps open university classes onto a visual week grid, highlights timetable clashes, and grabs open seats automatically using existing browser sessions. | `Manifest V3` `Zero-Backend` · [**Chrome Store ↗**](https://chromewebstore.google.com/detail/fap-auto-move-class/ghigbogpfhpgcogmbjehjpfigpgcalof) |
| **[recall_extension](https://github.com/longurara/recall_extension)** | **Recall** — Offline web page time-machine & archiver. Captures self-contained DOM snapshots via **Chrome DevTools Protocol (`chrome.debugger`)** & `MutationObserver`, compresses with `gzip` into `IndexedDB`, and features visual DOM diffing & full-text search. | `JavaScript` `CDP` `IndexedDB` `Gzip` |
| **[Search-docx-pdf-pptx](https://github.com/longurara/Search-docx-pdf-pptx)** | Client-side multi-format document search utility for indexing and querying inside `.docx`, `.pdf`, and `.pptx` files locally in the browser. | `HTML5` `JavaScript` · [**Live ↗**](https://search-docx-pdf-pptx.vercel.app) |
| **[CapturetoChatGPT](https://github.com/longurara/CapturetoChatGPT)** · **[Presentation_Random](https://github.com/longurara/Presentation_Random)** · **[FuOverflowAutoDownload](https://github.com/longurara/FuOverflowAutoDownload)** | Workflow micro-extensions: one-click slide cropper to ChatGPT clipboard, Google Slides random jumper (`Shift+Alt+R`), and batch attachment downloader. | `Chrome Extensions` `Manifest V3` |

#### 🎧 Cozy Media, Audio Players & Light Novel Readers
| Project | What it is | Stack & Links |
| :--- | :--- | :--- |
| **[Flutter_music_app](https://github.com/longurara/Flutter_music_app)** | Desktop-first cross-platform audiophile player with **Vinyl turntable & CD deck themes**, `media_kit` Hi-Res/lossless playback, Windows **WASAPI Exclusive** bit-perfect output, 5-band EQ, mic room calibration, synced lyrics (`lrclib`), and Google Drive streaming. | `Flutter` `Dart` `C++` `WASAPI` |
| **[Swift-music-app](https://github.com/longurara/Swift-music-app)** | **MusicGlass** — Native iOS SwiftUI music player concept with animated liquid-glass (glassmorphism) gradient blobs and `AVPlayer` streaming. | `Swift` `SwiftUI` `AVPlayer` |
| **[otonariNoTenshi](https://github.com/longurara/otonariNoTenshi)** | Mobile-first Light Novel reader workbench & EPUB/PDF/DOCX pipeline featuring character catalogs, reading stats, vocabulary flashcards, TTS audio, and **MediaPipe** hand-gesture camera navigation. | `Node.js` `JavaScript` `MediaPipe` · [**Live ↗**](https://otonari-no-tenshi.vercel.app) |
| **[hako_downloader](https://github.com/longurara/hako_downloader)** | Local Web UI + CLI crawler and downloader for the Hako / DocLN light novel ecosystem with volume selection, built-in DNS switcher, and clean `EPUB` / `TXT` generation. | `Node.js` `Express` `EPUB` |
| **[demo_Sports-Center-Management-System](https://github.com/longurara/demo_Sports-Center-Management-System)** | Multi-role management frontend prototype (Manager, Receptionist, Coach, Member) built for `SWP391`. | `React` `TypeScript` `Ant Design` · [**Live ↗**](https://frontend-eta-ruddy-61.vercel.app) |

<br />

### 🛠️ `~/toolbox`

| Domain | Stack & Tooling | Low-Level APIs & Internals |
| :--- | :--- | :--- |
| **🎮 Wasm & 3D Web** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/wasm/wasm-original.svg" width="34" height="34" alt="WebAssembly" title="WebAssembly" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/unity/cdd6f4" width="34" height="34" alt="Unity" title="Unity" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/babylonjs/babylonjs-original.svg" width="34" height="34" alt="Babylon.js" title="Babylon.js" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/webgl/f38ba8" width="34" height="34" alt="WebGL2" title="WebGL2" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg" width="34" height="34" alt="C++" title="C++" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg" width="34" height="34" alt="C#" title="C#" /> | `Emscripten` · `ShaderLab SM3.5` · `OffscreenCanvas` · `LZ4 AssetPacks` · `KTEX / ANIM4` |
| **⚙️ Systems & Langs** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg" width="34" height="34" alt="C" title="C" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/lua/lua-original.svg" width="34" height="34" alt="Lua" title="Lua 5.1" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="34" height="34" alt="Python" title="Python" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" width="34" height="34" alt="Java" title="Java" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cmake/cmake-original.svg" width="34" height="34" alt="CMake" title="CMake" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/junit/junit-original.svg" width="34" height="34" alt="JUnit" title="JUnit" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/powershell/powershell-original.svg" width="34" height="34" alt="PowerShell" title="PowerShell" /> | `Custom AST Interpreters` · `Trie & Fuzzy Indexing` · `Ninja` · `TDD / DDT` · `Winget CLI` |
| **🧩 Browser & Web** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" width="34" height="34" alt="TypeScript" title="TypeScript" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="34" height="34" alt="JavaScript" title="JavaScript" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" width="34" height="34" alt="React" title="React 18" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vitejs/vitejs-original.svg" width="34" height="34" alt="Vite" title="Vite" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original.svg" width="34" height="34" alt="Chrome" title="Chrome Extensions" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/webrtc/f9e2af" width="34" height="34" alt="WebRTC" title="WebRTC" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/antdesign/antdesign-original.svg" width="34" height="34" alt="Ant Design" title="Ant Design" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" width="34" height="34" alt="HTML5" title="HTML5" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" width="34" height="34" alt="CSS3" title="CSS3" /> | `Manifest V3` · `Chrome DevTools Protocol` · `IndexedDB` · `CacheStorage` · `Gzip DOM Diff` |
| **🎧 Apps, Audio & Dev** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg" width="34" height="34" alt="Flutter" title="Flutter" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/dart/dart-original.svg" width="34" height="34" alt="Dart" title="Dart" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swift/swift-original.svg" width="34" height="34" alt="Swift" title="Swift / SwiftUI" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nodejs/nodejs-original.svg" width="34" height="34" alt="Node.js" title="Node.js" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/express/cdd6f4" width="34" height="34" alt="Express" title="Express.js" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="34" height="34" alt="Git" title="Git" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/githubactions/githubactions-original.svg" width="34" height="34" alt="GitHub Actions" title="GitHub Actions" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" width="34" height="34" alt="VS Code" title="VS Code" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/visualstudio/visualstudio-original.svg" width="34" height="34" alt="Visual Studio" title="Visual Studio" /> | `WASAPI Exclusive` · `5-Band EQ DSP` · `MediaPipe Vision` · `AVPlayer / media_kit` · `EPUB / TTS` |

<br />

### 📊 `~/stats`

<div align="center">
  <img src="https://streak-stats.demolab.com?user=longurara&amp;theme=catppuccin-mocha&amp;hide_border=true&amp;background=1E1E2E&amp;ring=CBA6F7&amp;fire=F5C2E7&amp;currStreakLabel=CBA6F7" height="165" alt="GitHub Streak" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=longurara&amp;layout=compact&amp;theme=catppuccin_mocha&amp;hide_border=true&amp;bg_color=1e1e2e&amp;title_color=cba6f7&amp;text_color=cdd6f4&amp;langs_count=8" height="165" alt="Top Languages" />
</div>

<br />

---

<div align="center">
  <sub><i>"Quiet nights, warm coffee, lo-fi beats, and code that runs where it shouldn't."</i> ☕✨</sub>
</div>
