# Chianda Senior School - Student Voting & Real-Time Election Analysis System (CSSEC)

> **Motto:** *Strive To Excel* • **Established:** 1968 • **Siaya County, Kenya**  
> **Official Election Cycle:** 2026/2027 Student Council General Elections

A secure, mobile-first, role-based student voting and real-time election analysis system built specifically for **Chianda Senior School**. Designed with an authentic, distinguished school aesthetic (**Deep Navy Blue, Emerald Green, and Imperial Gold accents**) featuring micro-animations, cryptographic one-vote locking, live voter turnout tracking, and certified exportable reports.

---

## 🌟 Key Features

### 1. Unique School-Themed Landing & Portal Entry
- **School Heraldic Crest**: Custom SVG crest featuring the Chianda gold torch of knowledge, open book of wisdom, sports laurels, and emerald cross divider.
- **Live Polls Countdown Timer**: Real-time countdown clock counting down to poll closure.
- **Real-Time Voter Turnout Ticker**: Live participation percentage and progress bar reflecting all verified votes cast across grades.
- **Two-Tab Authentication Portal**:
  - **Student Voter Portal**: Admission Number (e.g. `CHS-2023-0104`) & 4-digit security PIN.
  - **Electoral Commission Admin Portal**: Commissioner ID (`COMMISSIONER-01`) & Security PIN (`8899`).
  - **Instant Demo Switchers**: One-click demo credentials directly on-screen for frictionless testing.

### 2. Student Voter Experience (The Ballot Box)
- **Role Verification & One-Vote Lock**: Verifies the student's Admission Number, Form (Form 1–4), and House (Aggrey, Oginga, Achieng Oneko, Tom Mboya, Krapf, Livingstone).
- **Double-Voting Prevention**: Once a student has cast their ballot, any subsequent login automatically redirects them to an official **"Vote Verified & Sealed"** receipt screen.
- **Cryptographic Confirmation Hash**: Displays a SHA-256 style 64-character verification hash and printable receipt proving participation **without compromising ballot secrecy**.
- **Interactive Multi-Position Stepper**:
  - 1. School President (Head Boy / Council Chair)
  - 2. Deputy School President (Welfare & Discipline)
  - 3. Dining Hall & Catering Captain
  - 4. Games & Sports Captain
  - 5. Academic Secretary (Library & Peer Mentorship)
  - 6. Environment & Health Captain
- **Candidate Manifesto Cards**: Includes candidate portrait, Form, House badge, 1-sentence campaign slogan, and an expandable modal with 3 policy pillars, leadership history, and faculty endorsement.
- **Review & Cast**: Summary review table where students inspect their selections before submitting, followed by a celebratory full-screen confetti animation.

### 3. Real-Time Voting Analysis Dashboard
- **Live Turnout Demographics**:
  - Breakdown by Form (Form 1, Form 2, Form 3, Form 4).
  - Breakdown by School Dormitory / House with color coding.
- **Position-by-Position Horizontal Bar Charts**: Exact vote counts, percentage shares to 1 decimal place, and live lead margins (+X votes ahead of 2nd place).
- **Projected Winner & Tie Detection**:
  - Highlights the leading nominee with a `"PROJECTED WINNER"` badge (or `"OFFICIALLY ELECTED"` with gold crown when closed).
  - Automatically flags exact ties with an amber banner: `⚠️ TIE DETECTED - RUNOFF REQUIRED`.
- **Exportable Official Results Report**: One-click *"Generate Official Election Report"* button producing a certified Chianda Senior School letterhead document ready for printing or saving to PDF, including returning officer and principal signature lines.

### 4. Electoral Commission Admin Control Panel
- **Operational Controls**: Single-click toggles to Start / Open Polls, Pause Voting, or Close & Certify.
- **Simulate Real-Time Incoming Vote**: Button to simulate an unvoted student submitting a ballot in real time, triggering live ledger updates and chart re-rendering.
- **Auto-Feed Simulation**: Automated background ticker casting votes every 3 seconds for dynamic live demonstrations.
- **Candidate Manager**: Add, edit, or delete candidates and manifesto pledges.
- **Voter Roll Manager**: Searchable registry of all 50 students, filterable by Form, House, and status (`Voted` / `Eligible`).
- **Transparency Audit Feed**: Anonymized live audit log registering timestamps, stream origins, and cryptographic block hashes without disclosing individual candidate choices.

---

## 🚀 Instant Launch

### Method 1: Using Python (Recommended)
Double-click `start.bat` or run in terminal:
```bash
python server.py
```
This automatically starts the local server at `http://localhost:8000` and opens your default browser.

### Method 2: Direct Browser Opening
Simply double-click `index.html` in your file explorer to open it in Chrome, Edge, Firefox, or Safari.

---

## 🔑 Demo Credentials

| Role | Identifier / Adm No | PIN | Description |
| :--- | :--- | :--- | :--- |
| **Student Voter** | `CHS-2023-0104` | `2024` | **Kevin Otieno** (Form 4 East, Aggrey House) - **Ready to vote** |
| **Student Voter** | `CHS-2022-0042` | `1122` | **Brian Omondi** (Form 4 West, Oginga House) - **Already voted (Receipt Lock Demo)** |
| **Electoral Admin** | `COMMISSIONER-01` | `8899` | **Mr. Patrick Omwamba** - Chief Electoral Returning Officer |

---

## 🛠 Tech Stack

- **Frontend:** React 18, Tailwind CSS, Lucide Icons (SVG), Canvas Confetti
- **State Management:** LocalStorage with Reactive Observer pattern & event dispatching
- **Security:** SHA-256 style cryptographic receipt generation, one-vote tamper-proof locking, strict ballot secrecy
- **Print Optimization:** Dedicated `@media print` stylesheet for official PDF certificates

---

## 🏛 Chianda Senior School Electoral Code Compliance
Developed in alignment with the Chianda Senior School Student Council Constitution (Revised 2026), ensuring free, fair, transparent, and verifiable elections.
