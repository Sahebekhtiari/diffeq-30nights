# Differential Equations in 30 Nights

This project contains nightly lessons and code for learning ODE, PDE, and SDE
with real-world applications in biology, computer science, and mathematics.

## Structure

---

## Project Map / نقشه پروژه / Plan du projet

- **`lessons/`** → nightly lesson scripts (code you can run)  
  اسکریپت‌های هر جلسه (قابل اجرا)  
  Scripts de cours (exécutables)
  - `lesson1_intro.py` → Newton’s Cooling: Euler vs. exact
- **`notes/`** → lesson handouts & explanations (Markdown)  
  جزوه‌ها و توضیحات هر جلسه (مارک‌داون)  
  Supports de cours et explications (Markdown)
  - `lesson1_notes.md` → DE basics + Newton’s Cooling + Euler
- **`notebooks/`** → Jupyter notebooks per session  
  نوت‌بوک‌های ژوپیتر هر جلسه  
  Notebooks Jupyter par séance
- **`src/`** → reusable library code  
  کدهای بازاستفاده‌شونده  
  Code réutilisable
  - `models/` → mathematical models  
    مدل‌های ریاضی | Modèles mathématiques
  - `solvers/` → numerical solvers (Euler, RK, …)  
    حل‌گرهای عددی | Solveurs numériques
  - `plots/` → plotting utilities  
    ابزارهای ترسیم | Outils de tracé
- **`examples/`** → small runnable examples  
  مثال‌های کوچک قابل اجرا  
  Petits exemples exécutables
- **`data/`** → sample datasets  
  داده‌های نمونه | Jeux de données d’exemple
  - `raw/` , `processed/`
- **`tests/`** → unit tests  
  تست‌های واحد | Tests unitaires

---

## Where to start? / از کجا شروع کنم؟ / Par où commencer ?

1. **Run the first lesson code**  
   اجرای کد جلسه اول  
   Exécuter le premier script  
   ```bash
   python lessons/lesson1_intro.py
