# Lesson 1 – Newton's Cooling Law

## English
This program demonstrates **Newton’s Cooling Law** by comparing:
1) a **numerical solution** using the **Euler method**, and  
2) the **exact analytical solution**.

**What the plot shows**
- **Euler** curve (points/solid) vs **Exact** curve (dashed) on the same axes.
- A thin horizontal line at **T_env** marks the **equilibrium** temperature.
- With a **smaller time step `dt`**, the Euler curve closely **overlaps** the exact one.  
  If `dt` is large, Euler can **deviate** (visible gap).

**What the printed error means**
- The console prints the **final-time absolute error**:
  \|Euler(T_end) − Exact(T_end)\| in **°C**.  
  Smaller is better. It shrinks when you **reduce `dt`** (and usually grows if you increase `dt`).

**Parameters you can change**
- `T0` (initial temperature), `T_env` (ambient), `k` (cooling rate), `dt` (time step), `t_end` (duration).
- **Time constant**:  τ = 1/k. Larger `k` ⇒ **faster** approach to `T_env`.  
- Reducing `dt` ⇒ **higher accuracy**, more steps.

---

## فارسی
این برنامه **قانون سرد شدن نیوتن** را با مقایسهٔ  

۱) **حل عددی** به روش **اویلر** 

۲) **حل دقیق تحلیلی** نشان می‌دهد.

**نمودار چه می‌گوید؟**
- منحنی **اویلر** (نقاط/خط پیوسته) در برابر منحنی **تحلیلی** (خط‌چین) روی یک نمودار.  
- خط افقی باریک در **T_env** دمای **تعادل** را نشان می‌دهد.  
- اگر **گام زمانی `dt` کوچک** باشد، منحنی اویلر تقریباً روی منحنی تحلیلی می‌افتد؛  
  اگر `dt` بزرگ باشد، **فاصله** بین دو منحنی دیده می‌شود.

**عددِ خطایی که چاپ می‌شود یعنی چه؟**
- در خروجی ترمینال، **خطای مطلق در زمان نهایی** چاپ می‌شود:  
  \|Euler(T_end) − Exact(T_end)\| بر حسب **°C**.  
  هرچه کوچک‌تر باشد بهتر است؛ با **کوچک‌کردن `dt`** معمولاً کمتر می‌شود.

**پارامترهایی که می‌توانی عوض کنی**
- `T0` (دمای اولیه)، `T_env` (دمای محیط)، `k` (نرخ سردشدن)، `dt` (گام زمانی)، `t_end` (مدت شبیه‌سازی).  
- **ثابت زمانی**:  
  $$
  \tau = \frac{1}{k}
  $$
  هرچه $k$ بزرگ‌تر باشد، رسیدن به $T_{env}$ سریع‌تر است.

- کوچک‌کردن `dt` ⇒ **دقت بالاتر** (ولی گام‌های بیشتر).

---

## Français
Ce programme illustre la **loi du refroidissement de Newton** en comparant  
1) une **solution numérique** par la **méthode d’Euler**, et  
2) la **solution analytique exacte**.

**Ce que montre la figure**
- Courbe **Euler** (points/plein) vs courbe **Exact** (pointillé) sur les mêmes axes.  
- Une ligne horizontale fine à **T_env** indique la **température d’équilibre**.  
- Avec un **pas de temps `dt` plus petit**, la courbe d’Euler **coïncide** avec l’exacte ;  
  si `dt` est grand, on observe un **écart**.

**Signification de l’erreur affichée**
- La console affiche l’**erreur absolue au temps final** :  
  \|Euler(T_end) − Exact(T_end)\| en **°C**.  
  Plus c’est petit, mieux c’est. Elle diminue en **réduisant `dt`**.

**Paramètres modifiables**
- `T0` (température initiale), `T_env` (ambiante), `k` (taux de refroidissement), `dt` (pas), `t_end` (durée).  
- **Constante de temps** :  τ = 1/k. Un `k` plus grand ⇒ approche **plus rapide** de `T_env`.  
- Diminuer `dt` ⇒ **meilleure précision** (plus d’itérations).

---
