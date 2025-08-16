# Lesson 1 – Differential Equations (English)

## 1. Why are Differential Equations Important?  
Differential equations are the main mathematical tool to describe changes in the real world.  
In many phenomena, **the rate of change** depends on **the current state of the system**.  

### Real-world Examples:  
- Cooling and heating of objects (tea on a table)  
- Growth of bacteria in a lab  
- Change of drug concentration in blood  
- Voltage drop in a capacitor  
- A car slowing down when the driver removes the foot from the gas pedal  
- Estimating the lifetime of a lamp or a living cell  

---

## 2. Basic Definitions  

- **Function**: A relation that gives one specific output for each input.  
- **Derivative**: The rate of change of a function; i.e., "how fast this function is changing right now".  
- **Differential Equation**: An equation that contains both a function and its derivative.  

In simple words:  

$$
\text{Function + Its Derivative = Differential Equation}
$$  

---

## 3. Why Both Function and Derivative Appear?  

Because in real life:  
- The current value matters (e.g., tea is now 90°C).  
- Its rate of change matters too (tea is cooling by several degrees per minute).  

By combining them, we can predict the future.  
For example: “What will the temperature be after 5 minutes?”  

---

## 4. Newton’s Cooling Law  

Newton showed that:  
> The cooling rate of an object is proportional to the temperature difference between the object and the environment.  

Formula:  

$$
\frac{dT}{dt} = -k \cdot (T - T_{env})
$$  

- $T$: Object’s temperature at time $t$  
- $T_{env}$: Ambient temperature (constant)  
- $k$: Cooling coefficient (depends on object & environment)  
- Minus sign $-$: Means if the object is hotter than the environment, its temperature decreases.  

🔑 **Key Point:**  
The system always tends to reach the ambient temperature.  

🍵 **Simple Example:**  
Place a 90°C cup of tea in a 25°C room:  
- At first, it cools very fast (large difference).  
- Later, cooling slows down.  
- Finally, it stabilizes at 25°C.  

---

## 5. Approximate Solution with Euler’s Method  

Euler’s method is a simple numerical way to approximate solutions of differential equations.  

Idea:  
If we know the rate of change, we can compute the next value using a small time step $\Delta t$:  

$$
T_{new} = T_{old} + \Delta t \cdot \frac{dT}{dt}
$$  

Repeating this builds an approximate curve of the cooling process.  

---

## 6. More Examples & Applications  

- **Biology**: Predicting the growth of a tree or cell division.  
- **Medicine**: Drug concentration in blood (rises first, then decreases).  
- **Electrical Engineering**: Capacitor discharge in RC circuits.  
- **Car Mechanics**: Speed decreases when releasing the pedal.  
- **Daily Life**: Cooling coffee, estimating lifetime of a bulb.  

---

## 7. Session Summary  

- Differential equations are tools for modeling real-world changes.  
- We defined function, derivative, and differential equation.  
- Newton’s Cooling Law was introduced as the main example.  
- Euler’s method was presented as a first numerical solution.  
- Applications span medicine, engineering, biology, and daily life.  

---

# درسنامه جلسه اول – معادلات دیفرانسیل (فارسی)

## ۱. چرا معادلات دیفرانسیل مهم هستند؟  
معادلات دیفرانسیل ابزار اصلی ریاضیات برای توصیف تغییرات در دنیای واقعی هستند.  
در بسیاری پدیده‌ها، **سرعت تغییرات** به **مقدار فعلی پدیده** بستگی دارد.  

### مثال‌های واقعی:  
- سرد و گرم شدن اجسام (چای روی میز)  
- رشد جمعیت باکتری‌ها در آزمایشگاه  
- تغییر غلظت دارو در خون  
- افت ولتاژ در یک خازن  
- کاهش سرعت خودرو وقتی پای راننده از روی گاز برداشته می‌شود  
- تخمین طول عمر یک لامپ یا یک سلول زنده  

---

## ۲. تعریف پایه‌ها  

- **تابع (Function)**: رابطه‌ای که برای هر ورودی، یک خروجی مشخص می‌دهد.  
- **مشتق (Derivative)**: نرخ تغییر یک تابع؛ یعنی "این تابع در همین لحظه چه‌قدر تغییر می‌کند".  
- **معادله دیفرانسیل (Differential Equation)**: معادله‌ای که هم خود تابع و هم مشتق آن درونش حضور دارد.  

به زبان ساده:  

$$
\text{تابع + مشتق آن = معادله دیفرانسیل}
$$  

---

## ۳. چرا تابع و مشتقش با هم می‌آیند؟  

چون در دنیای واقعی:  
- مقدار فعلی مهم است (مثلاً دمای چای الان ۹۰ درجه است).  
- سرعت تغییرش هم مهم است (چای هر دقیقه چند درجه سرد می‌شود).  

با ترکیب این دو، می‌توانیم آینده را پیش‌بینی کنیم.  
مثلاً بدانیم: «بعد از ۵ دقیقه دما چند درجه خواهد شد؟»  

---

## ۴. قانون سرد شدن نیوتن (Newton’s Cooling Law)  

نیوتن نشان داد:  
> سرعت سرد شدن یک جسم متناسب است با اختلاف دمای جسم و محیط.  

فرمول:  

$$
\frac{dT}{dt} = -k \cdot (T - T_{env})
$$  

- $T$: دمای جسم در لحظهٔ $t$  
- $T_{env}$: دمای محیط (ثابت)  
- $k$: ضریب خنک‌شدن (وابسته به شرایط جسم و محیط)  
- علامت منفی $-$: یعنی اگر جسم داغ‌تر از محیط باشد، دما کاهش می‌یابد.  

🔑 **نکته کلیدی:**  
سیستم همیشه تمایل دارد دمای خودش را به دمای محیط نزدیک کند.  

🍵 **مثال ساده:**  
یک لیوان چای ۹۰ درجه را در اتاق ۲۵ درجه بگذاریم:  
- اول خیلی سریع سرد می‌شود (چون اختلاف زیاد است).  
- بعد آرام‌تر سرد می‌شود.  
- در نهایت به دمای ۲۵ درجه می‌رسد و ثابت می‌ماند.  

---

## ۵. حل تقریبی با روش اویلر (Euler’s Method)  

روش اویلر یک راه عددی ساده برای تقریب حل معادلات دیفرانسیل است.  

ایده:  
اگر نرخ تغییر را بدانیم، می‌توانیم مقدار بعدی را با یک گام کوچک زمانی $\Delta t$ حساب کنیم:  

$$
T_{new} = T_{old} + \Delta t \cdot \frac{dT}{dt}
$$  

هر بار این کار را تکرار کنیم، یک منحنی تقریبی از سرد شدن جسم می‌سازیم.  

---

## ۶. مثال‌های جذاب و کاربردی  

- **زیست‌شناسی**: پیش‌بینی سرعت رشد یک درخت یا تقسیم سلولی.  
- **پزشکی**: بررسی غلظت دارو در خون (اول بالا می‌رود، بعد به‌تدریج کاهش می‌یابد).  
- **مهندسی برق**: خالی شدن شارژ خازن در مدار RC.  
- **مکانیک خودرو**: اگر راننده پایش را از روی پدال بردارد، سرعت ماشین به مرور کم می‌شود.  
- **زندگی روزمره**: پیش‌بینی زمان خنک شدن قهوه یا طول عمر یک لامپ.  

---

## ۷. جمع‌بندی جلسه اول  

- معادلات دیفرانسیل ابزاری برای مدل‌سازی تغییرات در جهان واقعی هستند.  
- تعریف تابع، مشتق و معادله دیفرانسیل را یاد گرفتیم.  
- قانون سرد شدن نیوتن به عنوان مثال اصلی معرفی شد.  
- روش اویلر به عنوان اولین روش حل عددی را دیدیم.  
- فهمیدیم که این مفاهیم در دنیای واقعی (پزشکی، مهندسی، زیست‌شناسی و حتی زندگی روزمره) کاربرد دارند.  

---

# Leçon 1 – Les équations différentielles (Français)

## 1. Pourquoi les équations différentielles sont-elles importantes ?  
Les équations différentielles sont l’outil principal des mathématiques pour décrire les changements dans le monde réel.  
Dans de nombreux phénomènes, **la vitesse de changement** dépend de **l’état actuel du système**.  

### Exemples réels :  
- Refroidissement et chauffage des objets (thé sur une table)  
- Croissance des bactéries dans un laboratoire  
- Variation de la concentration d’un médicament dans le sang  
- Chute de tension dans un condensateur  
- Ralentissement d’une voiture lorsque le conducteur retire son pied de l’accélérateur  
- Estimation de la durée de vie d’une ampoule ou d’une cellule vivante  

---

## 2. Définitions de base  

- **Fonction** : Relation qui donne une sortie spécifique pour chaque entrée.  
- **Dérivée** : Le taux de variation d’une fonction ; c’est-à-dire "quelle est la vitesse de changement en ce moment".  
- **Équation différentielle** : Une équation qui contient à la fois une fonction et sa dérivée.  

En termes simples :  

$$
\text{Fonction + Sa dérivée = Équation différentielle}
$$  

---

## 3. Pourquoi la fonction et sa dérivée apparaissent-elles ensemble ?  

Parce que dans la vie réelle :  
- La valeur actuelle compte (par ex., le thé est maintenant à 90°C).  
- Le taux de variation compte aussi (le thé refroidit de quelques degrés par minute).  

En les combinant, nous pouvons prédire l’avenir.  
Par exemple : “Quelle sera la température après 5 minutes ?”  

---

## 4. Loi du refroidissement de Newton  

Newton a montré que :  
> La vitesse de refroidissement d’un objet est proportionnelle à la différence de température entre l’objet et l’environnement.  

Formule :  

$$
\frac{dT}{dt} = -k \cdot (T - T_{env})
$$  

- $T$ : Température de l’objet à l’instant $t$  
- $T_{env}$ : Température ambiante (constante)  
- $k$ : Coefficient de refroidissement (dépend de l’objet et de l’environnement)  
- Signe négatif $-$ : signifie que si l’objet est plus chaud que l’environnement, sa température diminue.  

🔑 **Point clé :**  
Le système tend toujours à atteindre la température ambiante.  

🍵 **Exemple simple :**  
Un verre de thé à 90°C placé dans une pièce à 25°C :  
- Au début, il refroidit très rapidement (grande différence).  
- Ensuite, le refroidissement ralentit.  
- Finalement, il se stabilise à 25°C.  

---

## 5. Solution approchée avec la méthode d’Euler  

La méthode d’Euler est un moyen numérique simple d’approximer les solutions des équations différentielles.  

Idée :  
Si nous connaissons la vitesse de changement, nous pouvons calculer la valeur suivante avec un petit pas de temps $\Delta t$ :  

$$
T_{new} = T_{old} + \Delta t \cdot \frac{dT}{dt}
$$  

En répétant cela, on obtient une courbe approchée du processus de refroidissement.  

---

## 6. Autres exemples et applications  

- **Biologie** : Prédiction de la croissance d’un arbre ou division cellulaire.  
- **Médecine** : Concentration d’un médicament dans le sang (augmente d’abord, puis diminue progressivement).  
- **Génie électrique** : Décharge d’un condensateur dans un circuit RC.  
- **Mécanique automobile** : La vitesse diminue quand on relâche la pédale.  
- **Vie quotidienne** : Refroidissement du café, durée de vie d’une ampoule.  

---

## 7. Résumé de la session  

- Les équations différentielles modélisent les changements dans le monde réel.  
- Nous avons défini fonction, dérivée et équation différentielle.  
- La loi du refroidissement de Newton a été introduite comme exemple principal.  
- La méthode d’Euler a été présentée comme première solution numérique.  
- Applications : médecine, ingénierie, biologie et vie quotidienne.  
