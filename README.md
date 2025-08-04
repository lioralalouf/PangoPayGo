פרויקט אוטומציה למשימת בית למשרת QA Automation – בדיקות למערכת ניהול חניון.

---
##  טכנולוגיות:
- Python 3.13.3
- Pytest
- Selenium
- Logging להדפסה לטרמינל

---
##  מבנה הפרויקט:
project/ │ └── api/ ├── ui/ │├── pageObjects/tests ├── utils/ ├── docs/ │ ├── STP_Document.md │ ├── STD_Document.pdf│ ├── bug_reports.md │ Improvement_Suggestions.md|└── screenshots/ ├── conftest.py ├└── README.md


---
 הרצת הבדיקות:
```
הרצת כלל הבדיקות:
pytest --browser=chrome --env=prod --headless
משתני סביבה זמינים:
ENV – סביבה (אפשרויות: dev, staging, prod)
BROWSER – דפדפן (אפשרויות: chrome, firefox)
🧪 תוכן הבדיקות:
בדיקות UI בעזרת Selenium
מבנה Page Object מודולרי
שימוש בלוגים לצורך מעקב ו-debugging
תמיכה בהרצה לפי דפדפן וסביבה
📄 תיעוד הבדיקות:
בתיקיית docs/ נמצאים:

STP_Document.md – מסמך תכנון הבדיקות (Software Test Plan)
STD.md_Document – טבלאות תרחישי בדיקה (Software Test Design)
Bug_Report.md – דו"חות באגים מלאים כולל תיאור, שחזור, תוצאה צפויה וקישורים לתמונות
Improvement_Suggestions - הצעות לשיפור וייעול המערכת

Screenshots:
 כל הבאגים כוללים קישור לתמונות שנמצאות בתיקייה /screenshots/.

📌 הערות נוספות:
כל טסט כולל assert ברור והדפסות לוג למסך.
הפרויקט מודולרי ונקי, נבנה לפי עקרונות תכנות מונחה עצמים (OOP).
התיעוד מקיף ומציג הבנה תהליכית של כל שלב בבדיקות.
מתאים להרצה מקומית בסביבות שונות עם דפדפנים שונים.
